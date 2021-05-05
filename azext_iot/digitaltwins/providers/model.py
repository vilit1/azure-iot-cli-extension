# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
from azext_iot.common.utility import process_json_arg, scantree, unpack_msrest_error
from azext_iot.digitaltwins.providers.base import DigitalTwinsProvider
from azext_iot.sdk.digitaltwins.dataplane.models import ErrorResponseException
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


def get_model_dependencies(model):
    """Return a list of dependency DTMIs for a given model"""
    dependencies = []

    if "contents" in model:
        components = [item["schema"] for item in model["contents"] if item["@type"] == "Component"]
        dependencies += components

    if "extends" in model:
        # Models defined in a DTDL can implement extensions of up to two interfaces.
        # These interfaces can be in the form of a DTMI reference, or a nested model.
        if isinstance(model["extends"], str):
            # If its just a string, thats a single DTMI reference, so just add that to our list
            dependencies.append(model["extends"])
        elif isinstance(model["extends"], dict):
            # If its a single nested model. Get its dependencies and add them
            dependencies.extend(get_model_dependencies(model["extends"]))
        elif isinstance(model["extends"], list):
            # If its a list, could have DTMIs or nested models
            for item in model["extends"]:
                if isinstance(item, str):
                    # If there are strings in the list, that's a DTMI reference, so add it
                    dependencies.append(item)
                elif isinstance(item, dict):
                    # This is a nested model. Now go get its dependencies and add them
                    dependencies.extend(get_model_dependencies(item))

    # Remove duplicate dependencies
    dependencies = list(set(dependencies))
    return dependencies


class ModelProvider(DigitalTwinsProvider):
    def __init__(self, cmd, name, rg=None):
        super(ModelProvider, self).__init__(
            cmd=cmd, name=name, rg=rg,
        )
        self.model_sdk = self.get_sdk().digital_twin_models

    def add(self, models=None, from_directory=None):
        if not any([models, from_directory]):
            raise CLIError("Provide either --models or --from-directory.")

        # If both arguments are provided. --models wins.
        payload = []
        if models:
            models_result = process_json_arg(content=models, argument_name="models")

            if isinstance(models_result, list):
                payload.extend(models_result)
            elif isinstance(models_result, dict):
                payload.append(models_result)

        elif from_directory:
            payload = self._process_directory(from_directory=from_directory)

        logger.info("Models payload %s", json.dumps(payload))

        # TODO: Not standard - have to revisit.
        try:
            response = self.model_sdk.add(payload)
        except ErrorResponseException as e:
            raise CLIError(unpack_msrest_error(e))

        if response.status_code not in [200, 201]:
            error_text = response.text
            if response.status_code == 403 and not error_text:
                error_text = "Current principal access is forbidden. Please validate rbac role assignments."
            else:
                try:
                    error_text = response.json()
                except Exception:
                    pass
            raise CLIError(error_text)

        return response.json()

    def _process_directory(self, from_directory):
        logger.debug(
            "Documents contained in directory: {}, processing...".format(from_directory)
        )
        payload = []
        for entry in scantree(from_directory):
            if all(
                [not entry.name.endswith(".json"), not entry.name.endswith(".dtdl")]
            ):
                logger.debug(
                    "Skipping {} - model file must end with .json or .dtdl".format(
                        entry.path
                    )
                )
                continue
            entry_json = process_json_arg(content=entry.path, argument_name=entry.name)
            payload.append(entry_json)

        return payload

    def get(self, id, get_definition=False):
        try:
            return self.model_sdk.get_by_id(
                id=id, include_model_definition=get_definition, raw=True
            ).response.json()
        except ErrorResponseException as e:
            raise CLIError(unpack_msrest_error(e))

    def list(
        self, get_definition=False, dependencies_for=None, top=None
    ):  # top is guarded for int() in arg def
        from azext_iot.sdk.digitaltwins.dataplane.models import DigitalTwinModelsListOptions

        list_options = DigitalTwinModelsListOptions(max_item_count=top)

        return self.model_sdk.list(
            dependencies_for=dependencies_for,
            include_model_definition=get_definition,
            digital_twin_models_list_options=list_options,
        )

    def update(self, id, decommission: bool):
        patched_model = [
            {"op": "replace", "path": "/decommissioned", "value": decommission}
        ]

        # Does not return model object upon updating
        try:
            self.model_sdk.update(id=id, update_model=patched_model)
        except ErrorResponseException as e:
            raise CLIError(unpack_msrest_error(e))

        return self.get(id=id)

    def delete(self, id: str):
        try:
            self.model_sdk.delete(id=id)
        except ErrorResponseException as e:
            raise CLIError(unpack_msrest_error(e))

    def delete_all(self):
        # Get all models
        incoming_pager = self.list(get_definition=True)
        incoming_result = []
        try:
            while True:
                incoming_result.extend(incoming_pager.advance_page())
        except StopIteration:
            pass
        except ErrorResponseException as e:
            raise CLIError(unpack_msrest_error(e))

        # Build dict of model_id : set of parent_ids
        parsed_models = {model.id: set() for model in incoming_result}
        for model in incoming_result:
            # Parse dependents, add current model as parent of dependents
            dependencies = get_model_dependencies(model.model)
            for d_id in dependencies:
                parsed_models[d_id].add(model.id)

        def delete_parents(model_id, model_dict):
            # Check if current model has been deleted already
            if model_id not in model_dict:
                return

            # Delete parents first
            for parent_id in model_dict[model_id]:
                if parent_id in model_dict:
                    delete_parents(parent_id, model_dict)

            # Delete current model and remove references
            del model_dict[model_id]
            try:
                self.delete(model_id)
            except CLIError as e:
                logger.warn(f"Could not delete model {model_id}; error is {e}")

        while len(parsed_models) > 0:
            model_id = next(iter(parsed_models))
            delete_parents(model_id, parsed_models)
