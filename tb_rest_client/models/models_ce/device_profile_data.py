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

class DeviceProfileData(object):
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
        'configuration': 'DeviceProfileConfiguration',
        'transport_configuration': 'DeviceProfileTransportConfiguration',
        'provision_configuration': 'DeviceProfileProvisionConfiguration',
        'alarms': 'list[DeviceProfileAlarm]'
    }

    attribute_map = {
        'configuration': 'configuration',
        'transport_configuration': 'transportConfiguration',
        'provision_configuration': 'provisionConfiguration',
        'alarms': 'alarms'
    }

    def __init__(self, configuration=None, transport_configuration=None, provision_configuration=None, alarms=None):  # noqa: E501
        """DeviceProfileData - a model defined in Swagger"""  # noqa: E501
        self._configuration = None
        self._transport_configuration = None
        self._provision_configuration = None
        self._alarms = None
        self.discriminator = None
        if configuration is not None:
            self.configuration = configuration
        if transport_configuration is not None:
            self.transport_configuration = transport_configuration
        if provision_configuration is not None:
            self.provision_configuration = provision_configuration
        if alarms is not None:
            self.alarms = alarms

    @property
    def configuration(self):
        """Gets the configuration of this DeviceProfileData.  # noqa: E501


        :return: The configuration of this DeviceProfileData.  # noqa: E501
        :rtype: DeviceProfileConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this DeviceProfileData.


        :param configuration: The configuration of this DeviceProfileData.  # noqa: E501
        :type: DeviceProfileConfiguration
        """

        self._configuration = configuration

    @property
    def transport_configuration(self):
        """Gets the transport_configuration of this DeviceProfileData.  # noqa: E501


        :return: The transport_configuration of this DeviceProfileData.  # noqa: E501
        :rtype: DeviceProfileTransportConfiguration
        """
        return self._transport_configuration

    @transport_configuration.setter
    def transport_configuration(self, transport_configuration):
        """Sets the transport_configuration of this DeviceProfileData.


        :param transport_configuration: The transport_configuration of this DeviceProfileData.  # noqa: E501
        :type: DeviceProfileTransportConfiguration
        """

        self._transport_configuration = transport_configuration

    @property
    def provision_configuration(self):
        """Gets the provision_configuration of this DeviceProfileData.  # noqa: E501


        :return: The provision_configuration of this DeviceProfileData.  # noqa: E501
        :rtype: DeviceProfileProvisionConfiguration
        """
        return self._provision_configuration

    @provision_configuration.setter
    def provision_configuration(self, provision_configuration):
        """Sets the provision_configuration of this DeviceProfileData.


        :param provision_configuration: The provision_configuration of this DeviceProfileData.  # noqa: E501
        :type: DeviceProfileProvisionConfiguration
        """

        self._provision_configuration = provision_configuration

    @property
    def alarms(self):
        """Gets the alarms of this DeviceProfileData.  # noqa: E501

        JSON array of alarm rules configuration per device profile  # noqa: E501

        :return: The alarms of this DeviceProfileData.  # noqa: E501
        :rtype: list[DeviceProfileAlarm]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        """Sets the alarms of this DeviceProfileData.

        JSON array of alarm rules configuration per device profile  # noqa: E501

        :param alarms: The alarms of this DeviceProfileData.  # noqa: E501
        :type: list[DeviceProfileAlarm]
        """

        self._alarms = alarms

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
        if issubclass(DeviceProfileData, dict):
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
        if not isinstance(other, DeviceProfileData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
