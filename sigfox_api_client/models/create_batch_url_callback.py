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
from sigfox_api_client.models.create_callback import CreateCallback


class CreateBatchUrlCallback(object):
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
        'http_method': 'str',
        'line_pattern': 'str'
    }
    if hasattr(CreateCallback, "swagger_types"):
        swagger_types.update(CreateCallback.swagger_types)

    attribute_map = {
        'url': 'url',
        'http_method': 'httpMethod',
        'line_pattern': 'linePattern'
    }
    if hasattr(CreateCallback, "attribute_map"):
        attribute_map.update(CreateCallback.attribute_map)

    def __init__(self, url=None, http_method=None, line_pattern=None, *args, **kwargs):  # noqa: E501
        """CreateBatchUrlCallback - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._http_method = None
        self._line_pattern = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if http_method is not None:
            self.http_method = http_method
        if line_pattern is not None:
            self.line_pattern = line_pattern
        CreateCallback.__init__(self, *args, **kwargs)

    @property
    def url(self):
        """Gets the url of this CreateBatchUrlCallback.  # noqa: E501

        The callback's url  # noqa: E501

        :return: The url of this CreateBatchUrlCallback.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateBatchUrlCallback.

        The callback's url  # noqa: E501

        :param url: The url of this CreateBatchUrlCallback.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def http_method(self):
        """Gets the http_method of this CreateBatchUrlCallback.  # noqa: E501

        The http method used to send a callback  # noqa: E501

        :return: The http_method of this CreateBatchUrlCallback.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this CreateBatchUrlCallback.

        The http method used to send a callback  # noqa: E501

        :param http_method: The http_method of this CreateBatchUrlCallback.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "PUT", "POST"]  # noqa: E501
        if http_method not in allowed_values:
            raise ValueError(
                "Invalid value for `http_method` ({0}), must be one of {1}"  # noqa: E501
                .format(http_method, allowed_values)
            )

        self._http_method = http_method

    @property
    def line_pattern(self):
        """Gets the line_pattern of this CreateBatchUrlCallback.  # noqa: E501

        The line pattern representing a message.  # noqa: E501

        :return: The line_pattern of this CreateBatchUrlCallback.  # noqa: E501
        :rtype: str
        """
        return self._line_pattern

    @line_pattern.setter
    def line_pattern(self, line_pattern):
        """Sets the line_pattern of this CreateBatchUrlCallback.

        The line pattern representing a message.  # noqa: E501

        :param line_pattern: The line_pattern of this CreateBatchUrlCallback.  # noqa: E501
        :type: str
        """

        self._line_pattern = line_pattern

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
        if issubclass(CreateBatchUrlCallback, dict):
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
        if not isinstance(other, CreateBatchUrlCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
