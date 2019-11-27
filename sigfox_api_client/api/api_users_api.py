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


class ApiUsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_profile_to_api_user(self, body, id, **kwargs):  # noqa: E501
        """Associate profiles to an API user.  # noqa: E501

        Associate new profiles to a given API user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_profile_to_api_user(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileIds body: The API profile to update (required)
        :param str id: The API user identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_profile_to_api_user_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_profile_to_api_user_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def add_profile_to_api_user_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Associate profiles to an API user.  # noqa: E501

        Associate new profiles to a given API user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_profile_to_api_user_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileIds body: The API profile to update (required)
        :param str id: The API user identifier (required)
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
                    " to method add_profile_to_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_profile_to_api_user`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_profile_to_api_user`")  # noqa: E501

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
            '/api-users/{id}/profiles', 'PUT',
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

    def create_api_user(self, body, **kwargs):  # noqa: E501
        """Create an API user  # noqa: E501

        Create a new API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_api_user(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiUserCreation body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_api_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_api_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_api_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an API user  # noqa: E501

        Create a new API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_api_user_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiUserCreation body: (required)
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
                    " to method create_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_api_user`")  # noqa: E501

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
            '/api-users/', 'POST',
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

    def delete_api_user(self, id, **kwargs):  # noqa: E501
        """Delete an API user  # noqa: E501

        Delete a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_api_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_api_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_api_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete an API user  # noqa: E501

        Delete a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
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
                    " to method delete_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_api_user`")  # noqa: E501

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
            '/api-users/{id}', 'DELETE',
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

    def delete_profile_of_api_user(self, id, profile_id, **kwargs):  # noqa: E501
        """Delete a profile to a given API user.  # noqa: E501

        Delete a profile to a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_profile_of_api_user(id, profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :param str profile_id: The profile identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_profile_of_api_user_with_http_info(id, profile_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_profile_of_api_user_with_http_info(id, profile_id, **kwargs)  # noqa: E501
            return data

    def delete_profile_of_api_user_with_http_info(self, id, profile_id, **kwargs):  # noqa: E501
        """Delete a profile to a given API user.  # noqa: E501

        Delete a profile to a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_profile_of_api_user_with_http_info(id, profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :param str profile_id: The profile identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'profile_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_profile_of_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_profile_of_api_user`")  # noqa: E501
        # verify the required parameter 'profile_id' is set
        if ('profile_id' not in params or
                params['profile_id'] is None):
            raise ValueError("Missing the required parameter `profile_id` when calling `delete_profile_of_api_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'profile_id' in params:
            path_params['profileId'] = params['profile_id']  # noqa: E501

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
            '/api-users/{id}/profiles/{profileId}', 'DELETE',
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

    def get_api_user(self, id, **kwargs):  # noqa: E501
        """Retrieve information about an API user  # noqa: E501

        Retrieve information about a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :param str fields: Defines the other available fields to be returned in the response. 
        :return: ApiUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_api_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_api_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve information about an API user  # noqa: E501

        Retrieve information about a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :param str fields: Defines the other available fields to be returned in the response. 
        :return: ApiUser
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
                    " to method get_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_api_user`")  # noqa: E501

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
            '/api-users/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_api_users(self, **kwargs):  # noqa: E501
        """Retrieve a list of API users  # noqa: E501

        Retrieve a list of API users according to visibility permissions and request filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_api_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Defines the other available fields to be returned in the response. 
        :param str profile_id: Searches for API users with the given profile
        :param list[str] group_ids: Searches for API users who are attached to the given groups
        :param int limit: Defines the maximum number of items to return
        :param int offset: Defines the number of items to skip
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_api_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_api_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_api_users_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of API users  # noqa: E501

        Retrieve a list of API users according to visibility permissions and request filters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_api_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Defines the other available fields to be returned in the response. 
        :param str profile_id: Searches for API users with the given profile
        :param list[str] group_ids: Searches for API users who are attached to the given groups
        :param int limit: Defines the maximum number of items to return
        :param int offset: Defines the number of items to skip
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'profile_id', 'group_ids', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_api_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'profile_id' in params:
            query_params.append(('profileId', params['profile_id']))  # noqa: E501
        if 'group_ids' in params:
            query_params.append(('groupIds', params['group_ids']))  # noqa: E501
            collection_formats['groupIds'] = 'csv'  # noqa: E501
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
            '/api-users/', 'GET',
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

    def renew_credential(self, id, **kwargs):  # noqa: E501
        """Generate a new password for an API user  # noqa: E501

        Generate a new password for a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_credential(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.renew_credential_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.renew_credential_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def renew_credential_with_http_info(self, id, **kwargs):  # noqa: E501
        """Generate a new password for an API user  # noqa: E501

        Generate a new password for a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_credential_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The API user identifier (required)
        :return: object
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
                    " to method renew_credential" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `renew_credential`")  # noqa: E501

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
            '/api-users/{id}/renew-credential', 'PUT',
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

    def update_api_user(self, body, id, **kwargs):  # noqa: E501
        """Update an API user  # noqa: E501

        Update information about a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_user(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiUserEdition body: The information to update (required)
        :param str id: The API user identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_api_user_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_api_user_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_api_user_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update an API user  # noqa: E501

        Update information about a given API user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_user_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiUserEdition body: The information to update (required)
        :param str id: The API user identifier (required)
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
                    " to method update_api_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_api_user`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_api_user`")  # noqa: E501

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
            '/api-users/{id}', 'PUT',
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
