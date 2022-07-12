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

class DeviceGroupOtaPackage(object):
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
        'group_id': 'EntityGroupId',
        'id': 'str',
        'ota_package_id': 'OtaPackageId',
        'ota_package_type': 'str',
        'ota_package_update_time': 'int'
    }

    attribute_map = {
        'group_id': 'groupId',
        'id': 'id',
        'ota_package_id': 'otaPackageId',
        'ota_package_type': 'otaPackageType',
        'ota_package_update_time': 'otaPackageUpdateTime'
    }

    def __init__(self, group_id=None, id=None, ota_package_id=None, ota_package_type=None, ota_package_update_time=None):  # noqa: E501
        """DeviceGroupOtaPackage - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._id = None
        self._ota_package_id = None
        self._ota_package_type = None
        self._ota_package_update_time = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if ota_package_id is not None:
            self.ota_package_id = ota_package_id
        if ota_package_type is not None:
            self.ota_package_type = ota_package_type
        if ota_package_update_time is not None:
            self.ota_package_update_time = ota_package_update_time

    @property
    def group_id(self):
        """Gets the group_id of this DeviceGroupOtaPackage.  # noqa: E501


        :return: The group_id of this DeviceGroupOtaPackage.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeviceGroupOtaPackage.


        :param group_id: The group_id of this DeviceGroupOtaPackage.  # noqa: E501
        :type: EntityGroupId
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this DeviceGroupOtaPackage.  # noqa: E501


        :return: The id of this DeviceGroupOtaPackage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceGroupOtaPackage.


        :param id: The id of this DeviceGroupOtaPackage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ota_package_id(self):
        """Gets the ota_package_id of this DeviceGroupOtaPackage.  # noqa: E501


        :return: The ota_package_id of this DeviceGroupOtaPackage.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._ota_package_id

    @ota_package_id.setter
    def ota_package_id(self, ota_package_id):
        """Sets the ota_package_id of this DeviceGroupOtaPackage.


        :param ota_package_id: The ota_package_id of this DeviceGroupOtaPackage.  # noqa: E501
        :type: OtaPackageId
        """

        self._ota_package_id = ota_package_id

    @property
    def ota_package_type(self):
        """Gets the ota_package_type of this DeviceGroupOtaPackage.  # noqa: E501


        :return: The ota_package_type of this DeviceGroupOtaPackage.  # noqa: E501
        :rtype: str
        """
        return self._ota_package_type

    @ota_package_type.setter
    def ota_package_type(self, ota_package_type):
        """Sets the ota_package_type of this DeviceGroupOtaPackage.


        :param ota_package_type: The ota_package_type of this DeviceGroupOtaPackage.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRMWARE", "SOFTWARE"]  # noqa: E501
        if ota_package_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ota_package_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ota_package_type, allowed_values)
            )

        self._ota_package_type = ota_package_type

    @property
    def ota_package_update_time(self):
        """Gets the ota_package_update_time of this DeviceGroupOtaPackage.  # noqa: E501


        :return: The ota_package_update_time of this DeviceGroupOtaPackage.  # noqa: E501
        :rtype: int
        """
        return self._ota_package_update_time

    @ota_package_update_time.setter
    def ota_package_update_time(self, ota_package_update_time):
        """Sets the ota_package_update_time of this DeviceGroupOtaPackage.


        :param ota_package_update_time: The ota_package_update_time of this DeviceGroupOtaPackage.  # noqa: E501
        :type: int
        """

        self._ota_package_update_time = ota_package_update_time

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
        if issubclass(DeviceGroupOtaPackage, dict):
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
        if not isinstance(other, DeviceGroupOtaPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
