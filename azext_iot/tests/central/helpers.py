# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import time
from typing import Optional, Tuple
from knack.log import get_logger

from azure.cli.core.azclierror import CLIInternalError
from azext_iot.common import utility
from azext_iot.common.embedded_cli import EmbeddedCLI
from azext_iot.tests.generators import generate_names
from azext_iot.tests.central import (
    DEVICE_TEMPLATE_PATH,
    EDGE_TEMPLATE_PATH_PREVIEW,
    APP_RG,
    TOKEN,
    DNS_SUFFIX,
    settings
)


logger = get_logger(__name__)
cli = EmbeddedCLI()
TEMPLATE_ID_KEY = "@id"


def cmd(command, api_version=None, include_opt_args=True, expect_failure=False) -> EmbeddedCLI:
    if include_opt_args:
        if api_version:
            command += f" --api-version {api_version}"
        if TOKEN:
            command += f" --token \"{TOKEN}\""
        if DNS_SUFFIX:
            command += f" --central-dns-suffix \"{DNS_SUFFIX}\""

    result = cli.invoke(command=command)
    if expect_failure:
        assert not result.success(), f"Command `{command}` did not fail as expected."
    return result


def create_app(tracked_resources) -> Tuple[str, str]:
    """
    Create an Iot Central Application if a name is not given in the pytest configuration.
    """
    app_id = (
        settings.env.azext_iot_central_app_id or generate_names(prefix="test-app-", max_length=20)
    )

    # Create Central App if it does not exist. Note that app_primary_key will be nullified since
    # there is no current way to get the app_primary_key and not all tests can be executed.
    target_app = None
    if not settings.env.azext_iot_central_app_id:
        if not APP_RG:
            raise CLIInternalError("Tests need either app name or resource group.")
        if DNS_SUFFIX or TOKEN:
            raise CLIInternalError(
                "Create an IoT Central App with a valid API token and populate the azext_iot_central_app_id, "
                "azext_iot_central_dns_suffix, and azext_iot_central_token variables for testing in non-prod environments."
            )

        app_list = cmd(
            'iot central app list -g "{}"'.format(APP_RG)
        ).as_json()

        # Check if the generated name is already used
        for app in app_list:
            if app["name"] == app_id:
                target_app = app
                break

        # Create the min version app and assign the correct roles
        if not target_app:
            target_app = cmd(
                "iot central app create -n {} -g {} -s {} -l {}".format(
                    app_id, APP_RG, app_id, "westus"
                ),
                include_opt_args=False,
            ).as_json()
            tracked_resources.append(target_app["id"])

    # Get Central App RG if possible
    if DNS_SUFFIX or TOKEN:
        if not APP_RG:
            logger.info(
                "Tests will not have the resource group populated. If a storage account is not"
                " specified, it will not be created and the respective tests will not run."
            )
        return app_id, APP_RG
    elif target_app:
        return app_id, target_app['resourceGroup']
    else:
        app_list = cmd('iot central app list').as_json()
        for app in app_list:
            if app["applicationId"] == app_id or app["name"] == app_id:
                return app_id, app['resourceGroup']
        # Throw if no resource group found
        raise CLIInternalError(
            f"Please provide API token (azext_iot_central_token) in the setting for application {app_id}"
        )


def create_device_template(app_id: str, api_version: Optional[str] = None, edge: bool = False) -> Tuple[str, str]:
    if edge:
        template_path = EDGE_TEMPLATE_PATH_PREVIEW
    else:
        template_path = DEVICE_TEMPLATE_PATH

    template = utility.process_json_arg(
        template_path,
        argument_name="template_path",
    )

    template_name = template["displayName"]
    template_id = template_name + "id;1"

    if edge:
        # check if template already exists as a create call does not work for edge templates
        # since deployment manifest cannot be changed
        try:
            command = "iot central device-template show --app-id {} --device-template-id {}".format(
                app_id, template_id
            )
            result = cmd(command, api_version=api_version).as_json()

            if result and result.get(TEMPLATE_ID_KEY) == template_id:
                return (template_id, template_name)
        except Exception:
            pass

    command = "iot central device-template create --app-id {} --device-template-id {} -k '{}'".format(
        app_id, template_id, template_path
    )

    result = cmd(command, api_version).as_json()
    assert result["displayName"] == template_name
    assert result[TEMPLATE_ID_KEY] == template_id

    return (template_id, template_name)


