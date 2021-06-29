# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.4.5, generator: @autorest/python@5.8.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DeviceOperations(object):
    """DeviceOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.iot.gateway.device.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_devices_and_modules_in_scope(
        self,
        device_id,  # type: str
        module_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ScopeResult"
        """Query IotHub to retrieve information regarding devices which belong to the same deviceScope.

        Query IotHub to retrieve information regarding devices which belong to the same deviceScope.
        See https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language for more
        information. Pagination of results is supported. This returns information about device twins
        only.

        :param device_id:
        :type device_id: str
        :param module_id:
        :type module_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScopeResult, or the result of cls(response)
        :rtype: ~azure.iot.gateway.device.models.ScopeResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ScopeResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_devices_and_modules_in_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceId': self._serialize.url("device_id", device_id, 'str'),
            'moduleId': self._serialize.url("module_id", module_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('ScopeResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_devices_and_modules_in_scope.metadata = {'url': '/devices/{deviceId}/modules/{moduleId}/devicesAndModulesInDeviceScope'}  # type: ignore

    def get_device_and_module_in_scope(
        self,
        device_id,  # type: str
        module_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ScopeResult"
        """Get device registry information using module connect for a specific device in deviceScope.

        Get device registry information using module connect for a specific device in deviceScope. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language for more information.
        Pagination of results is supported. This returns information about device twins only.

        :param device_id:
        :type device_id: str
        :param module_id:
        :type module_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScopeResult, or the result of cls(response)
        :rtype: ~azure.iot.gateway.device.models.ScopeResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ScopeResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_device_and_module_in_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceId': self._serialize.url("device_id", device_id, 'str'),
            'moduleId': self._serialize.url("module_id", module_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('ScopeResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_device_and_module_in_scope.metadata = {'url': '/devices/{deviceId}/modules/{moduleId}/deviceAndModuleInDeviceScope'}  # type: ignore

    def send_device_event(
        self,
        id,  # type: str
        iothub_app_xxx=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Send a device-to-cloud message.

        Send a device-to-cloud message. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information.

        :param id: Device ID.
        :type id: str
        :param iothub_app_xxx: Optional application property prefixed with 'iothub-app-' to be placed
         in 'applicationProperties' section of the message ('iothub-app-' prefix will be stripped).
        :type iothub_app_xxx: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"

        # Construct URL
        url = self.send_device_event.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if iothub_app_xxx is not None:
            header_parameters['iothub-app-XXX'] = self._serialize.header("iothub_app_xxx", iothub_app_xxx, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    send_device_event.metadata = {'url': '/devices/{id}/messages/events'}  # type: ignore

    def receive_device_bound_notification(
        self,
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """This method is used to retrieve a cloud-to-device message.

        This method is used to retrieve a cloud-to-device message See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information. This
        capability is only available in the standard tier IoT Hub. For more information, see `Choose
        the right IoT Hub tier <https://aka.ms/scaleyouriotsolution>`_.

        :param id: Device ID.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"

        # Construct URL
        url = self.receive_device_bound_notification.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    receive_device_bound_notification.metadata = {'url': '/devices/{id}/messages/deviceBound'}  # type: ignore

    def abandon_device_bound_notification(
        self,
        id,  # type: str
        etag,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """This method abandons a cloud-to-device message.

        This method abandons a cloud-to-device message. The Etag obtained when the message was received
        must be provided to resolve race conditions when completing, rejecting, or abandoning a
        message. A abandoned message is put back in the device message queue for re-delivery to the
        device. See https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more
        information. Currently, the use of the Etag in the header does not comply with RFC 7232. A fix
        for this issue is currently on our backlog. This capability is only available in the standard
        tier IoT Hub. For more information, see `Choose the right IoT Hub tier
        <https://aka.ms/scaleyouriotsolution>`_.

        :param id: Device ID.
        :type id: str
        :param etag:
        :type etag: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"

        # Construct URL
        url = self.abandon_device_bound_notification.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
            'etag': self._serialize.url("etag", etag, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    abandon_device_bound_notification.metadata = {'url': '/devices/{id}/messages/deviceBound/{etag}/abandon'}  # type: ignore

    def create_file_upload_sas_uri(
        self,
        device_id,  # type: str
        file_upload_request,  # type: "_models.FileUploadRequest"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FileUploadResponse"
        """This method is used to retrieve a storage SAS URI to upload a file.

        This method is used to retrieve a storage SAS URI to upload a file. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-file-upload for more information.

        :param device_id: Device ID.
        :type device_id: str
        :param file_upload_request: File upload request object.
        :type file_upload_request: ~azure.iot.gateway.device.models.FileUploadRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileUploadResponse, or the result of cls(response)
        :rtype: ~azure.iot.gateway.device.models.FileUploadResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileUploadResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_file_upload_sas_uri.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceId': self._serialize.url("device_id", device_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(file_upload_request, 'FileUploadRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('FileUploadResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_file_upload_sas_uri.metadata = {'url': '/devices/{deviceId}/files'}  # type: ignore

    def update_file_upload_status(
        self,
        device_id,  # type: str
        file_upload_completion_status,  # type: "_models.FileUploadCompletionStatus"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FileUploadCompletionStatus"
        """This method is used to notify an IoT hub of a completed file upload.

        This method is used to notify an IoT hub of a completed file upload. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-file-upload for more information.

        :param device_id: Device ID.
        :type device_id: str
        :param file_upload_completion_status: File upload completion status object.
        :type file_upload_completion_status: ~azure.iot.gateway.device.models.FileUploadCompletionStatus
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileUploadCompletionStatus, or the result of cls(response)
        :rtype: ~azure.iot.gateway.device.models.FileUploadCompletionStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileUploadCompletionStatus"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_file_upload_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceId': self._serialize.url("device_id", device_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(file_upload_completion_status, 'FileUploadCompletionStatus')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('FileUploadCompletionStatus', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update_file_upload_status.metadata = {'url': '/devices/{deviceId}/files/notifications'}  # type: ignore

    def complete_device_bound_notification(
        self,
        id,  # type: str
        etag,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """This method completes or rejects a cloud-to-device message.

        This method completes or rejects a cloud-to-device message. The Etag obtained when the message
        was received must be provided to resolve race conditions when completing, rejecting, or
        abandoning a message. A completed message is deleted from the device message queue, and a
        positive acknowledgment is sent to the application back-end if requested. A rejected message
        causes it to be deadlettered. To reject a message, include a query parameter called \"reject\".
        See https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information.
        Currently, the use of the Etag in the header does not comply with RFC 7232. A fix for this
        issue is currently on our backlog. This capability is only available in the standard tier IoT
        Hub. For more information, see `Choose the right IoT Hub tier
        <https://aka.ms/scaleyouriotsolution>`_.

        :param id: Device ID.
        :type id: str
        :param etag:
        :type etag: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"

        # Construct URL
        url = self.complete_device_bound_notification.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
            'etag': self._serialize.url("etag", etag, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    complete_device_bound_notification.metadata = {'url': '/devices/{id}/messages/deviceBound/{etag}'}  # type: ignore
