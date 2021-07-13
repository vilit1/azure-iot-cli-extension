# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.4.5, generator: @autorest/python@5.8.3)
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

class CloudToDeviceMessagesOperations(object):
    """CloudToDeviceMessagesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~iot_hub_gateway_service_apis.models
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

    def purge_cloud_to_device_message_queue(
        self,
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.PurgeMessageQueueResult"
        """Deletes all the pending commands for a device in the IoT Hub.

        :param id: The unique identifier of the device.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PurgeMessageQueueResult, or the result of cls(response)
        :rtype: ~iot_hub_gateway_service_apis.models.PurgeMessageQueueResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PurgeMessageQueueResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-06-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.purge_cloud_to_device_message_queue.metadata['url']  # type: ignore
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('PurgeMessageQueueResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    purge_cloud_to_device_message_queue.metadata = {'url': '/devices/{id}/commands'}  # type: ignore

    def receive_feedback_notification(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Gets the feedback for cloud-to-device messages. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information. This
        capability is only available in the standard tier IoT Hub. For more information, see `Choose
        the right IoT Hub tier <https://aka.ms/scaleyouriotsolution>`_.

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
        url = self.receive_feedback_notification.metadata['url']  # type: ignore

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

    receive_feedback_notification.metadata = {'url': '/messages/serviceBound/feedback'}  # type: ignore

    def complete_feedback_notification(
        self,
        lock_token,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Completes the cloud-to-device feedback message. A completed message is deleted from the
        feedback queue of the service. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information.

        :param lock_token: The lock token obtained when the cloud-to-device message is received. This
         is used to resolve race conditions when completing a feedback message.
        :type lock_token: str
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
        url = self.complete_feedback_notification.metadata['url']  # type: ignore
        path_format_arguments = {
            'lockToken': self._serialize.url("lock_token", lock_token, 'str'),
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

    complete_feedback_notification.metadata = {'url': '/messages/serviceBound/feedback/{lockToken}'}  # type: ignore

    def abandon_feedback_notification(
        self,
        lock_token,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Abandons the lock on a cloud-to-device feedback message. See
        https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging for more information.

        :param lock_token: The lock token obtained when the cloud-to-device message is received.
        :type lock_token: str
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
        url = self.abandon_feedback_notification.metadata['url']  # type: ignore
        path_format_arguments = {
            'lockToken': self._serialize.url("lock_token", lock_token, 'str'),
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

    abandon_feedback_notification.metadata = {'url': '/messages/serviceBound/feedback/{lockToken}/abandon'}  # type: ignore
