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


class InternetSubscription(object):
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
        'id': 'str',
        'type': 'int',
        'priority': 'int',
        'comments': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'provider': 'MinProvider',
        'contacts': 'list[MinContact]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'priority': 'priority',
        'comments': 'comments',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'provider': 'provider',
        'contacts': 'contacts'
    }

    discriminator_value_class_map = {
              }

    def __init__(self, id=None, type=None, priority=None, comments=None, start_time=None, end_time=None, provider=None, contacts=None):  # noqa: E501
        """InternetSubscription - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._priority = None
        self._comments = None
        self._start_time = None
        self._end_time = None
        self._provider = None
        self._contacts = None
        self.discriminator = 'type'
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if priority is not None:
            self.priority = priority
        if comments is not None:
            self.comments = comments
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if provider is not None:
            self.provider = provider
        if contacts is not None:
            self.contacts = contacts

    @property
    def id(self):
        """Gets the id of this InternetSubscription.  # noqa: E501

        The identifier of this internet subscription  # noqa: E501

        :return: The id of this InternetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InternetSubscription.

        The identifier of this internet subscription  # noqa: E501

        :param id: The id of this InternetSubscription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InternetSubscription.  # noqa: E501

        Internet subscription type - 0 -> GSM - 1 -> ADSL - 2 -> SATELLITE - 3 -> LAN - 4 -> WIFI   # noqa: E501

        :return: The type of this InternetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InternetSubscription.

        Internet subscription type - 0 -> GSM - 1 -> ADSL - 2 -> SATELLITE - 3 -> LAN - 4 -> WIFI   # noqa: E501

        :param type: The type of this InternetSubscription.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def priority(self):
        """Gets the priority of this InternetSubscription.  # noqa: E501

        Internet subscription priority. - 0 -> PRIMARY - 1 -> SECONDARY - 2 -> TERMINATED   # noqa: E501

        :return: The priority of this InternetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InternetSubscription.

        Internet subscription priority. - 0 -> PRIMARY - 1 -> SECONDARY - 2 -> TERMINATED   # noqa: E501

        :param priority: The priority of this InternetSubscription.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def comments(self):
        """Gets the comments of this InternetSubscription.  # noqa: E501

        The comments about this internet subscription. This field can be unset when updating.  # noqa: E501

        :return: The comments of this InternetSubscription.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this InternetSubscription.

        The comments about this internet subscription. This field can be unset when updating.  # noqa: E501

        :param comments: The comments of this InternetSubscription.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def start_time(self):
        """Gets the start_time of this InternetSubscription.  # noqa: E501

        The start time of this internet subscription  # noqa: E501

        :return: The start_time of this InternetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InternetSubscription.

        The start time of this internet subscription  # noqa: E501

        :param start_time: The start_time of this InternetSubscription.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InternetSubscription.  # noqa: E501

        The end time this internet subscription. This field can be unset when updating.  # noqa: E501

        :return: The end_time of this InternetSubscription.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InternetSubscription.

        The end time this internet subscription. This field can be unset when updating.  # noqa: E501

        :param end_time: The end_time of this InternetSubscription.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def provider(self):
        """Gets the provider of this InternetSubscription.  # noqa: E501


        :return: The provider of this InternetSubscription.  # noqa: E501
        :rtype: MinProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this InternetSubscription.


        :param provider: The provider of this InternetSubscription.  # noqa: E501
        :type: MinProvider
        """

        self._provider = provider

    @property
    def contacts(self):
        """Gets the contacts of this InternetSubscription.  # noqa: E501


        :return: The contacts of this InternetSubscription.  # noqa: E501
        :rtype: list[MinContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this InternetSubscription.


        :param contacts: The contacts of this InternetSubscription.  # noqa: E501
        :type: list[MinContact]
        """

        self._contacts = contacts

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(InternetSubscription, dict):
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
        if not isinstance(other, InternetSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
