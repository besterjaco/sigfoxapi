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
from sigfox_api_client.models.common_contract_info import CommonContractInfo


class ContractInfoCreate(object):
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
        'group_id': 'str',
        'contract_id': 'str',
        'user_id': 'str',
        'order_id': 'str',
        'order_name': 'str',
        'pricing_model': 'int',
        'start_time': 'int',
        'timezone': 'str',
        'subscription_plan': 'int',
        'token_duration': 'int',
        'blacklisted_territories': 'list[str]'
    }
    if hasattr(CommonContractInfo, "swagger_types"):
        swagger_types.update(CommonContractInfo.swagger_types)

    attribute_map = {
        'group_id': 'groupId',
        'contract_id': 'contractId',
        'user_id': 'userId',
        'order_id': 'orderId',
        'order_name': 'orderName',
        'pricing_model': 'pricingModel',
        'start_time': 'startTime',
        'timezone': 'timezone',
        'subscription_plan': 'subscriptionPlan',
        'token_duration': 'tokenDuration',
        'blacklisted_territories': 'blacklistedTerritories'
    }
    if hasattr(CommonContractInfo, "attribute_map"):
        attribute_map.update(CommonContractInfo.attribute_map)

    def __init__(self, group_id=None, contract_id=None, user_id=None, order_id=None, order_name=None, pricing_model=None, start_time=None, timezone=None, subscription_plan=None, token_duration=None, blacklisted_territories=None, *args, **kwargs):  # noqa: E501
        """ContractInfoCreate - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._contract_id = None
        self._user_id = None
        self._order_id = None
        self._order_name = None
        self._pricing_model = None
        self._start_time = None
        self._timezone = None
        self._subscription_plan = None
        self._token_duration = None
        self._blacklisted_territories = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if contract_id is not None:
            self.contract_id = contract_id
        if user_id is not None:
            self.user_id = user_id
        if order_id is not None:
            self.order_id = order_id
        if order_name is not None:
            self.order_name = order_name
        if pricing_model is not None:
            self.pricing_model = pricing_model
        if start_time is not None:
            self.start_time = start_time
        if timezone is not None:
            self.timezone = timezone
        if subscription_plan is not None:
            self.subscription_plan = subscription_plan
        if token_duration is not None:
            self.token_duration = token_duration
        if blacklisted_territories is not None:
            self.blacklisted_territories = blacklisted_territories
        CommonContractInfo.__init__(self, *args, **kwargs)

    @property
    def group_id(self):
        """Gets the group_id of this ContractInfoCreate.  # noqa: E501

        ID of group associated with the contact  # noqa: E501

        :return: The group_id of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ContractInfoCreate.

        ID of group associated with the contact  # noqa: E501

        :param group_id: The group_id of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractInfoCreate.  # noqa: E501

        The contract external ID. It's used to identify the contract in EDRs.  # noqa: E501

        :return: The contract_id of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractInfoCreate.

        The contract external ID. It's used to identify the contract in EDRs.  # noqa: E501

        :param contract_id: The contract_id of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._contract_id = contract_id

    @property
    def user_id(self):
        """Gets the user_id of this ContractInfoCreate.  # noqa: E501

        The ID of the user who created the contract in BSS.  # noqa: E501

        :return: The user_id of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ContractInfoCreate.

        The ID of the user who created the contract in BSS.  # noqa: E501

        :param user_id: The user_id of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def order_id(self):
        """Gets the order_id of this ContractInfoCreate.  # noqa: E501

        The order ID (hex), if any.  # noqa: E501

        :return: The order_id of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ContractInfoCreate.

        The order ID (hex), if any.  # noqa: E501

        :param order_id: The order_id of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_name(self):
        """Gets the order_name of this ContractInfoCreate.  # noqa: E501

        The order name, if any  # noqa: E501

        :return: The order_name of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._order_name

    @order_name.setter
    def order_name(self, order_name):
        """Sets the order_name of this ContractInfoCreate.

        The order name, if any  # noqa: E501

        :param order_name: The order_name of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._order_name = order_name

    @property
    def pricing_model(self):
        """Gets the pricing_model of this ContractInfoCreate.  # noqa: E501

        The pricing model used by this contract info. 1 -> Pricing model version 1. 2 -> Pricing model version 2. 3 -> Pricing model version 3.   # noqa: E501

        :return: The pricing_model of this ContractInfoCreate.  # noqa: E501
        :rtype: int
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """Sets the pricing_model of this ContractInfoCreate.

        The pricing model used by this contract info. 1 -> Pricing model version 1. 2 -> Pricing model version 2. 3 -> Pricing model version 3.   # noqa: E501

        :param pricing_model: The pricing_model of this ContractInfoCreate.  # noqa: E501
        :type: int
        """

        self._pricing_model = pricing_model

    @property
    def start_time(self):
        """Gets the start_time of this ContractInfoCreate.  # noqa: E501

        The start time (in milliseconds) of the contract  # noqa: E501

        :return: The start_time of this ContractInfoCreate.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ContractInfoCreate.

        The start time (in milliseconds) of the contract  # noqa: E501

        :param start_time: The start_time of this ContractInfoCreate.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def timezone(self):
        """Gets the timezone of this ContractInfoCreate.  # noqa: E501

        The contract timezone name as a Java TimeZone ID (\"full name\" version only, like \"America/Costa_Rica\").  # noqa: E501

        :return: The timezone of this ContractInfoCreate.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ContractInfoCreate.

        The contract timezone name as a Java TimeZone ID (\"full name\" version only, like \"America/Costa_Rica\").  # noqa: E501

        :param timezone: The timezone of this ContractInfoCreate.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def subscription_plan(self):
        """Gets the subscription_plan of this ContractInfoCreate.  # noqa: E501

        The contract info subscription plan. 0 -> Free order 1 -> Pay As You Grow (PAYG) 2 -> Committed Volume Plan (CVP) 3 -> Flexible Committed Volume Plan (CVP Flex) 4 -> PACK 5 -> DevKit 6 -> Activate   # noqa: E501

        :return: The subscription_plan of this ContractInfoCreate.  # noqa: E501
        :rtype: int
        """
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, subscription_plan):
        """Sets the subscription_plan of this ContractInfoCreate.

        The contract info subscription plan. 0 -> Free order 1 -> Pay As You Grow (PAYG) 2 -> Committed Volume Plan (CVP) 3 -> Flexible Committed Volume Plan (CVP Flex) 4 -> PACK 5 -> DevKit 6 -> Activate   # noqa: E501

        :param subscription_plan: The subscription_plan of this ContractInfoCreate.  # noqa: E501
        :type: int
        """

        self._subscription_plan = subscription_plan

    @property
    def token_duration(self):
        """Gets the token_duration of this ContractInfoCreate.  # noqa: E501

        The token duration in months. Must be >= 0, if 0 unlimited token duration.  # noqa: E501

        :return: The token_duration of this ContractInfoCreate.  # noqa: E501
        :rtype: int
        """
        return self._token_duration

    @token_duration.setter
    def token_duration(self, token_duration):
        """Sets the token_duration of this ContractInfoCreate.

        The token duration in months. Must be >= 0, if 0 unlimited token duration.  # noqa: E501

        :param token_duration: The token_duration of this ContractInfoCreate.  # noqa: E501
        :type: int
        """

        self._token_duration = token_duration

    @property
    def blacklisted_territories(self):
        """Gets the blacklisted_territories of this ContractInfoCreate.  # noqa: E501

        The list of \"blacklisted\" territories, as an array of NIP group IDs.  # noqa: E501

        :return: The blacklisted_territories of this ContractInfoCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._blacklisted_territories

    @blacklisted_territories.setter
    def blacklisted_territories(self, blacklisted_territories):
        """Sets the blacklisted_territories of this ContractInfoCreate.

        The list of \"blacklisted\" territories, as an array of NIP group IDs.  # noqa: E501

        :param blacklisted_territories: The blacklisted_territories of this ContractInfoCreate.  # noqa: E501
        :type: list[str]
        """

        self._blacklisted_territories = blacklisted_territories

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
        if issubclass(ContractInfoCreate, dict):
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
        if not isinstance(other, ContractInfoCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
