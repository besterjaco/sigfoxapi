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
from sigfox_api_client.models.base_device_type import BaseDeviceType


class DeviceTypeUpdate(object):
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
        'payload_type': 'int',
        'payload_config': 'str',
        'downlink_mode': 'int',
        'downlink_data_string': 'str',
        'description': 'str',
        'contract_id': 'str',
        'contracts': 'list[ContractId]',
        'geoloc_payload_config_id': 'str',
        'automatic_renewal': 'bool'
    }
    if hasattr(BaseDeviceType, "swagger_types"):
        swagger_types.update(BaseDeviceType.swagger_types)

    attribute_map = {
        'payload_type': 'payloadType',
        'payload_config': 'payloadConfig',
        'downlink_mode': 'downlinkMode',
        'downlink_data_string': 'downlinkDataString',
        'description': 'description',
        'contract_id': 'contractId',
        'contracts': 'contracts',
        'geoloc_payload_config_id': 'geolocPayloadConfigId',
        'automatic_renewal': 'automaticRenewal'
    }
    if hasattr(BaseDeviceType, "attribute_map"):
        attribute_map.update(BaseDeviceType.attribute_map)

    def __init__(self, payload_type=None, payload_config=None, downlink_mode=None, downlink_data_string=None, description=None, contract_id=None, contracts=None, geoloc_payload_config_id=None, automatic_renewal=None, *args, **kwargs):  # noqa: E501
        """DeviceTypeUpdate - a model defined in Swagger"""  # noqa: E501
        self._payload_type = None
        self._payload_config = None
        self._downlink_mode = None
        self._downlink_data_string = None
        self._description = None
        self._contract_id = None
        self._contracts = None
        self._geoloc_payload_config_id = None
        self._automatic_renewal = None
        self.discriminator = None
        if payload_type is not None:
            self.payload_type = payload_type
        if payload_config is not None:
            self.payload_config = payload_config
        if downlink_mode is not None:
            self.downlink_mode = downlink_mode
        if downlink_data_string is not None:
            self.downlink_data_string = downlink_data_string
        if description is not None:
            self.description = description
        if contract_id is not None:
            self.contract_id = contract_id
        if contracts is not None:
            self.contracts = contracts
        if geoloc_payload_config_id is not None:
            self.geoloc_payload_config_id = geoloc_payload_config_id
        if automatic_renewal is not None:
            self.automatic_renewal = automatic_renewal
        BaseDeviceType.__init__(self, *args, **kwargs)

    @property
    def payload_type(self):
        """Gets the payload_type of this DeviceTypeUpdate.  # noqa: E501

        The payload type 2 -> Regular (raw payload) 3 -> Custom grammar 4 -> Geolocation 5 -> Display in ASCII 6 -> Radio planning frame 9 -> Sensitv2   # noqa: E501

        :return: The payload_type of this DeviceTypeUpdate.  # noqa: E501
        :rtype: int
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this DeviceTypeUpdate.

        The payload type 2 -> Regular (raw payload) 3 -> Custom grammar 4 -> Geolocation 5 -> Display in ASCII 6 -> Radio planning frame 9 -> Sensitv2   # noqa: E501

        :param payload_type: The payload_type of this DeviceTypeUpdate.  # noqa: E501
        :type: int
        """

        self._payload_type = payload_type

    @property
    def payload_config(self):
        """Gets the payload_config of this DeviceTypeUpdate.  # noqa: E501

        The payload configuration. Required if the payload type is Custom, else ignored.  # noqa: E501

        :return: The payload_config of this DeviceTypeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._payload_config

    @payload_config.setter
    def payload_config(self, payload_config):
        """Sets the payload_config of this DeviceTypeUpdate.

        The payload configuration. Required if the payload type is Custom, else ignored.  # noqa: E501

        :param payload_config: The payload_config of this DeviceTypeUpdate.  # noqa: E501
        :type: str
        """

        self._payload_config = payload_config

    @property
    def downlink_mode(self):
        """Gets the downlink_mode of this DeviceTypeUpdate.  # noqa: E501

        The downlink mode to use for the devices of this device type. 0 -> DIRECT 1 -> CALLBACK 2 -> NONE 3 -> MANAGED   # noqa: E501

        :return: The downlink_mode of this DeviceTypeUpdate.  # noqa: E501
        :rtype: int
        """
        return self._downlink_mode

    @downlink_mode.setter
    def downlink_mode(self, downlink_mode):
        """Sets the downlink_mode of this DeviceTypeUpdate.

        The downlink mode to use for the devices of this device type. 0 -> DIRECT 1 -> CALLBACK 2 -> NONE 3 -> MANAGED   # noqa: E501

        :param downlink_mode: The downlink_mode of this DeviceTypeUpdate.  # noqa: E501
        :type: int
        """

        self._downlink_mode = downlink_mode

    @property
    def downlink_data_string(self):
        """Gets the downlink_data_string of this DeviceTypeUpdate.  # noqa: E501

        Downlink data to be sent to the devices of this device type if downlinkMode is equal to 0. It must be an 8 byte length message given in hexadecimal string format.   # noqa: E501

        :return: The downlink_data_string of this DeviceTypeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._downlink_data_string

    @downlink_data_string.setter
    def downlink_data_string(self, downlink_data_string):
        """Sets the downlink_data_string of this DeviceTypeUpdate.

        Downlink data to be sent to the devices of this device type if downlinkMode is equal to 0. It must be an 8 byte length message given in hexadecimal string format.   # noqa: E501

        :param downlink_data_string: The downlink_data_string of this DeviceTypeUpdate.  # noqa: E501
        :type: str
        """

        self._downlink_data_string = downlink_data_string

    @property
    def description(self):
        """Gets the description of this DeviceTypeUpdate.  # noqa: E501

        The device types's description  # noqa: E501

        :return: The description of this DeviceTypeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceTypeUpdate.

        The device types's description  # noqa: E501

        :param description: The description of this DeviceTypeUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contract_id(self):
        """Gets the contract_id of this DeviceTypeUpdate.  # noqa: E501

        The device type's contract identifier (must be on the same group than the device type)  # noqa: E501

        :return: The contract_id of this DeviceTypeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this DeviceTypeUpdate.

        The device type's contract identifier (must be on the same group than the device type)  # noqa: E501

        :param contract_id: The contract_id of this DeviceTypeUpdate.  # noqa: E501
        :type: str
        """

        self._contract_id = contract_id

    @property
    def contracts(self):
        """Gets the contracts of this DeviceTypeUpdate.  # noqa: E501

        The device type's contract identifiers (must be on the same group than the device type)  # noqa: E501

        :return: The contracts of this DeviceTypeUpdate.  # noqa: E501
        :rtype: list[ContractId]
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this DeviceTypeUpdate.

        The device type's contract identifiers (must be on the same group than the device type)  # noqa: E501

        :param contracts: The contracts of this DeviceTypeUpdate.  # noqa: E501
        :type: list[ContractId]
        """

        self._contracts = contracts

    @property
    def geoloc_payload_config_id(self):
        """Gets the geoloc_payload_config_id of this DeviceTypeUpdate.  # noqa: E501

        The geoloc payload configuration identifier. Required if the payload type is Geolocation, else ignored.  # noqa: E501

        :return: The geoloc_payload_config_id of this DeviceTypeUpdate.  # noqa: E501
        :rtype: str
        """
        return self._geoloc_payload_config_id

    @geoloc_payload_config_id.setter
    def geoloc_payload_config_id(self, geoloc_payload_config_id):
        """Sets the geoloc_payload_config_id of this DeviceTypeUpdate.

        The geoloc payload configuration identifier. Required if the payload type is Geolocation, else ignored.  # noqa: E501

        :param geoloc_payload_config_id: The geoloc_payload_config_id of this DeviceTypeUpdate.  # noqa: E501
        :type: str
        """

        self._geoloc_payload_config_id = geoloc_payload_config_id

    @property
    def automatic_renewal(self):
        """Gets the automatic_renewal of this DeviceTypeUpdate.  # noqa: E501

        Allows the automatic renewal of devices attached to this device type  # noqa: E501

        :return: The automatic_renewal of this DeviceTypeUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_renewal

    @automatic_renewal.setter
    def automatic_renewal(self, automatic_renewal):
        """Sets the automatic_renewal of this DeviceTypeUpdate.

        Allows the automatic renewal of devices attached to this device type  # noqa: E501

        :param automatic_renewal: The automatic_renewal of this DeviceTypeUpdate.  # noqa: E501
        :type: bool
        """

        self._automatic_renewal = automatic_renewal

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
        if issubclass(DeviceTypeUpdate, dict):
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
        if not isinstance(other, DeviceTypeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