def create_device(app_id: str, api_version: Optional[str] = None, **kwargs) -> Tuple[str, str]:
    """
    kwargs:
        template: template_id (str)
        simulated: if the device is to be simulated (bool)
    """
    device_id, device_name = generate_names(prefix="aztest", count=2, max_length=24)

    command = "iot central device create --app-id {} -d {} --device-name {}".format(
        app_id, device_id, device_name
    )

    checks = [
        ("displayName", device_name),
        ("id", device_id),
        ("enabled", True)
    ]

    template = kwargs.get("template")
    if template:
        command = command + " --template {}".format(template)
        checks.append(("template", template))

    simulated = bool(kwargs.get("simulated"))
    if simulated:
        command = command + " --simulated"

    checks.append(("simulated", simulated))

    result = cmd(command, api_version=api_version).as_json()
    for key, expected in checks:
        assert result[key] == expected

    return (device_id, device_name)


def get_credentials(app_id: str, device_id: str, api_version: Optional[str] = None):
    return cmd(
        "iot central device show-credentials --app-id {} -d {}".format(
            app_id, device_id
        ),
        api_version=api_version,
    ).as_json()


def get_validate_messages_output(
    app_id: str, device_id: str, enqueued_time: str, duration: int = 60, max_messages: int = 1, asserts=None
):
    # TODO: prob better way of handling this?
    from azext_iot.tests import command_execute_assert
    if not asserts:
        asserts = []

    print(
        "iot central diagnostics validate-messages"
        " --app-id {} "
        " -d {} "
        " --et {} "
        " --duration {} "
        " --mm {} -y --style json".format(
            app_id, device_id, enqueued_time, duration, max_messages
        )
    )
    import pdb; pdb.set_trace()
    output = command_execute_assert(
        cli,
        "iot central diagnostics validate-messages"
        " --app-id {} "
        " -d {} "
        " --et {} "
        " --duration {} "
        " --mm {} -y --style json".format(
            app_id, device_id, enqueued_time, duration, max_messages
        ),
        asserts,
    )
    print(output)

    if not output:
        output = ""

    return output


def delete_device(app_id: str, device_id: str, api_version: Optional[str] = None) -> None:
    command = "iot central device delete --app-id {} -d {} ".format(
        app_id, device_id
    )

    result = cmd(command=command, api_version=api_version).as_json()
    assert result["result"] == "success"


def delete_device_template(app_id: str, template_id: str, api_version: Optional[str] = None):
    attempts = range(0, 10)

    # retry logic to delete the template
    error = None
    for _ in attempts:
        try:
            error = None
            result = cmd(
                command="iot central device-template delete --app-id {} --device-template-id {}".format(
                    app_id, template_id
                ),
                api_version=api_version,
            )
            assert result.as_json()["result"] == "success"
            return
        except Exception as e:
            error = e
            # delete associated devices if any.
            devices = cmd(
                command="iot central device list --app-id {}".format(app_id),
                api_version=api_version,
            ).as_json()

            if devices:
                for device in devices:
                    device_template = device["template"]
                    if device_template == template_id:
                        # delete attached children devices if any
                        children = []

                        list_children_command = "iot central device edge children list --app-id {} -d {}".format(
                            app_id, device["id"]
                        )
                        try:
                            children = cmd(
                                list_children_command, api_version=api_version
                            ).as_json()
                        except Exception:
                            pass

                        for child in children:
                            try:
                                cmd(
                                    "iot central device delete --app-id {} --device-id {}".format(
                                        app_id, child["id"]
                                    ),
                                    api_version=api_version,
                                )
                            except Exception:
                                pass

                        time.sleep(10)
                        try:
                            cmd(
                                "iot central device delete --app-id {} --device-id {}".format(
                                    app_id, device["id"]
                                ),
                                api_version=api_version,
                            )
                        except Exception:
                            pass
            time.sleep(10)

    raise CLIInternalError(
        f"Device template {template_id} cannot be deleted."
        + (f" Error: {error}" if error is not None else "")
    )
