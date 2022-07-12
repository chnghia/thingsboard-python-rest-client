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

class ShortCustomerInfo(object):
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
        'public': 'bool',
        'customer_id': 'CustomerId',
        'title': 'str'
    }

    attribute_map = {
        'public': 'public',
        'customer_id': 'customerId',
        'title': 'title'
    }

    def __init__(self, public=None, customer_id=None, title=None):  # noqa: E501
        """ShortCustomerInfo - a model defined in Swagger"""  # noqa: E501
        self._public = None
        self._customer_id = None
        self._title = None
        self.discriminator = None
        if public is not None:
            self.public = public
        if customer_id is not None:
            self.customer_id = customer_id
        if title is not None:
            self.title = title

    @property
    def public(self):
        """Gets the public of this ShortCustomerInfo.  # noqa: E501


        :return: The public of this ShortCustomerInfo.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ShortCustomerInfo.


        :param public: The public of this ShortCustomerInfo.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def customer_id(self):
        """Gets the customer_id of this ShortCustomerInfo.  # noqa: E501


        :return: The customer_id of this ShortCustomerInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ShortCustomerInfo.


        :param customer_id: The customer_id of this ShortCustomerInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def title(self):
        """Gets the title of this ShortCustomerInfo.  # noqa: E501

        Title of the customer.  # noqa: E501

        :return: The title of this ShortCustomerInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShortCustomerInfo.

        Title of the customer.  # noqa: E501

        :param title: The title of this ShortCustomerInfo.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(ShortCustomerInfo, dict):
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
        if not isinstance(other, ShortCustomerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
