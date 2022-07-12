# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AlarmConditionFilter(object):
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
        'key': 'AlarmConditionFilterKey',
        'value_type': 'str',
        'value': 'object',
        'predicate': 'KeyFilterPredicate'
    }

    attribute_map = {
        'key': 'key',
        'value_type': 'valueType',
        'value': 'value',
        'predicate': 'predicate'
    }

    def __init__(self, key=None, value_type=None, value=None, predicate=None):  # noqa: E501
        """AlarmConditionFilter - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value_type = None
        self._value = None
        self._predicate = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if value_type is not None:
            self.value_type = value_type
        if value is not None:
            self.value = value
        if predicate is not None:
            self.predicate = predicate

    @property
    def key(self):
        """Gets the key of this AlarmConditionFilter.  # noqa: E501


        :return: The key of this AlarmConditionFilter.  # noqa: E501
        :rtype: AlarmConditionFilterKey
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AlarmConditionFilter.


        :param key: The key of this AlarmConditionFilter.  # noqa: E501
        :type: AlarmConditionFilterKey
        """

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this AlarmConditionFilter.  # noqa: E501

        String representation of the type of the value  # noqa: E501

        :return: The value_type of this AlarmConditionFilter.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AlarmConditionFilter.

        String representation of the type of the value  # noqa: E501

        :param value_type: The value_type of this AlarmConditionFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOOLEAN", "DATE_TIME", "NUMERIC", "STRING"]  # noqa: E501
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def value(self):
        """Gets the value of this AlarmConditionFilter.  # noqa: E501

        Value used in Constant comparison. For other types, such as TIME_SERIES or ATTRIBUTE, the predicate condition is used  # noqa: E501

        :return: The value of this AlarmConditionFilter.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AlarmConditionFilter.

        Value used in Constant comparison. For other types, such as TIME_SERIES or ATTRIBUTE, the predicate condition is used  # noqa: E501

        :param value: The value of this AlarmConditionFilter.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def predicate(self):
        """Gets the predicate of this AlarmConditionFilter.  # noqa: E501


        :return: The predicate of this AlarmConditionFilter.  # noqa: E501
        :rtype: KeyFilterPredicate
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this AlarmConditionFilter.


        :param predicate: The predicate of this AlarmConditionFilter.  # noqa: E501
        :type: KeyFilterPredicate
        """

        self._predicate = predicate

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
        if issubclass(AlarmConditionFilter, dict):
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
        if not isinstance(other, AlarmConditionFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
