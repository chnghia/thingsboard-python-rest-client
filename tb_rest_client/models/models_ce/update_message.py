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

class UpdateMessage(object):
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
        'update_available': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'update_available': 'updateAvailable',
        'message': 'message'
    }

    def __init__(self, update_available=None, message=None):  # noqa: E501
        """UpdateMessage - a model defined in Swagger"""  # noqa: E501
        self._update_available = None
        self._message = None
        self.discriminator = None
        if update_available is not None:
            self.update_available = update_available
        if message is not None:
            self.message = message

    @property
    def update_available(self):
        """Gets the update_available of this UpdateMessage.  # noqa: E501


        :return: The update_available of this UpdateMessage.  # noqa: E501
        :rtype: bool
        """
        return self._update_available

    @update_available.setter
    def update_available(self, update_available):
        """Sets the update_available of this UpdateMessage.


        :param update_available: The update_available of this UpdateMessage.  # noqa: E501
        :type: bool
        """

        self._update_available = update_available

    @property
    def message(self):
        """Gets the message of this UpdateMessage.  # noqa: E501

        The message about new platform update available.  # noqa: E501

        :return: The message of this UpdateMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpdateMessage.

        The message about new platform update available.  # noqa: E501

        :param message: The message of this UpdateMessage.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(UpdateMessage, dict):
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
        if not isinstance(other, UpdateMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
