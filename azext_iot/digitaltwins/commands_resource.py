# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List
from azext_iot.common.shared import (
    AzCliCommand,
    AzureOperationPoller,
    DigitalTwinsDescription,
    DigitalTwinsDescriptionPaged,
    DigitalTwinsEndpointResource,
    DigitalTwinsEndpointResourcePaged
)
from azext_iot.digitaltwins.providers.resource import ResourceProvider
from azext_iot.digitaltwins.common import (
    ADTEndpointType,
    ADTEndpointAuthType,
    ADTPublicNetworkAccessType,
)
from knack.log import get_logger

logger = get_logger(__name__)


def create_instance(
    cmd : AzCliCommand,
    name : str,
    resource_group_name : str,
    location : str = None,
    tags : List[str] = None,
    assign_identity : str = None,
    scopes : List[str] = None,
    role_type : str = "Contributor",
    public_network_access : str = ADTPublicNetworkAccessType.enabled.value,
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.create(
        name=name,
        resource_group_name=resource_group_name,
        location=location,
        tags=tags,
        assign_identity=assign_identity,
        scopes=scopes,
        role_type=role_type,
        public_network_access=public_network_access,
    )


def list_instances(cmd : AzCliCommand, resource_group_name : str = None) -> DigitalTwinsDescriptionPaged:
    rp = ResourceProvider(cmd)

    if not resource_group_name:
        return rp.list()
    return rp.list_by_resouce_group(resource_group_name)


def show_instance(cmd : AzCliCommand, name : str, resource_group_name : str = None) -> DigitalTwinsDescription:
    rp = ResourceProvider(cmd)
    return rp.find_instance(name=name, resource_group_name=resource_group_name)


def delete_instance(cmd : AzCliCommand, name : str, resource_group_name : str = None) -> None:
    rp = ResourceProvider(cmd)
    return rp.delete(name=name, resource_group_name=resource_group_name)


def list_endpoints(
    cmd : AzCliCommand, name : str, resource_group_name : str = None
) -> DigitalTwinsEndpointResourcePaged:
    rp = ResourceProvider(cmd)
    return rp.list_endpoints(name=name, resource_group_name=resource_group_name)


def show_endpoint(
    cmd : AzCliCommand, name : str, endpoint_name : str, resource_group_name : str = None
) -> DigitalTwinsEndpointResource:
    rp = ResourceProvider(cmd)
    return rp.get_endpoint(
        name=name, endpoint_name=endpoint_name, resource_group_name=resource_group_name
    )


def delete_endpoint(
    cmd, name : str, endpoint_name : str, resource_group_name : str = None
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.delete_endpoint(
        name=name, endpoint_name=endpoint_name, resource_group_name=resource_group_name
    )


def add_endpoint_eventgrid(
    cmd : AzCliCommand,
    name : str,
    endpoint_name : str,
    eventgrid_topic_name : str,
    eventgrid_resource_group : str,
    resource_group_name : str = None,
    endpoint_subscription : str = None,
    dead_letter_uri : str = None,
    dead_letter_secret : str = None,
    auth_type : str = ADTEndpointAuthType.keybased.value,
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.add_endpoint(
        name=name,
        resource_group_name=resource_group_name,
        endpoint_name=endpoint_name,
        endpoint_resource_type=ADTEndpointType.eventgridtopic.value,
        endpoint_resource_name=eventgrid_topic_name,
        endpoint_resource_group=eventgrid_resource_group,
        endpoint_subscription=endpoint_subscription,
        dead_letter_uri=dead_letter_uri,
        dead_letter_secret=dead_letter_secret,
        auth_type=auth_type,
    )


def add_endpoint_servicebus(
    cmd : AzCliCommand,
    name : str,
    endpoint_name : str,
    servicebus_topic_name : str,
    servicebus_resource_group : str,
    servicebus_namespace : str,
    servicebus_policy : str = None,
    resource_group_name : str = None,
    endpoint_subscription : str = None,
    dead_letter_uri : str = None,
    dead_letter_secret : str = None,
    auth_type : str = ADTEndpointAuthType.keybased.value,
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.add_endpoint(
        name=name,
        resource_group_name=resource_group_name,
        endpoint_name=endpoint_name,
        endpoint_resource_type=ADTEndpointType.servicebus.value,
        endpoint_resource_name=servicebus_topic_name,
        endpoint_resource_group=servicebus_resource_group,
        endpoint_resource_namespace=servicebus_namespace,
        endpoint_resource_policy=servicebus_policy,
        endpoint_subscription=endpoint_subscription,
        dead_letter_uri=dead_letter_uri,
        dead_letter_secret=dead_letter_secret,
        auth_type=auth_type,
    )


def add_endpoint_eventhub(
    cmd : AzCliCommand,
    name : str,
    endpoint_name : str,
    eventhub_name : str,
    eventhub_resource_group : str,
    eventhub_namespace : str,
    eventhub_policy : str = None,
    resource_group_name : str = None,
    endpoint_subscription : str = None,
    dead_letter_uri : str = None,
    dead_letter_secret : str = None,
    auth_type : str = ADTEndpointAuthType.keybased.value,
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.add_endpoint(
        name=name,
        resource_group_name=resource_group_name,
        endpoint_name=endpoint_name,
        endpoint_resource_type=ADTEndpointType.eventhub.value,
        endpoint_resource_name=eventhub_name,
        endpoint_resource_group=eventhub_resource_group,
        endpoint_resource_namespace=eventhub_namespace,
        endpoint_resource_policy=eventhub_policy,
        endpoint_subscription=endpoint_subscription,
        dead_letter_uri=dead_letter_uri,
        dead_letter_secret=dead_letter_secret,
        auth_type=auth_type,
    )


def show_private_link(
    cmd : AzCliCommand, name : str, link_name : str, resource_group_name : str = None
) -> dict:
    rp = ResourceProvider(cmd)
    return rp.get_private_link(
        name=name, resource_group_name=resource_group_name, link_name=link_name
    )


def list_private_links(
    cmd : AzCliCommand, name, resource_group_name : str = None
) -> List[dict]:
    rp = ResourceProvider(cmd)
    return rp.list_private_links(name=name, resource_group_name=resource_group_name)


def set_private_endpoint_conn(
    cmd : AzCliCommand,
    name : str,
    conn_name : str,
    status : str,
    description : str = None,
    group_ids : str = None,
    actions_required : str = None,
    resource_group_name : str = None,
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.set_private_endpoint_conn(
        name=name,
        resource_group_name=resource_group_name,
        conn_name=conn_name,
        status=status,
        description=description,
        group_ids=group_ids,
        actions_required=actions_required,
    )


def show_private_endpoint_conn(
    cmd : AzCliCommand, name : str, conn_name : str, resource_group_name : str = None
) -> DigitalTwinsEndpointResource:
    rp = ResourceProvider(cmd)
    return rp.get_private_endpoint_conn(
        name=name, resource_group_name=resource_group_name, conn_name=conn_name
    )


def list_private_endpoint_conns(
    cmd : AzCliCommand, name : str, resource_group_name : str = None
) -> List[dict]:
    rp = ResourceProvider(cmd)
    return rp.list_private_endpoint_conns(
        name=name, resource_group_name=resource_group_name
    )


def delete_private_endpoint_conn(
    cmd : AzCliCommand, name : str, conn_name : str, resource_group_name : str = None
) -> AzureOperationPoller:
    rp = ResourceProvider(cmd)
    return rp.delete_private_endpoint_conn(
        name=name, resource_group_name=resource_group_name, conn_name=conn_name
    )
