# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.common.shared import AzCliCommand
from azext_iot.digitaltwins.providers.twin import TwinProvider
from knack.log import get_logger

logger = get_logger(__name__)


def query_twins(
    cmd : AzCliCommand,
    name_or_hostname : str,
    query_command : str,
    show_cost : bool = False,
    resource_group_name : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.invoke_query(query=query_command, show_cost=show_cost)


def create_twin(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    model_id : str,
    if_none_match : bool = False,
    properties : str = None,
    resource_group_name : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.create(
        twin_id=twin_id, model_id=model_id, if_none_match=if_none_match, properties=properties
    )


def show_twin(
    cmd : AzCliCommand, name_or_hostname : str, twin_id : str, resource_group_name : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.get(twin_id)


def update_twin(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    json_patch : str,
    resource_group_name : str = None,
    etag : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.update(twin_id=twin_id, json_patch=json_patch, etag=etag)


def delete_twin(
    cmd : AzCliCommand, name_or_hostname : str, twin_id : str, resource_group_name : str = None, etag : str = None
) -> None:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.delete(twin_id=twin_id, etag=etag)


def delete_all_twin(
    cmd : AzCliCommand, name_or_hostname : str, resource_group_name : str = None
) -> None:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.delete_all()


def create_relationship(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    target_twin_id : str,
    relationship_id : str,
    relationship : str,
    if_none_match=False,
    properties : str = None,
    resource_group_name : str = None,
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.add_relationship(
        twin_id=twin_id,
        target_twin_id=target_twin_id,
        relationship_id=relationship_id,
        relationship=relationship,
        if_none_match=if_none_match,
        properties=properties,
    )


def show_relationship(
    cmd : AzCliCommand, name_or_hostname : str, twin_id : str, relationship_id : str, resource_group_name : str = None,
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.get_relationship(
        twin_id=twin_id, relationship_id=relationship_id
    )


def update_relationship(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    relationship_id : str,
    json_patch : str,
    resource_group_name : str = None,
    etag : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.update_relationship(
        twin_id=twin_id, relationship_id=relationship_id, json_patch=json_patch, etag=etag
    )


def list_relationships(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    incoming_relationships=False,
    relationship : str = None,
    resource_group_name : str = None,
):
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.list_relationships(
        twin_id=twin_id,
        incoming_relationships=incoming_relationships,
        relationship=relationship,
    )


def delete_relationship(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    relationship_id : str,
    resource_group_name : str = None,
    etag : str = None
) -> None:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.delete_relationship(
        twin_id=twin_id, relationship_id=relationship_id, etag=etag
    )


def delete_all_relationship(
    cmd : AzCliCommand, name_or_hostname : str, twin_id : str = None, resource_group_name : str = None
) -> None:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    if twin_id:
        return twin_provider.delete_all_relationship(twin_id=twin_id)
    return twin_provider.delete_all(only_relationships=True)


def send_telemetry(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    dt_id : str = None,
    component_path : str = None,
    telemetry : str = None,
    resource_group_name : str = None,
) -> None:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.send_telemetry(
        twin_id=twin_id, dt_id=dt_id, component_path=component_path, telemetry=telemetry
    )


def show_component(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    component_path : str,
    resource_group_name : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.get_component(twin_id=twin_id, component_path=component_path)


def update_component(
    cmd : AzCliCommand,
    name_or_hostname : str,
    twin_id : str,
    component_path : str,
    json_patch : str,
    resource_group_name : str = None,
    etag : str = None
) -> dict:
    twin_provider = TwinProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return twin_provider.update_component(
        twin_id=twin_id, component_path=component_path, json_patch=json_patch, etag=etag
    )
