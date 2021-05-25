# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.common.shared import AzCliCommand, EventRoute, EventRoutePaged
from azext_iot.digitaltwins.providers.route import RouteProvider
from knack.log import get_logger

logger = get_logger(__name__)


def create_route(
    cmd : AzCliCommand,
    name_or_hostname : str,
    route_name : str,
    endpoint_name : str,
    filter : str = "true",
    resource_group_name : str = None
) -> None:
    route_provider = RouteProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return route_provider.create(
        route_name=route_name, endpoint_name=endpoint_name, filter=filter
    )


def show_route(
    cmd : AzCliCommand, name_or_hostname : str, route_name : str, resource_group_name : str = None
) -> EventRoute:
    route_provider = RouteProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return route_provider.get(route_name=route_name)


def list_routes(
    cmd : AzCliCommand, name_or_hostname : str, resource_group_name : str = None
) -> EventRoutePaged:
    route_provider = RouteProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return route_provider.list()


def delete_route(
    cmd : AzCliCommand, name_or_hostname : str, route_name : str, resource_group_name : str = None
) -> None:
    route_provider = RouteProvider(cmd=cmd, name=name_or_hostname, rg=resource_group_name)
    return route_provider.delete(route_name=route_name)
