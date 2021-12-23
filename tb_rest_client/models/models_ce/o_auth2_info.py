# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OAuth2Info(object):
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
        'enabled': 'bool',
        'oauth2_params_infos': 'list[OAuth2ParamsInfo]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'oauth2_params_infos': 'oauth2ParamsInfos'
    }

    def __init__(self, enabled=None, oauth2_params_infos=None):  # noqa: E501
        """OAuth2Info - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._oauth2_params_infos = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        self.oauth2_params_infos = oauth2_params_infos

    @property
    def enabled(self):
        """Gets the enabled of this OAuth2Info.  # noqa: E501

        Whether OAuth2 settings are enabled or not  # noqa: E501

        :return: The enabled of this OAuth2Info.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OAuth2Info.

        Whether OAuth2 settings are enabled or not  # noqa: E501

        :param enabled: The enabled of this OAuth2Info.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def oauth2_params_infos(self):
        """Gets the oauth2_params_infos of this OAuth2Info.  # noqa: E501

        List of configured OAuth2 clients. Cannot contain null values  # noqa: E501

        :return: The oauth2_params_infos of this OAuth2Info.  # noqa: E501
        :rtype: list[OAuth2ParamsInfo]
        """
        return self._oauth2_params_infos

    @oauth2_params_infos.setter
    def oauth2_params_infos(self, oauth2_params_infos):
        """Sets the oauth2_params_infos of this OAuth2Info.

        List of configured OAuth2 clients. Cannot contain null values  # noqa: E501

        :param oauth2_params_infos: The oauth2_params_infos of this OAuth2Info.  # noqa: E501
        :type: list[OAuth2ParamsInfo]
        """
        if oauth2_params_infos is None:
            raise ValueError("Invalid value for `oauth2_params_infos`, must not be `None`")  # noqa: E501

        self._oauth2_params_infos = oauth2_params_infos

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
        if issubclass(OAuth2Info, dict):
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
        if not isinstance(other, OAuth2Info):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
