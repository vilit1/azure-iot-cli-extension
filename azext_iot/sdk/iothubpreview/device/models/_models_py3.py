# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.4.5, generator: @autorest/python@5.8.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

import msrest.serialization

from ._iot_hub_gateway_device_apis_enums import *


class AuthenticationMechanism(msrest.serialization.Model):
    """AuthenticationMechanism.

    :param symmetric_key: The primary and secondary keys used for SAS based authentication.
    :type symmetric_key: ~iot_hub_gateway_device_apis.models.SymmetricKey
    :param x509_thumbprint: The primary and secondary x509 thumbprints used for x509 based
     authentication.
    :type x509_thumbprint: ~iot_hub_gateway_device_apis.models.X509Thumbprint
    :param type: The type of authentication used to connect to the service. Possible values
     include: "sas", "selfSigned", "certificateAuthority", "none".
    :type type: str or ~iot_hub_gateway_device_apis.models.AuthenticationMechanismType
    """

    _attribute_map = {
        'symmetric_key': {'key': 'symmetricKey', 'type': 'SymmetricKey'},
        'x509_thumbprint': {'key': 'x509Thumbprint', 'type': 'X509Thumbprint'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        symmetric_key: Optional["SymmetricKey"] = None,
        x509_thumbprint: Optional["X509Thumbprint"] = None,
        type: Optional[Union[str, "AuthenticationMechanismType"]] = None,
        **kwargs
    ):
        super(AuthenticationMechanism, self).__init__(**kwargs)
        self.symmetric_key = symmetric_key
        self.x509_thumbprint = x509_thumbprint
        self.type = type


class Device(msrest.serialization.Model):
    """Device.

    :param device_id: The unique identifier of the device.
    :type device_id: str
    :param generation_id: The IoT Hub-generated, case-sensitive string up to 128 characters long.
     This value is used to distinguish devices with the same deviceId, when they have been deleted
     and re-created.
    :type generation_id: str
    :param etag: The string representing a weak ETag for the device identity, as per RFC7232.
    :type etag: str
    :param connection_state: The state of the device. Possible values include: "Disconnected",
     "Connected".
    :type connection_state: str or ~iot_hub_gateway_device_apis.models.DeviceConnectionState
    :param status: The status of the device. If the status disabled, a device cannot connect to the
     service. Possible values include: "enabled", "disabled".
    :type status: str or ~iot_hub_gateway_device_apis.models.DeviceStatus
    :param status_reason: The 128 character-long string that stores the reason for the device
     identity status. All UTF-8 characters are allowed.
    :type status_reason: str
    :param connection_state_updated_time: The date and time the connection state was last updated.
    :type connection_state_updated_time: ~datetime.datetime
    :param status_updated_time: The date and time when the status field was last updated.
    :type status_updated_time: ~datetime.datetime
    :param last_activity_time: The date and last time the device last connected, received, or sent
     a message.
    :type last_activity_time: ~datetime.datetime
    :param cloud_to_device_message_count: The number of cloud-to-device messages currently queued
     to be sent to the device.
    :type cloud_to_device_message_count: int
    :param authentication: The authentication mechanism used by the device.
    :type authentication: ~iot_hub_gateway_device_apis.models.AuthenticationMechanism
    :param capabilities: The set of capabilities of the device. For example, if this device is an
     edge device or not.
    :type capabilities: ~iot_hub_gateway_device_apis.models.DeviceCapabilities
    :param device_scope: The scope of the device. Auto generated and immutable for edge devices and
     modifiable in leaf devices to create child/parent relationship.
    :type device_scope: str
    :param parent_scopes: The scopes of the upper level edge devices if applicable. Only available
     for edge devices.
    :type parent_scopes: list[str]
    """

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'generation_id': {'key': 'generationId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'connection_state_updated_time': {'key': 'connectionStateUpdatedTime', 'type': 'iso-8601'},
        'status_updated_time': {'key': 'statusUpdatedTime', 'type': 'iso-8601'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'int'},
        'authentication': {'key': 'authentication', 'type': 'AuthenticationMechanism'},
        'capabilities': {'key': 'capabilities', 'type': 'DeviceCapabilities'},
        'device_scope': {'key': 'deviceScope', 'type': 'str'},
        'parent_scopes': {'key': 'parentScopes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        device_id: Optional[str] = None,
        generation_id: Optional[str] = None,
        etag: Optional[str] = None,
        connection_state: Optional[Union[str, "DeviceConnectionState"]] = None,
        status: Optional[Union[str, "DeviceStatus"]] = None,
        status_reason: Optional[str] = None,
        connection_state_updated_time: Optional[datetime.datetime] = None,
        status_updated_time: Optional[datetime.datetime] = None,
        last_activity_time: Optional[datetime.datetime] = None,
        cloud_to_device_message_count: Optional[int] = None,
        authentication: Optional["AuthenticationMechanism"] = None,
        capabilities: Optional["DeviceCapabilities"] = None,
        device_scope: Optional[str] = None,
        parent_scopes: Optional[List[str]] = None,
        **kwargs
    ):
        super(Device, self).__init__(**kwargs)
        self.device_id = device_id
        self.generation_id = generation_id
        self.etag = etag
        self.connection_state = connection_state
        self.status = status
        self.status_reason = status_reason
        self.connection_state_updated_time = connection_state_updated_time
        self.status_updated_time = status_updated_time
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication = authentication
        self.capabilities = capabilities
        self.device_scope = device_scope
        self.parent_scopes = parent_scopes


class DeviceCapabilities(msrest.serialization.Model):
    """The status of capabilities enabled on the device.

    :param iot_edge: The property that determines if the device is an edge device or not.
    :type iot_edge: bool
    """

    _attribute_map = {
        'iot_edge': {'key': 'iotEdge', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        iot_edge: Optional[bool] = None,
        **kwargs
    ):
        super(DeviceCapabilities, self).__init__(**kwargs)
        self.iot_edge = iot_edge


class FileUploadCompletionStatus(msrest.serialization.Model):
    """FileUploadCompletionStatus.

    :param correlation_id:
    :type correlation_id: str
    :param is_success:
    :type is_success: bool
    :param status_code:
    :type status_code: int
    :param status_description:
    :type status_description: str
    """

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'status_code': {'key': 'statusCode', 'type': 'int'},
        'status_description': {'key': 'statusDescription', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        correlation_id: Optional[str] = None,
        is_success: Optional[bool] = None,
        status_code: Optional[int] = None,
        status_description: Optional[str] = None,
        **kwargs
    ):
        super(FileUploadCompletionStatus, self).__init__(**kwargs)
        self.correlation_id = correlation_id
        self.is_success = is_success
        self.status_code = status_code
        self.status_description = status_description


class FileUploadRequest(msrest.serialization.Model):
    """FileUploadRequest.

    :param blob_name: Name of the blob.
    :type blob_name: str
    """

    _attribute_map = {
        'blob_name': {'key': 'blobName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        blob_name: Optional[str] = None,
        **kwargs
    ):
        super(FileUploadRequest, self).__init__(**kwargs)
        self.blob_name = blob_name


class FileUploadResponse(msrest.serialization.Model):
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

    def __init__(
        self,
        *,
        correlation_id: Optional[str] = None,
        host_name: Optional[str] = None,
        container_name: Optional[str] = None,
        blob_name: Optional[str] = None,
        sas_token: Optional[str] = None,
        **kwargs
    ):
        super(FileUploadResponse, self).__init__(**kwargs)
        self.correlation_id = correlation_id
        self.host_name = host_name
        self.container_name = container_name
        self.blob_name = blob_name
        self.sas_token = sas_token


class Module(msrest.serialization.Model):
    """The module identity on a device.

    :param module_id: The unique identifier of the module.
    :type module_id: str
    :param managed_by: Identifies who manages this module. For instance, this value is \"IotEdge\"
     if the edge runtime owns this module.
    :type managed_by: str
    :param device_id: The unique identifier of the device.
    :type device_id: str
    :param generation_id: The IoT Hub generated, case-sensitive string up to 128 characters long.
     This value is used to distinguish modules with the same moduleId, when they have been deleted
     and re-created.
    :type generation_id: str
    :param etag: The string representing a weak ETag for the module identity, as per RFC7232.
    :type etag: str
    :param connection_state: The connection state of the device. Possible values include:
     "Disconnected", "Connected".
    :type connection_state: str or ~iot_hub_gateway_device_apis.models.ModuleConnectionState
    :param connection_state_updated_time: The date and time the connection state was last updated.
    :type connection_state_updated_time: ~datetime.datetime
    :param last_activity_time: The date and time the device last connected, received, or sent a
     message.
    :type last_activity_time: ~datetime.datetime
    :param cloud_to_device_message_count: The number of cloud-to-module messages currently queued
     to be sent to the module.
    :type cloud_to_device_message_count: int
    :param authentication: The authentication mechanism used by the module when connecting to the
     service and edge hub.
    :type authentication: ~iot_hub_gateway_device_apis.models.AuthenticationMechanism
    """

    _attribute_map = {
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'generation_id': {'key': 'generationId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'connection_state_updated_time': {'key': 'connectionStateUpdatedTime', 'type': 'iso-8601'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'int'},
        'authentication': {'key': 'authentication', 'type': 'AuthenticationMechanism'},
    }

    def __init__(
        self,
        *,
        module_id: Optional[str] = None,
        managed_by: Optional[str] = None,
        device_id: Optional[str] = None,
        generation_id: Optional[str] = None,
        etag: Optional[str] = None,
        connection_state: Optional[Union[str, "ModuleConnectionState"]] = None,
        connection_state_updated_time: Optional[datetime.datetime] = None,
        last_activity_time: Optional[datetime.datetime] = None,
        cloud_to_device_message_count: Optional[int] = None,
        authentication: Optional["AuthenticationMechanism"] = None,
        **kwargs
    ):
        super(Module, self).__init__(**kwargs)
        self.module_id = module_id
        self.managed_by = managed_by
        self.device_id = device_id
        self.generation_id = generation_id
        self.etag = etag
        self.connection_state = connection_state
        self.connection_state_updated_time = connection_state_updated_time
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication = authentication


class ScopeResult(msrest.serialization.Model):
    """The query result.

    :param devices: The scope result items, as a collection.
    :type devices: list[~iot_hub_gateway_device_apis.models.Device]
    :param modules: The scope result items, as a collection.
    :type modules: list[~iot_hub_gateway_device_apis.models.Module]
    :param continuation_link: Request continuation token.
    :type continuation_link: str
    """

    _attribute_map = {
        'devices': {'key': 'devices', 'type': '[Device]'},
        'modules': {'key': 'modules', 'type': '[Module]'},
        'continuation_link': {'key': 'continuationLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        devices: Optional[List["Device"]] = None,
        modules: Optional[List["Module"]] = None,
        continuation_link: Optional[str] = None,
        **kwargs
    ):
        super(ScopeResult, self).__init__(**kwargs)
        self.devices = devices
        self.modules = modules
        self.continuation_link = continuation_link


class SymmetricKey(msrest.serialization.Model):
    """SymmetricKey.

    :param primary_key: The base64 encoded primary key of the device.
    :type primary_key: str
    :param secondary_key: The base64 encoded secondary key of the device.
    :type secondary_key: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        primary_key: Optional[str] = None,
        secondary_key: Optional[str] = None,
        **kwargs
    ):
        super(SymmetricKey, self).__init__(**kwargs)
        self.primary_key = primary_key
        self.secondary_key = secondary_key


class X509Thumbprint(msrest.serialization.Model):
    """X509Thumbprint.

    :param primary_thumbprint: The X509 client certificate primary thumbprint.
    :type primary_thumbprint: str
    :param secondary_thumbprint: The X509 client certificate secondary thumbprint.
    :type secondary_thumbprint: str
    """

    _attribute_map = {
        'primary_thumbprint': {'key': 'primaryThumbprint', 'type': 'str'},
        'secondary_thumbprint': {'key': 'secondaryThumbprint', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        primary_thumbprint: Optional[str] = None,
        secondary_thumbprint: Optional[str] = None,
        **kwargs
    ):
        super(X509Thumbprint, self).__init__(**kwargs)
        self.primary_thumbprint = primary_thumbprint
        self.secondary_thumbprint = secondary_thumbprint
