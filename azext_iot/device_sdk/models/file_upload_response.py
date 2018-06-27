# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FileUploadResponse(Model):
    """FileUploadResponse.

    :param correlation_id:
    :type correlation_id: str
    :param host_name:
    :type host_name: str
    :param container_name:
    :type container_name: str
    :param blob_name:
    :type blob_name: str
    :param sas_token:
    :type sas_token: str
    """

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'blob_name': {'key': 'blobName', 'type': 'str'},
        'sas_token': {'key': 'sasToken', 'type': 'str'},
    }

    def __init__(self, correlation_id=None, host_name=None, container_name=None, blob_name=None, sas_token=None):
        super(FileUploadResponse, self).__init__()
        self.correlation_id = correlation_id
        self.host_name = host_name
        self.container_name = container_name
        self.blob_name = blob_name
        self.sas_token = sas_token
