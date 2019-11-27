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


class UpdateCallback(object):
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
        'channel': 'str',
        'callback_type': 'int',
        'callback_subtype': 'int',
        'payload_config': 'str',
        'enabled': 'bool',
        'send_duplicate': 'bool',
        'dead': 'bool'
    }

    attribute_map = {
        'channel': 'channel',
        'callback_type': 'callbackType',
        'callback_subtype': 'callbackSubtype',
        'payload_config': 'payloadConfig',
        'enabled': 'enabled',
        'send_duplicate': 'sendDuplicate',
        'dead': 'dead'
    }

    discriminator_value_class_map = {
          'updatebatchUrlCallback': 'UpdatebatchUrlCallback',
'updateUrlCallback': 'UpdateUrlCallback',
'updateEmailCallback': 'UpdateEmailCallback'    }

    def __init__(self, channel=None, callback_type=None, callback_subtype=None, payload_config=None, enabled=None, send_duplicate=None, dead=None):  # noqa: E501
        """UpdateCallback - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._callback_type = None
        self._callback_subtype = None
        self._payload_config = None
        self._enabled = None
        self._send_duplicate = None
        self._dead = None
        self.discriminator = 'channel'
        if channel is not None:
            self.channel = channel
        if callback_type is not None:
            self.callback_type = callback_type
        if callback_subtype is not None:
            self.callback_subtype = callback_subtype
        if payload_config is not None:
            self.payload_config = payload_config
        if enabled is not None:
            self.enabled = enabled
        if send_duplicate is not None:
            self.send_duplicate = send_duplicate
        if dead is not None:
            self.dead = dead

    @property
    def channel(self):
        """Gets the channel of this UpdateCallback.  # noqa: E501

        The callback's channel. - URL - BATCH_URL - EMAIL   # noqa: E501

        :return: The channel of this UpdateCallback.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this UpdateCallback.

        The callback's channel. - URL - BATCH_URL - EMAIL   # noqa: E501

        :param channel: The channel of this UpdateCallback.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def callback_type(self):
        """Gets the callback_type of this UpdateCallback.  # noqa: E501

        The callback's type.  # noqa: E501

        :return: The callback_type of this UpdateCallback.  # noqa: E501
        :rtype: int
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this UpdateCallback.

        The callback's type.  # noqa: E501

        :param callback_type: The callback_type of this UpdateCallback.  # noqa: E501
        :type: int
        """

        self._callback_type = callback_type

    @property
    def callback_subtype(self):
        """Gets the callback_subtype of this UpdateCallback.  # noqa: E501

        The callback's subtype. The subtype must be valid against its type. - 0 -> STATUS callback sending information about the status of a device (available for SERVICE callbacks) - 1 -> GEOLOC callback sent on a message that can be geolocated (available for SERVICE callbacks) ! Warning - From June 2019, the custom callback SERVICE/GEOLOC will be deprecated  ! - 2 -> UPLINK callback for an uplink message (available for DATA callbacks) - 3 -> BIDIR callback for a bidirectional message (available for DATA callbacks) - 4 -> ACKNOWLEDGE callback sent on a downlink acknowledged message (available for SERVICE callbacks) - 5 -> REPEATER callback triggered when a repeater sends an OOB (available for SERVICE callbacks) - 6 -> DATA_ADVANCED callback sent on a message that can be geolocated (available for SERVICE callbacks)   # noqa: E501

        :return: The callback_subtype of this UpdateCallback.  # noqa: E501
        :rtype: int
        """
        return self._callback_subtype

    @callback_subtype.setter
    def callback_subtype(self, callback_subtype):
        """Sets the callback_subtype of this UpdateCallback.

        The callback's subtype. The subtype must be valid against its type. - 0 -> STATUS callback sending information about the status of a device (available for SERVICE callbacks) - 1 -> GEOLOC callback sent on a message that can be geolocated (available for SERVICE callbacks) ! Warning - From June 2019, the custom callback SERVICE/GEOLOC will be deprecated  ! - 2 -> UPLINK callback for an uplink message (available for DATA callbacks) - 3 -> BIDIR callback for a bidirectional message (available for DATA callbacks) - 4 -> ACKNOWLEDGE callback sent on a downlink acknowledged message (available for SERVICE callbacks) - 5 -> REPEATER callback triggered when a repeater sends an OOB (available for SERVICE callbacks) - 6 -> DATA_ADVANCED callback sent on a message that can be geolocated (available for SERVICE callbacks)   # noqa: E501

        :param callback_subtype: The callback_subtype of this UpdateCallback.  # noqa: E501
        :type: int
        """

        self._callback_subtype = callback_subtype

    @property
    def payload_config(self):
        """Gets the payload_config of this UpdateCallback.  # noqa: E501

        The custom payload configuration. Only for DATA callbacks. This field can be unset when updating.  # noqa: E501

        :return: The payload_config of this UpdateCallback.  # noqa: E501
        :rtype: str
        """
        return self._payload_config

    @payload_config.setter
    def payload_config(self, payload_config):
        """Sets the payload_config of this UpdateCallback.

        The custom payload configuration. Only for DATA callbacks. This field can be unset when updating.  # noqa: E501

        :param payload_config: The payload_config of this UpdateCallback.  # noqa: E501
        :type: str
        """

        self._payload_config = payload_config

    @property
    def enabled(self):
        """Gets the enabled of this UpdateCallback.  # noqa: E501

        True to enable the callback, otherwise false  # noqa: E501

        :return: The enabled of this UpdateCallback.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateCallback.

        True to enable the callback, otherwise false  # noqa: E501

        :param enabled: The enabled of this UpdateCallback.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def send_duplicate(self):
        """Gets the send_duplicate of this UpdateCallback.  # noqa: E501

        True to duplicates callback, otherwise false  # noqa: E501

        :return: The send_duplicate of this UpdateCallback.  # noqa: E501
        :rtype: bool
        """
        return self._send_duplicate

    @send_duplicate.setter
    def send_duplicate(self, send_duplicate):
        """Sets the send_duplicate of this UpdateCallback.

        True to duplicates callback, otherwise false  # noqa: E501

        :param send_duplicate: The send_duplicate of this UpdateCallback.  # noqa: E501
        :type: bool
        """

        self._send_duplicate = send_duplicate

    @property
    def dead(self):
        """Gets the dead of this UpdateCallback.  # noqa: E501

        True if last use of the callback fails, otherwise false  # noqa: E501

        :return: The dead of this UpdateCallback.  # noqa: E501
        :rtype: bool
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """Sets the dead of this UpdateCallback.

        True if last use of the callback fails, otherwise false  # noqa: E501

        :param dead: The dead of this UpdateCallback.  # noqa: E501
        :type: bool
        """

        self._dead = dead

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
        if issubclass(UpdateCallback, dict):
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
        if not isinstance(other, UpdateCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other