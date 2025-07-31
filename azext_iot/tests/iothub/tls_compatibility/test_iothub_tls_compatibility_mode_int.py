# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pytest
from azext_iot.common.embedded_cli import EmbeddedCLI

cli = EmbeddedCLI()


@pytest.mark.hub_infrastructure(location="eastus2euap")
def test_tls_compatibility_mode(provisioned_only_iot_hubs_module):
    hub_name = provisioned_only_iot_hubs_module[0]["name"]
    rg = provisioned_only_iot_hubs_module[0]["rg"]

    initial_state = cli.invoke(
        f"iot hub tls-compat show -n {hub_name} -g {rg}"
    ).as_json()["tlsCompatibilityMode"]

    # transition 1
    updated_state = cli.invoke(
        f"iot hub tls-compat set -n {hub_name} -g {rg} --enable {not initial_state} --yes"
    ).as_json()["tlsCompatibilityMode"]
    assert updated_state is not initial_state

    # verify the change
    show_state = cli.invoke(
        f"iot hub tls-compat show -n {hub_name} -g {rg}"
    ).as_json()["tlsCompatibilityMode"]
    assert show_state is updated_state

    # transition 2
    updated_state = cli.invoke(
        f"iot hub tls-compat set -n {hub_name} -g {rg} --enable {initial_state} --yes"
    ).as_json()["tlsCompatibilityMode"]
    assert updated_state is initial_state

    # verify the change
    show_state = cli.invoke(
        f"iot hub tls-compat show -n {hub_name} -g {rg}"
    ).as_json()["tlsCompatibilityMode"]
    assert show_state is initial_state
