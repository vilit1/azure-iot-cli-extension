# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.4.5, generator: @autorest/python@5.8.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import IotHubGatewayServiceAPIsConfiguration
from .operations import ConfigurationOperations
from .operations import StatisticsOperations
from .operations import DevicesOperations
from .operations import BulkRegistryOperations
from .operations import QueryOperations
from .operations import JobsOperations
from .operations import CloudToDeviceMessagesOperations
from .operations import ModulesOperations
from .operations import DigitalTwinOperations
from .operations import TopicSpaceOperations
from . import models


class IotHubGatewayServiceAPIs(object):
    """IotHubGatewayServiceAPIs.

    :ivar configuration: ConfigurationOperations operations
    :vartype configuration: iot_hub_gateway_service_apis.operations.ConfigurationOperations
    :ivar statistics: StatisticsOperations operations
    :vartype statistics: iot_hub_gateway_service_apis.operations.StatisticsOperations
    :ivar devices: DevicesOperations operations
    :vartype devices: iot_hub_gateway_service_apis.operations.DevicesOperations
    :ivar bulk_registry: BulkRegistryOperations operations
    :vartype bulk_registry: iot_hub_gateway_service_apis.operations.BulkRegistryOperations
    :ivar query: QueryOperations operations
    :vartype query: iot_hub_gateway_service_apis.operations.QueryOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: iot_hub_gateway_service_apis.operations.JobsOperations
    :ivar cloud_to_device_messages: CloudToDeviceMessagesOperations operations
    :vartype cloud_to_device_messages: iot_hub_gateway_service_apis.operations.CloudToDeviceMessagesOperations
    :ivar modules: ModulesOperations operations
    :vartype modules: iot_hub_gateway_service_apis.operations.ModulesOperations
    :ivar digital_twin: DigitalTwinOperations operations
    :vartype digital_twin: iot_hub_gateway_service_apis.operations.DigitalTwinOperations
    :ivar topic_space: TopicSpaceOperations operations
    :vartype topic_space: iot_hub_gateway_service_apis.operations.TopicSpaceOperations
    :param str base_url: Service URL
    """

    def __init__(
        self,
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://fully-qualified-iothubname.azure-devices.net'
        self._config = IotHubGatewayServiceAPIsConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.configuration = ConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.statistics = StatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bulk_registry = BulkRegistryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_to_device_messages = CloudToDeviceMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.modules = ModulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.digital_twin = DigitalTwinOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.topic_space = TopicSpaceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        http_request.url = self._client.format_url(http_request.url)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> IotHubGatewayServiceAPIs
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
