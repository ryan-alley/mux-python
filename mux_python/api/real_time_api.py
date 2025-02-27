# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mux_python.api_client import ApiClient
from mux_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RealTimeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_realtime_breakdown(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Breakdown  # noqa: E501

        Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_breakdown(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_metric_id: ID of the Realtime Metric (required)
        :type realtime_metric_id: str
        :param dimension: Dimension the specified value belongs to
        :type dimension: str
        :param timestamp: Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
        :type timestamp: float
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param order_by: Value to order the results by
        :type order_by: str
        :param order_direction: Sort order.
        :type order_direction: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRealTimeBreakdownResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_realtime_breakdown_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501

    def get_realtime_breakdown_with_http_info(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Breakdown  # noqa: E501

        Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_breakdown_with_http_info(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_metric_id: ID of the Realtime Metric (required)
        :type realtime_metric_id: str
        :param dimension: Dimension the specified value belongs to
        :type dimension: str
        :param timestamp: Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
        :type timestamp: float
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param order_by: Value to order the results by
        :type order_by: str
        :param order_direction: Sort order.
        :type order_direction: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRealTimeBreakdownResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'realtime_metric_id',
            'dimension',
            'timestamp',
            'filters',
            'order_by',
            'order_direction'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_breakdown" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_metric_id' is set
        if self.api_client.client_side_validation and ('realtime_metric_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['realtime_metric_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `realtime_metric_id` when calling `get_realtime_breakdown`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_metric_id' in local_var_params:
            path_params['REALTIME_METRIC_ID'] = local_var_params['realtime_metric_id']  # noqa: E501

        query_params = []
        if 'dimension' in local_var_params and local_var_params['dimension'] is not None:  # noqa: E501
            query_params.append(('dimension', local_var_params['dimension']))  # noqa: E501
        if 'timestamp' in local_var_params and local_var_params['timestamp'] is not None:  # noqa: E501
            query_params.append(('timestamp', local_var_params['timestamp']))  # noqa: E501
        if 'filters' in local_var_params and local_var_params['filters'] is not None:  # noqa: E501
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('order_by', local_var_params['order_by']))  # noqa: E501
        if 'order_direction' in local_var_params and local_var_params['order_direction'] is not None:  # noqa: E501
            query_params.append(('order_direction', local_var_params['order_direction']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "GetRealTimeBreakdownResponse",
        }

        return self.api_client.call_api(
            '/data/v1/realtime/metrics/{REALTIME_METRIC_ID}/breakdown', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_realtime_histogram_timeseries(self, realtime_histogram_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Histogram Timeseries  # noqa: E501

        Gets histogram timeseries information for a specific metric.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_histogram_timeseries(realtime_histogram_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_histogram_metric_id: ID of the Realtime Histogram Metric (required)
        :type realtime_histogram_metric_id: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRealTimeHistogramTimeseriesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_realtime_histogram_timeseries_with_http_info(realtime_histogram_metric_id, **kwargs)  # noqa: E501

    def get_realtime_histogram_timeseries_with_http_info(self, realtime_histogram_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Histogram Timeseries  # noqa: E501

        Gets histogram timeseries information for a specific metric.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_histogram_timeseries_with_http_info(realtime_histogram_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_histogram_metric_id: ID of the Realtime Histogram Metric (required)
        :type realtime_histogram_metric_id: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRealTimeHistogramTimeseriesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'realtime_histogram_metric_id',
            'filters'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_histogram_timeseries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_histogram_metric_id' is set
        if self.api_client.client_side_validation and ('realtime_histogram_metric_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['realtime_histogram_metric_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `realtime_histogram_metric_id` when calling `get_realtime_histogram_timeseries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_histogram_metric_id' in local_var_params:
            path_params['REALTIME_HISTOGRAM_METRIC_ID'] = local_var_params['realtime_histogram_metric_id']  # noqa: E501

        query_params = []
        if 'filters' in local_var_params and local_var_params['filters'] is not None:  # noqa: E501
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "GetRealTimeHistogramTimeseriesResponse",
        }

        return self.api_client.call_api(
            '/data/v1/realtime/metrics/{REALTIME_HISTOGRAM_METRIC_ID}/histogram-timeseries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_realtime_timeseries(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Timeseries  # noqa: E501

        Gets Time series information for a specific metric along with the number of concurrent viewers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_timeseries(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_metric_id: ID of the Realtime Metric (required)
        :type realtime_metric_id: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRealTimeTimeseriesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_realtime_timeseries_with_http_info(realtime_metric_id, **kwargs)  # noqa: E501

    def get_realtime_timeseries_with_http_info(self, realtime_metric_id, **kwargs):  # noqa: E501
        """Get Real-Time Timeseries  # noqa: E501

        Gets Time series information for a specific metric along with the number of concurrent viewers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_realtime_timeseries_with_http_info(realtime_metric_id, async_req=True)
        >>> result = thread.get()

        :param realtime_metric_id: ID of the Realtime Metric (required)
        :type realtime_metric_id: str
        :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
        :type filters: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRealTimeTimeseriesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'realtime_metric_id',
            'filters'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_realtime_timeseries" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'realtime_metric_id' is set
        if self.api_client.client_side_validation and ('realtime_metric_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['realtime_metric_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `realtime_metric_id` when calling `get_realtime_timeseries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'realtime_metric_id' in local_var_params:
            path_params['REALTIME_METRIC_ID'] = local_var_params['realtime_metric_id']  # noqa: E501

        query_params = []
        if 'filters' in local_var_params and local_var_params['filters'] is not None:  # noqa: E501
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "GetRealTimeTimeseriesResponse",
        }

        return self.api_client.call_api(
            '/data/v1/realtime/metrics/{REALTIME_METRIC_ID}/timeseries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_realtime_dimensions(self, **kwargs):  # noqa: E501
        """List Real-Time Dimensions  # noqa: E501

        Lists available real-time dimensions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_realtime_dimensions(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListRealTimeDimensionsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_realtime_dimensions_with_http_info(**kwargs)  # noqa: E501

    def list_realtime_dimensions_with_http_info(self, **kwargs):  # noqa: E501
        """List Real-Time Dimensions  # noqa: E501

        Lists available real-time dimensions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_realtime_dimensions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListRealTimeDimensionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_realtime_dimensions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "ListRealTimeDimensionsResponse",
        }

        return self.api_client.call_api(
            '/data/v1/realtime/dimensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_realtime_metrics(self, **kwargs):  # noqa: E501
        """List Real-Time Metrics  # noqa: E501

        Lists available real-time metrics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_realtime_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListRealTimeMetricsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_realtime_metrics_with_http_info(**kwargs)  # noqa: E501

    def list_realtime_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """List Real-Time Metrics  # noqa: E501

        Lists available real-time metrics.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_realtime_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListRealTimeMetricsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_realtime_metrics" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "ListRealTimeMetricsResponse",
        }

        return self.api_client.call_api(
            '/data/v1/realtime/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
