# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.digitaltwins.providers.resource import ResourceProvider
from knack.log import get_logger
from typing import TypeVar

logger = get_logger(__name__)
AzCliCommand = TypeVar('AzCliCommand')


def assign_role(
    cmd : AzCliCommand,
    name : str,
    role_type : str,
    assignee : str,
    resource_group_name : str = None
):
    rp = ResourceProvider(cmd)
    return rp.assign_role(
        name=name,
        role_type=role_type,
        assignee=assignee,
        resource_group_name=resource_group_name,
    )


def remove_role(
    cmd : AzCliCommand,
    name : str,
    assignee : str = None,
    role_type : str = None,
    resource_group_name : str = None
) -> None:
    rp = ResourceProvider(cmd)
    return rp.remove_role(
        name=name,
        assignee=assignee,
        role_type=role_type,
        resource_group_name=resource_group_name,
    )


def list_assignments(
    cmd : AzCliCommand,
    name : str,
    include_inherited : bool = False,
    role_type : str = None,
    resource_group_name : str = None
):
    rp = ResourceProvider(cmd)
    return rp.get_role_assignments(
        name=name,
        include_inherited=include_inherited,
        resource_group_name=resource_group_name,
        role_type=role_type,
    )
