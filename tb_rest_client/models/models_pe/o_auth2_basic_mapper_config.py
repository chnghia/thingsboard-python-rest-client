# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OAuth2BasicMapperConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'always_full_screen': 'bool',
        'customer_name_pattern': 'str',
        'default_dashboard_name': 'str',
        'email_attribute_key': 'str',
        'first_name_attribute_key': 'str',
        'last_name_attribute_key': 'str',
        'parent_customer_name_pattern': 'str',
        'tenant_name_pattern': 'str',
        'tenant_name_strategy': 'str',
        'user_groups_name_pattern': 'list[str]'
    }

    attribute_map = {
        'always_full_screen': 'alwaysFullScreen',
        'customer_name_pattern': 'customerNamePattern',
        'default_dashboard_name': 'defaultDashboardName',
        'email_attribute_key': 'emailAttributeKey',
        'first_name_attribute_key': 'firstNameAttributeKey',
        'last_name_attribute_key': 'lastNameAttributeKey',
        'parent_customer_name_pattern': 'parentCustomerNamePattern',
        'tenant_name_pattern': 'tenantNamePattern',
        'tenant_name_strategy': 'tenantNameStrategy',
        'user_groups_name_pattern': 'userGroupsNamePattern'
    }

    def __init__(self, always_full_screen=None, customer_name_pattern=None, default_dashboard_name=None, email_attribute_key=None, first_name_attribute_key=None, last_name_attribute_key=None, parent_customer_name_pattern=None, tenant_name_pattern=None, tenant_name_strategy=None, user_groups_name_pattern=None):  # noqa: E501
        """OAuth2BasicMapperConfig - a model defined in Swagger"""  # noqa: E501
        self._always_full_screen = None
        self._customer_name_pattern = None
        self._default_dashboard_name = None
        self._email_attribute_key = None
        self._first_name_attribute_key = None
        self._last_name_attribute_key = None
        self._parent_customer_name_pattern = None
        self._tenant_name_pattern = None
        self._tenant_name_strategy = None
        self._user_groups_name_pattern = None
        self.discriminator = None
        if always_full_screen is not None:
            self.always_full_screen = always_full_screen
        if customer_name_pattern is not None:
            self.customer_name_pattern = customer_name_pattern
        if default_dashboard_name is not None:
            self.default_dashboard_name = default_dashboard_name
        if email_attribute_key is not None:
            self.email_attribute_key = email_attribute_key
        if first_name_attribute_key is not None:
            self.first_name_attribute_key = first_name_attribute_key
        if last_name_attribute_key is not None:
            self.last_name_attribute_key = last_name_attribute_key
        if parent_customer_name_pattern is not None:
            self.parent_customer_name_pattern = parent_customer_name_pattern
        if tenant_name_pattern is not None:
            self.tenant_name_pattern = tenant_name_pattern
        self.tenant_name_strategy = tenant_name_strategy
        if user_groups_name_pattern is not None:
            self.user_groups_name_pattern = user_groups_name_pattern

    @property
    def always_full_screen(self):
        """Gets the always_full_screen of this OAuth2BasicMapperConfig.  # noqa: E501

        Whether default dashboard should be open in full screen  # noqa: E501

        :return: The always_full_screen of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: bool
        """
        return self._always_full_screen

    @always_full_screen.setter
    def always_full_screen(self, always_full_screen):
        """Sets the always_full_screen of this OAuth2BasicMapperConfig.

        Whether default dashboard should be open in full screen  # noqa: E501

        :param always_full_screen: The always_full_screen of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: bool
        """

        self._always_full_screen = always_full_screen

    @property
    def customer_name_pattern(self):
        """Gets the customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501

        Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user  # noqa: E501

        :return: The customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._customer_name_pattern

    @customer_name_pattern.setter
    def customer_name_pattern(self, customer_name_pattern):
        """Sets the customer_name_pattern of this OAuth2BasicMapperConfig.

        Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user  # noqa: E501

        :param customer_name_pattern: The customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._customer_name_pattern = customer_name_pattern

    @property
    def default_dashboard_name(self):
        """Gets the default_dashboard_name of this OAuth2BasicMapperConfig.  # noqa: E501

        Name of the tenant's dashboard to set as default dashboard for newly created user  # noqa: E501

        :return: The default_dashboard_name of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._default_dashboard_name

    @default_dashboard_name.setter
    def default_dashboard_name(self, default_dashboard_name):
        """Sets the default_dashboard_name of this OAuth2BasicMapperConfig.

        Name of the tenant's dashboard to set as default dashboard for newly created user  # noqa: E501

        :param default_dashboard_name: The default_dashboard_name of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._default_dashboard_name = default_dashboard_name

    @property
    def email_attribute_key(self):
        """Gets the email_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501

        Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type  # noqa: E501

        :return: The email_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._email_attribute_key

    @email_attribute_key.setter
    def email_attribute_key(self, email_attribute_key):
        """Sets the email_attribute_key of this OAuth2BasicMapperConfig.

        Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type  # noqa: E501

        :param email_attribute_key: The email_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._email_attribute_key = email_attribute_key

    @property
    def first_name_attribute_key(self):
        """Gets the first_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501

        First name attribute key  # noqa: E501

        :return: The first_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._first_name_attribute_key

    @first_name_attribute_key.setter
    def first_name_attribute_key(self, first_name_attribute_key):
        """Sets the first_name_attribute_key of this OAuth2BasicMapperConfig.

        First name attribute key  # noqa: E501

        :param first_name_attribute_key: The first_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._first_name_attribute_key = first_name_attribute_key

    @property
    def last_name_attribute_key(self):
        """Gets the last_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501

        Last name attribute key  # noqa: E501

        :return: The last_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._last_name_attribute_key

    @last_name_attribute_key.setter
    def last_name_attribute_key(self, last_name_attribute_key):
        """Sets the last_name_attribute_key of this OAuth2BasicMapperConfig.

        Last name attribute key  # noqa: E501

        :param last_name_attribute_key: The last_name_attribute_key of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._last_name_attribute_key = last_name_attribute_key

    @property
    def parent_customer_name_pattern(self):
        """Gets the parent_customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501


        :return: The parent_customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._parent_customer_name_pattern

    @parent_customer_name_pattern.setter
    def parent_customer_name_pattern(self, parent_customer_name_pattern):
        """Sets the parent_customer_name_pattern of this OAuth2BasicMapperConfig.


        :param parent_customer_name_pattern: The parent_customer_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._parent_customer_name_pattern = parent_customer_name_pattern

    @property
    def tenant_name_pattern(self):
        """Gets the tenant_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501

        Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}'  # noqa: E501

        :return: The tenant_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name_pattern

    @tenant_name_pattern.setter
    def tenant_name_pattern(self, tenant_name_pattern):
        """Sets the tenant_name_pattern of this OAuth2BasicMapperConfig.

        Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}'  # noqa: E501

        :param tenant_name_pattern: The tenant_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """

        self._tenant_name_pattern = tenant_name_pattern

    @property
    def tenant_name_strategy(self):
        """Gets the tenant_name_strategy of this OAuth2BasicMapperConfig.  # noqa: E501

        Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@')  # noqa: E501

        :return: The tenant_name_strategy of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name_strategy

    @tenant_name_strategy.setter
    def tenant_name_strategy(self, tenant_name_strategy):
        """Sets the tenant_name_strategy of this OAuth2BasicMapperConfig.

        Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@')  # noqa: E501

        :param tenant_name_strategy: The tenant_name_strategy of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: str
        """
        if tenant_name_strategy is None:
            raise ValueError("Invalid value for `tenant_name_strategy`, must not be `None`")  # noqa: E501
        allowed_values = ["CUSTOM", "DOMAIN", "EMAIL"]  # noqa: E501
        if tenant_name_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `tenant_name_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(tenant_name_strategy, allowed_values)
            )

        self._tenant_name_strategy = tenant_name_strategy

    @property
    def user_groups_name_pattern(self):
        """Gets the user_groups_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501


        :return: The user_groups_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups_name_pattern

    @user_groups_name_pattern.setter
    def user_groups_name_pattern(self, user_groups_name_pattern):
        """Sets the user_groups_name_pattern of this OAuth2BasicMapperConfig.


        :param user_groups_name_pattern: The user_groups_name_pattern of this OAuth2BasicMapperConfig.  # noqa: E501
        :type: list[str]
        """

        self._user_groups_name_pattern = user_groups_name_pattern

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
        if issubclass(OAuth2BasicMapperConfig, dict):
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
        if not isinstance(other, OAuth2BasicMapperConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
