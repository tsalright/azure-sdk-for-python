# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class NetworkManagementClientOperationsMixin(object):

    def check_dns_name_availability(
        self,
        location,  # type: str
        domain_name_label=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DnsNameAvailabilityResult"
        """Checks whether a domain name in the cloudapp.net zone is available for use.

        :param location: The location of the domain name.
        :type location: str
        :param domain_name_label: The domain name to be verified. It must conform to the following
         regular expression: ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
        :type domain_name_label: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DnsNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2015_06_15.models.DnsNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DnsNameAvailabilityResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-06-15"

        # Construct URL
        url = self.check_dns_name_availability.metadata['url']  # type: ignore
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if domain_name_label is not None:
            query_parameters['domainNameLabel'] = self._serialize.query("domain_name_label", domain_name_label, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DnsNameAvailabilityResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    check_dns_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability'}  # type: ignore
