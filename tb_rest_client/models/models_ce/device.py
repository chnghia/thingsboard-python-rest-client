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

class Device(object):
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
        'external_id': 'DeviceId',
        'id': 'DeviceId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'label': 'str',
        'device_profile_id': 'DeviceProfileId',
        'device_data': 'DeviceData',
        'firmware_id': 'OtaPackageId',
        'software_id': 'OtaPackageId',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'external_id': 'externalId',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'label': 'label',
        'device_profile_id': 'deviceProfileId',
        'device_data': 'deviceData',
        'firmware_id': 'firmwareId',
        'software_id': 'softwareId',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, external_id=None, id=None, created_time=None, tenant_id=None, customer_id=None, name=None, type=None, label=None, device_profile_id=None, device_data=None, firmware_id=None, software_id=None, additional_info=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._label = None
        self._device_profile_id = None
        self._device_data = None
        self._firmware_id = None
        self._software_id = None
        self._additional_info = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        self.type = type
        if label is not None:
            self.label = label
        self.device_profile_id = device_profile_id
        if device_data is not None:
            self.device_data = device_data
        if firmware_id is not None:
            self.firmware_id = firmware_id
        if software_id is not None:
            self.software_id = software_id
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def external_id(self):
        """Gets the external_id of this Device.  # noqa: E501


        :return: The external_id of this Device.  # noqa: E501
        :rtype: DeviceId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Device.


        :param external_id: The external_id of this Device.  # noqa: E501
        :type: DeviceId
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: DeviceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: DeviceId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this Device.  # noqa: E501

        Timestamp of the device creation, in milliseconds  # noqa: E501

        :return: The created_time of this Device.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Device.

        Timestamp of the device creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Device.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Device.  # noqa: E501


        :return: The tenant_id of this Device.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Device.


        :param tenant_id: The tenant_id of this Device.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Device.  # noqa: E501


        :return: The customer_id of this Device.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Device.


        :param customer_id: The customer_id of this Device.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501

        Unique Device Name in scope of Tenant  # noqa: E501

        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.

        Unique Device Name in scope of Tenant  # noqa: E501

        :param name: The name of this Device.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        Device Profile Name  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        Device Profile Name  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def label(self):
        """Gets the label of this Device.  # noqa: E501

        Label that may be used in widgets  # noqa: E501

        :return: The label of this Device.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Device.

        Label that may be used in widgets  # noqa: E501

        :param label: The label of this Device.  # noqa: E501
        :type: str
        """
        if label is None:
            self._label = None

        self._label = label

    @property
    def device_profile_id(self):
        """Gets the device_profile_id of this Device.  # noqa: E501


        :return: The device_profile_id of this Device.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._device_profile_id

    @device_profile_id.setter
    def device_profile_id(self, device_profile_id):
        """Sets the device_profile_id of this Device.


        :param device_profile_id: The device_profile_id of this Device.  # noqa: E501
        :type: DeviceProfileId
        """
        if device_profile_id is None:
            raise ValueError("Invalid value for `device_profile_id`, must not be `None`")  # noqa: E501

        self._device_profile_id = device_profile_id

    @property
    def device_data(self):
        """Gets the device_data of this Device.  # noqa: E501


        :return: The device_data of this Device.  # noqa: E501
        :rtype: DeviceData
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        """Sets the device_data of this Device.


        :param device_data: The device_data of this Device.  # noqa: E501
        :type: DeviceData
        """

        self._device_data = device_data

    @property
    def firmware_id(self):
        """Gets the firmware_id of this Device.  # noqa: E501


        :return: The firmware_id of this Device.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._firmware_id

    @firmware_id.setter
    def firmware_id(self, firmware_id):
        """Sets the firmware_id of this Device.


        :param firmware_id: The firmware_id of this Device.  # noqa: E501
        :type: OtaPackageId
        """

        self._firmware_id = firmware_id

    @property
    def software_id(self):
        """Gets the software_id of this Device.  # noqa: E501


        :return: The software_id of this Device.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this Device.


        :param software_id: The software_id of this Device.  # noqa: E501
        :type: OtaPackageId
        """

        self._software_id = software_id

    @property
    def additional_info(self):
        """Gets the additional_info of this Device.  # noqa: E501


        :return: The additional_info of this Device.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Device.


        :param additional_info: The additional_info of this Device.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
