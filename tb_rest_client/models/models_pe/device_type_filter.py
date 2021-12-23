# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_pe.entity_filter import EntityFilter  # noqa: F401,E501


class DeviceTypeFilter(EntityFilter):
    """
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
        'device_name_filter': 'str',
        'device_type': 'str'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'device_name_filter': 'deviceNameFilter',
        'device_type': 'deviceType'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, device_name_filter=None, device_type=None, *args, **kwargs):  # noqa: E501
        """DeviceTypeFilter - a model defined in Swagger"""  # noqa: E501
        self._device_name_filter = None
        self._device_type = None
        self.discriminator = None
        if device_name_filter is not None:
            self.device_name_filter = device_name_filter
        if device_type is not None:
            self.device_type = device_type
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def device_name_filter(self):
        """Gets the device_name_filter of this DeviceTypeFilter.  # noqa: E501


        :return: The device_name_filter of this DeviceTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._device_name_filter

    @device_name_filter.setter
    def device_name_filter(self, device_name_filter):
        """Sets the device_name_filter of this DeviceTypeFilter.


        :param device_name_filter: The device_name_filter of this DeviceTypeFilter.  # noqa: E501
        :type: str
        """

        self._device_name_filter = device_name_filter

    @property
    def device_type(self):
        """Gets the device_type of this DeviceTypeFilter.  # noqa: E501


        :return: The device_type of this DeviceTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this DeviceTypeFilter.


        :param device_type: The device_type of this DeviceTypeFilter.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

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
        if issubclass(DeviceTypeFilter, dict):
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
        if not isinstance(other, DeviceTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
