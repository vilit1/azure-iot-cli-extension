# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import json
import pytest
from knack.log import get_logger

from azure.iot.device import Message
from azext_iot.common import utility
from azext_iot.tests import helpers
import azext_iot.tests.central.helpers as central_helpers


logger = get_logger(__name__)


def test_alt_central_validate_messages_success():
    app_id = None
    (template_id, _) = central_helpers.create_device_template(app_id)
    (device_id, _) = central_helpers.create_device(
        app_id=app_id,
        template=template_id
    )
    credentials = central_helpers.get_credentials(
        app_id=app_id,
        device_id=device_id
    )

    device_client = helpers.dps_connect_device(device_id, credentials)

    enqueued_time = utility.calculate_millisec_since_unix_epoch_utc() - 10000

    payload = {"Bool": True}
    msg = Message(
        data=json.dumps(payload),
        content_encoding="utf-8",
        content_type="application/json",
    )
    device_client.send_message(msg)

    # Validate the messages
    output = central_helpers.get_validate_messages_output(device_id, enqueued_time)

    central_helpers.delete_device(device_id=device_id)

    central_helpers.delete_device_template(
        template_id=template_id
    )

    assert output
    assert "Successfully parsed 1 message(s)" in output
    assert "No errors detected" in output