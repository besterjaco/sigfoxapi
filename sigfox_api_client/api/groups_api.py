# coding: utf-8

"""
    Sigfox API

     # API overview Sigfox API is used to integrate with the Sigfox platform.  The API uses the HTTP protocol, following the REST principles (POST, GET, DELETE, PUT requests). The API endpoints accept and return data in the JSON format, with the corresponding \"application/json\" content type header.  The Sigfox API access differs for every API User based on their profile. If you already have a Sigfox account, you can retrieve the API Documentation customized for your API User directly in json or yaml format. The “how to” procedure is detailed in the [API Documentation](https://support.sigfox.com/docs/api-documentation) article.  The PUT request is the only request used to edit an existing entity. You don't need to specify each value. If a property is not present in the request, it won't be processed and updated. To remove an optional property, it must be filled in the request with the explicit value NULL. If a property has no value, it won't appear in the result of a GET request.  # Authentication and security Sigfox API is only accessible using HTTPS, and all API endpoints require authentication credentials (API user login and password). An API User is associated to a group with given profiles. You can view and manage your API User in the [Sigfox Portal](https://backend.sigfox.com/auth/login).  If you need an API User, follow the [API credential creation](https://support.sigfox.com/docs/api-credential-creation) procedure.  Your API User must remain private. Should the API credentials be compromised, new ones can be generated at any moment, invalidating the previous ones. CORS and JSONP are intentionally unsupported. CORS and JSONP JavaScript techniques tends to expose your credentials to your users. If you really need to call Sigfox API from JavaScript in the browser, you must set a reverse proxy on your website. Be careful not to use proxy for all requests to Sigfox OSS but to only select the relevant ones.  <!-- ReDoc-Inject: <security-definitions> -->  # Usage limits All Sigfox API endpoints are using the same underlying technology that powers the core Sigfox Platform. For Cloud efficiency and security reasons, Sigfox is moving a step forward on API rate limiting, by setting upper bounds for some API endpoints. Please note that a new HTTP response will be returned in case of rate exceeded : “HTTP 429: too many requests”.  For more information check [API Rate limiting](https://support.sigfox.com/docs/api-rate-limiting) policy. Sigfox reserves the right to modify these limits without notice.  # Versioning  Sigfox API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vX\", where X is the version number. For example: v2/device.  All requests must include the version suffix in the endpoint URL.  Any new backwards-incompatible change will be released in a new version.   Read the [API versioning management](https://storage.sbg1.cloud.ovh.net/v1/AUTH_669d7dfced0b44518cb186841d7cbd75/prod_docs/55746591-API_Versioning_management.pdf) to learn more about it.  # Paging  Some API requests will return a list of data. If the list is longer than the set limit, the items will be retrieved via multiple requests. The paging section in the response will specify a URL for the next request.  Keep in mind rate limiting policy to manage your requests.  You can use the limit parameter to limit the number of items to be returned, between 1 and 100 (default). The offset parameter is used to specify a number of items to skip.  # Errors  Sigfox API uses conventional HTTP response codes to indicate the success or failure of an API request.  Codes in the 2xx range indicate success.  Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter missing, a resource was not found, etc.). Often the response will also include a message explaining the error.  Codes in the 5xx range indicate an error with servers.   For more information please refer to the [Response code article](https://support.sigfox.com/docs/api-response-code-references).   # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sigfox_api_client.api_client import ApiClient


class GroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_group(self, body, **kwargs):  # noqa: E501
        """Create a group  # noqa: E501

        Create a new group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommonGroupCreate body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a group  # noqa: E501

        Create a new group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommonGroupCreate body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_group(self, id, **kwargs):  # noqa: E501
        """Delete a group  # noqa: E501

        Delete a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a group  # noqa: E501

        Delete a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_callback_messages_error_list_for_group(self, id, **kwargs):  # noqa: E501
        """Retrieve a list of undelivered callbacks  # noqa: E501

        Retrieve a list of undelivered callbacks and errors for a given group, in reverse chronological order (most recent message first).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_callback_messages_error_list_for_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param int since: Starting timestamp (in milliseconds since Unix Epoch)
        :param int before: Ending timestamp (in milliseconds since Unix Epoch)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_callback_messages_error_list_for_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_callback_messages_error_list_for_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_callback_messages_error_list_for_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a list of undelivered callbacks  # noqa: E501

        Retrieve a list of undelivered callbacks and errors for a given group, in reverse chronological order (most recent message first).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_callback_messages_error_list_for_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param int since: Starting timestamp (in milliseconds since Unix Epoch)
        :param int before: Ending timestamp (in milliseconds since Unix Epoch)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'since', 'before', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_callback_messages_error_list_for_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_callback_messages_error_list_for_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/callbacks-not-delivered', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group(self, id, **kwargs):  # noqa: E501
        """Retrieve information about a group  # noqa: E501

        Retrieve information about a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param str fields: Defines the other available fields to be returned in the response. 
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve information about a group  # noqa: E501

        Retrieve information about a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param str fields: Defines the other available fields to be returned in the response. 
        :return: Group
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Group',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_geolocation_payload(self, id, **kwargs):  # noqa: E501
        """Retrieve a list of geolocation payload  # noqa: E501

        Retrieve a list of geolocation payload according to request filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_geolocation_payload(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :param str page_id: Token representing the page to retrieve
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_geolocation_payload_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_geolocation_payload_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_geolocation_payload_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve a list of geolocation payload  # noqa: E501

        Retrieve a list of geolocation payload according to request filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_geolocation_payload_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Group identifier (required)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :param str page_id: Token representing the page to retrieve
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'offset', 'page_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_geolocation_payload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_geolocation_payload`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_id' in params:
            query_params.append(('pageId', params['page_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}/geoloc-payloads', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_groups(self, **kwargs):  # noqa: E501
        """Retrieve a list of groups according to visibility permissions and request filters.  # noqa: E501

        Retrieve a list of groups according to visibility permissions and request filters.    If parentIds is provided, retrieve all direct sub-groups under the given parents. If parentIds is not provided, retrieve all direct sub-groups under the API user's group.   If deep is true, retrieve all sub-groups under either given parent groups or the API user group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] parent_ids: The parent group's identifiers from which the children will be fetched
        :param bool deep: Retrieve all sub-groups
        :param str name: Searches for groups containing the given text in their name
        :param list[int] types: Group's type - 0 -> SO - 2 -> Other - 5 -> SVNO - 6 -> Partners - 7 -> NIP - 8 -> DIST - 9 -> Channel - 10 -> Starter - 11 -> Partner 
        :param str fields: Defines the other available fields to be returned in the response. 
        :param str sort: The field on which the list will be sorted. (field to sort ascending or -field to sort descending)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :param str page_id: Token representing the page to retrieve
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of groups according to visibility permissions and request filters.  # noqa: E501

        Retrieve a list of groups according to visibility permissions and request filters.    If parentIds is provided, retrieve all direct sub-groups under the given parents. If parentIds is not provided, retrieve all direct sub-groups under the API user's group.   If deep is true, retrieve all sub-groups under either given parent groups or the API user group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] parent_ids: The parent group's identifiers from which the children will be fetched
        :param bool deep: Retrieve all sub-groups
        :param str name: Searches for groups containing the given text in their name
        :param list[int] types: Group's type - 0 -> SO - 2 -> Other - 5 -> SVNO - 6 -> Partners - 7 -> NIP - 8 -> DIST - 9 -> Channel - 10 -> Starter - 11 -> Partner 
        :param str fields: Defines the other available fields to be returned in the response. 
        :param str sort: The field on which the list will be sorted. (field to sort ascending or -field to sort descending)
        :param int limit: The maximum number of items to return
        :param int offset: The number of items to skip
        :param str page_id: Token representing the page to retrieve
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parent_ids', 'deep', 'name', 'types', 'fields', 'sort', 'limit', 'offset', 'page_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_ids' in params:
            query_params.append(('parentIds', params['parent_ids']))  # noqa: E501
            collection_formats['parentIds'] = 'csv'  # noqa: E501
        if 'deep' in params:
            query_params.append(('deep', params['deep']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'types' in params:
            query_params.append(('types', params['types']))  # noqa: E501
            collection_formats['types'] = 'csv'  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'page_id' in params:
            query_params.append(('pageId', params['page_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_group(self, body, id, **kwargs):  # noqa: E501
        """Update a group  # noqa: E501

        Update a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommonGroupUpdate body: The group to update (required)
        :param str id: The Group identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_group_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_group_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a group  # noqa: E501

        Update a given group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommonGroupUpdate body: The group to update (required)
        :param str id: The Group identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
