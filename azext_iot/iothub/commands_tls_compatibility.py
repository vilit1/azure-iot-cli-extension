# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import Optional, Dict
from knack.log import get_logger
from azext_iot.iothub.providers.tls_compatibility import TLSCompatabilityProvider

logger = get_logger(__name__)


def tls_compatibility_mode_show(
    cmd, hub_name: str, resource_group_name: Optional[str] = None
) -> Dict[str, str]:
    provider = TLSCompatabilityProvider(cmd, hub_name, resource_group_name)
    return provider.get_tls_compatibility_mode()


def tls_compatibility_mode_set(
    cmd,
    hub_name: str,
    tls_compatibility_mode: bool,
    resource_group_name: Optional[str] = None,
    confirm_yes: bool = False,
) -> Dict[str, str]:
    provider = TLSCompatabilityProvider(cmd, hub_name, resource_group_name)
    return provider.set_tls_compatibility_mode(
        tls_compatibility_mode=tls_compatibility_mode, confirm_yes=confirm_yes
    )
