# coding: utf-8

"""
    Sigfox API

     # API overview Sigfox API is used to integrate with the Sigfox platform.  The API uses the HTTP protocol, following the REST principles (POST, GET, DELETE, PUT requests). The API endpoints accept and return data in the JSON format, with the corresponding \"application/json\" content type header.  The Sigfox API access differs for every API User based on their profile. If you already have a Sigfox account, you can retrieve the API Documentation customized for your API User directly in json or yaml format. The “how to” procedure is detailed in the [API Documentation](https://support.sigfox.com/docs/api-documentation) article.  The PUT request is the only request used to edit an existing entity. You don't need to specify each value. If a property is not present in the request, it won't be processed and updated. To remove an optional property, it must be filled in the request with the explicit value NULL. If a property has no value, it won't appear in the result of a GET request.  # Authentication and security Sigfox API is only accessible using HTTPS, and all API endpoints require authentication credentials (API user login and password). An API User is associated to a group with given profiles. You can view and manage your API User in the [Sigfox Portal](https://backend.sigfox.com/auth/login).  If you need an API User, follow the [API credential creation](https://support.sigfox.com/docs/api-credential-creation) procedure.  Your API User must remain private. Should the API credentials be compromised, new ones can be generated at any moment, invalidating the previous ones. CORS and JSONP are intentionally unsupported. CORS and JSONP JavaScript techniques tends to expose your credentials to your users. If you really need to call Sigfox API from JavaScript in the browser, you must set a reverse proxy on your website. Be careful not to use proxy for all requests to Sigfox OSS but to only select the relevant ones.  <!-- ReDoc-Inject: <security-definitions> -->  # Usage limits All Sigfox API endpoints are using the same underlying technology that powers the core Sigfox Platform. For Cloud efficiency and security reasons, Sigfox is moving a step forward on API rate limiting, by setting upper bounds for some API endpoints. Please note that a new HTTP response will be returned in case of rate exceeded : “HTTP 429: too many requests”.  For more information check [API Rate limiting](https://support.sigfox.com/docs/api-rate-limiting) policy. Sigfox reserves the right to modify these limits without notice.  # Versioning  Sigfox API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vX\", where X is the version number. For example: v2/device.  All requests must include the version suffix in the endpoint URL.  Any new backwards-incompatible change will be released in a new version.   Read the [API versioning management](https://storage.sbg1.cloud.ovh.net/v1/AUTH_669d7dfced0b44518cb186841d7cbd75/prod_docs/55746591-API_Versioning_management.pdf) to learn more about it.  # Paging  Some API requests will return a list of data. If the list is longer than the set limit, the items will be retrieved via multiple requests. The paging section in the response will specify a URL for the next request.  Keep in mind rate limiting policy to manage your requests.  You can use the limit parameter to limit the number of items to be returned, between 1 and 100 (default). The offset parameter is used to specify a number of items to skip.  # Errors  Sigfox API uses conventional HTTP response codes to indicate the success or failure of an API request.  Codes in the 2xx range indicate success.  Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter missing, a resource was not found, etc.). Often the response will also include a message explaining the error.  Codes in the 5xx range indicate an error with servers.   For more information please refer to the [Response code article](https://support.sigfox.com/docs/api-response-code-references).   # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from sigfox_api_client.models.callback_email import CallbackEmail


class CallbackMedium(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'headers': 'object',
        'body': 'str',
        'content_type': 'str',
        'method': 'str',
        'error': 'str'
    }
    if hasattr(CallbackEmail, "swagger_types"):
        swagger_types.update(CallbackEmail.swagger_types)

    attribute_map = {
        'url': 'url',
        'headers': 'headers',
        'body': 'body',
        'content_type': 'contentType',
        'method': 'method',
        'error': 'error'
    }
    if hasattr(CallbackEmail, "attribute_map"):
        attribute_map.update(CallbackEmail.attribute_map)

    def __init__(self, url=None, headers=None, body=None, content_type=None, method=None, error=None, *args, **kwargs):  # noqa: E501
        """CallbackMedium - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._headers = None
        self._body = None
        self._content_type = None
        self._method = None
        self._error = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body
        if content_type is not None:
            self.content_type = content_type
        if method is not None:
            self.method = method
        if error is not None:
            self.error = error
        CallbackEmail.__init__(self, *args, **kwargs)

    @property
    def url(self):
        """Gets the url of this CallbackMedium.  # noqa: E501

        The URL called when this message has been processed  # noqa: E501

        :return: The url of this CallbackMedium.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CallbackMedium.

        The URL called when this message has been processed  # noqa: E501

        :param url: The url of this CallbackMedium.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this CallbackMedium.  # noqa: E501

        The headers sent in the request. If no header is defined, this field is not present.  # noqa: E501

        :return: The headers of this CallbackMedium.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this CallbackMedium.

        The headers sent in the request. If no header is defined, this field is not present.  # noqa: E501

        :param headers: The headers of this CallbackMedium.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def body(self):
        """Gets the body of this CallbackMedium.  # noqa: E501

        The body of the request, if any. It is only present if the request method is POST.  # noqa: E501

        :return: The body of this CallbackMedium.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CallbackMedium.

        The body of the request, if any. It is only present if the request method is POST.  # noqa: E501

        :param body: The body of this CallbackMedium.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def content_type(self):
        """Gets the content_type of this CallbackMedium.  # noqa: E501

        The content type of the request. It is only present if the request is a POST.  # noqa: E501

        :return: The content_type of this CallbackMedium.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CallbackMedium.

        The content type of the request. It is only present if the request is a POST.  # noqa: E501

        :param content_type: The content_type of this CallbackMedium.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def method(self):
        """Gets the method of this CallbackMedium.  # noqa: E501

        The HTTP method, currently only GET, POST or PUT.  # noqa: E501

        :return: The method of this CallbackMedium.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CallbackMedium.

        The HTTP method, currently only GET, POST or PUT.  # noqa: E501

        :param method: The method of this CallbackMedium.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def error(self):
        """Gets the error of this CallbackMedium.  # noqa: E501

        If there was an error, for instance if the body is JSON and could not be evaluated.  # noqa: E501

        :return: The error of this CallbackMedium.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CallbackMedium.

        If there was an error, for instance if the body is JSON and could not be evaluated.  # noqa: E501

        :param error: The error of this CallbackMedium.  # noqa: E501
        :type: str
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CallbackMedium, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CallbackMedium):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
