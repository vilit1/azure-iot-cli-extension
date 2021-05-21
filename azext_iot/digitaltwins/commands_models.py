# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.digitaltwins.providers.model import ModelProvider
from knack.log import get_logger
from typing import TypeVar

logger = get_logger(__name__)
AzCliCommand = TypeVar('AzCliCommand')


def add_models(
    cmd : AzCliCommand,
    name_or_hostname : str,
    models : str = None,
    from_directory : str = None,
    resource_group_name : str = None
):
    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    logger.debug("Received models input: %s", models)
    return model_provider.add(models=models, from_directory=from_directory)


def show_model(
    cmd : AzCliCommand,
    name_or_hostname : str,
    model_id : str,
    definition : bool = False,
    resource_group_name : str = None
):
    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return model_provider.get(id=model_id, get_definition=definition)


def list_models(
    cmd : AzCliCommand,
    name_or_hostname : str,
    definition : str = False,
    dependencies_for : str = None,
    resource_group_name : str = None
):
    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return model_provider.list(
        get_definition=definition, dependencies_for=dependencies_for
    )


def update_model(
    cmd : AzCliCommand,
    name_or_hostname : str,
    model_id : str,
    decommission : str = None,
    resource_group_name : str = None
):
    if decommission is None:
        logger.info("No update arguments provided. Nothing to update.")
        return

    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return model_provider.update(id=model_id, decommission=decommission,)


def delete_model(
    cmd : AzCliCommand,
    name_or_hostname : str,
    model_id : str,
    resource_group_name : str = None
):
    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return model_provider.delete(id=model_id)


def delete_all_models(
    cmd : AzCliCommand,
    name_or_hostname : str,
    resource_group_name : str = None
):
    model_provider = ModelProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return model_provider.delete_all()
