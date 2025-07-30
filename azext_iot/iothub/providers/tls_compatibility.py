# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import Optional, Dict
from azure.cli.core.azclierror import ManualInterrupt
from azext_iot.common.embedded_cli import EmbeddedCLI
from azext_iot.iothub.providers.base import IoTHubProvider
from azext_iot.iothub.common import HUB_PROVIDER
from knack.log import get_logger
from knack.prompting import prompt_y_n

logger = get_logger(__name__)

MIN_TLS_API = "2025-05-01-preview"


class TLSCompatabilityProvider(IoTHubProvider):
    def __init__(self, cmd, hub_name: str, rg: Optional[str] = None):
        super(TLSCompatabilityProvider, self).__init__(cmd, hub_name, rg, dataplane=False)
        self.cli = EmbeddedCLI(cli_ctx=self.cmd.cli_ctx)

        if not self.rg:
            # note: may be better to use target (use dataplane=True)
            self.rg = self.hub_resource.additional_properties["resourcegroup"]

    def get_tls_compatibility_mode(self):
        return {"tlsCompatibilityMode": self._get_target_properties().get("tlsCompatibilityMode", False)}

    def set_tls_compatibility_mode(
        self, tls_compatibility_mode: bool, confirm_yes: bool = False
    ) -> Dict[str, str]:
        properties = self._get_target_properties()

        # no need to update if the version is already set
        if properties.get("tlsCompatibilityMode") is tls_compatibility_mode:
            logger.warning(
                f"TLS compatibility mode is already set to `{tls_compatibility_mode}` for IoT Hub {self.hub_name}."
            )
            return {"tlsCompatibilityMode": tls_compatibility_mode}

        # Confirm the change if not already confirmed
        if not confirm_yes and not prompt_y_n(
            f"Setting TLS compatibility mode to {tls_compatibility_mode}. Continue? ", default="n"
        ):
            raise ManualInterrupt(
                "Aborting TLS compatibility mode update."
            )

        # Build the command
        command = (
            f"resource update -n {self.hub_name} -g {self.rg} --api-version {MIN_TLS_API} "
            f"--resource-type {HUB_PROVIDER} "
        )
        if "tlsCompatibilityMode" not in properties:
            # is this or the json dumps + replace format better?
            command += f"--set properties=\"{{\\\"tlsCompatibilityMode\\\": {tls_compatibility_mode}}}\""
        else:
            command += f"--set properties.tlsCompatibilityMode={tls_compatibility_mode}"

        # could use a spinner
        result = self.cli.invoke(command=command, capture_stderr=True).as_json()
        return {"tlsCompatibilityMode": result["properties"]["tlsCompatibilityMode"]}

    def _get_target_properties(self) -> Optional[Dict[str, str]]:
        result = self.cli.invoke(
            f"resource show -n {self.hub_name} -g {self.rg} --api-version {MIN_TLS_API} "
            f"--resource-type {HUB_PROVIDER}",
            capture_stderr=True
        )
        return result.as_json()["properties"]
