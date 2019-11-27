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


class BulkDeviceAsynchronousRequest(object):
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
        'device_type_id': 'str',
        'product_certificate': 'CertificateUpdate',
        'prototype': 'bool',
        'prefix': 'str',
        'data': 'list[object]'
    }

    attribute_map = {
        'device_type_id': 'deviceTypeId',
        'product_certificate': 'productCertificate',
        'prototype': 'prototype',
        'prefix': 'prefix',
        'data': 'data'
    }

    def __init__(self, device_type_id=None, product_certificate=None, prototype=False, prefix=None, data=None):  # noqa: E501
        """BulkDeviceAsynchronousRequest - a model defined in Swagger"""  # noqa: E501
        self._device_type_id = None
        self._product_certificate = None
        self._prototype = None
        self._prefix = None
        self._data = None
        self.discriminator = None
        self.device_type_id = device_type_id
        if product_certificate is not None:
            self.product_certificate = product_certificate
        if prototype is not None:
            self.prototype = prototype
        if prefix is not None:
            self.prefix = prefix
        if data is not None:
            self.data = data

    @property
    def device_type_id(self):
        """Gets the device_type_id of this BulkDeviceAsynchronousRequest.  # noqa: E501

        The identifier of the device type under which the new devices will be created  # noqa: E501

        :return: The device_type_id of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_type_id

    @device_type_id.setter
    def device_type_id(self, device_type_id):
        """Sets the device_type_id of this BulkDeviceAsynchronousRequest.

        The identifier of the device type under which the new devices will be created  # noqa: E501

        :param device_type_id: The device_type_id of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :type: str
        """
        if device_type_id is None:
            raise ValueError("Invalid value for `device_type_id`, must not be `None`")  # noqa: E501

        self._device_type_id = device_type_id

    @property
    def product_certificate(self):
        """Gets the product_certificate of this BulkDeviceAsynchronousRequest.  # noqa: E501


        :return: The product_certificate of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :rtype: CertificateUpdate
        """
        return self._product_certificate

    @product_certificate.setter
    def product_certificate(self, product_certificate):
        """Sets the product_certificate of this BulkDeviceAsynchronousRequest.


        :param product_certificate: The product_certificate of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :type: CertificateUpdate
        """

        self._product_certificate = product_certificate

    @property
    def prototype(self):
        """Gets the prototype of this BulkDeviceAsynchronousRequest.  # noqa: E501

        Value describing if the devices are prototypes  # noqa: E501

        :return: The prototype of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :rtype: bool
        """
        return self._prototype

    @prototype.setter
    def prototype(self, prototype):
        """Sets the prototype of this BulkDeviceAsynchronousRequest.

        Value describing if the devices are prototypes  # noqa: E501

        :param prototype: The prototype of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :type: bool
        """

        self._prototype = prototype

    @property
    def prefix(self):
        """Gets the prefix of this BulkDeviceAsynchronousRequest.  # noqa: E501

        Prefix to used in device name  # noqa: E501

        :return: The prefix of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this BulkDeviceAsynchronousRequest.

        Prefix to used in device name  # noqa: E501

        :param prefix: The prefix of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def data(self):
        """Gets the data of this BulkDeviceAsynchronousRequest.  # noqa: E501


        :return: The data of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BulkDeviceAsynchronousRequest.


        :param data: The data of this BulkDeviceAsynchronousRequest.  # noqa: E501
        :type: list[object]
        """

        self._data = data

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
        if issubclass(BulkDeviceAsynchronousRequest, dict):
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
        if not isinstance(other, BulkDeviceAsynchronousRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
