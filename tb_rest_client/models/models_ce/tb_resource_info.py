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

class TbResourceInfo(object):
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
        'id': 'TbResourceId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'title': 'str',
        'resource_type': 'str',
        'resource_key': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'title': 'title',
        'resource_type': 'resourceType',
        'resource_key': 'resourceKey'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, title=None, resource_type=None, resource_key=None):  # noqa: E501
        """TbResourceInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._title = None
        self._resource_type = None
        self._resource_key = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if title is not None:
            self.title = title
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_key is not None:
            self.resource_key = resource_key

    @property
    def id(self):
        """Gets the id of this TbResourceInfo.  # noqa: E501


        :return: The id of this TbResourceInfo.  # noqa: E501
        :rtype: TbResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TbResourceInfo.


        :param id: The id of this TbResourceInfo.  # noqa: E501
        :type: TbResourceId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this TbResourceInfo.  # noqa: E501

        Timestamp of the resource creation, in milliseconds  # noqa: E501

        :return: The created_time of this TbResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this TbResourceInfo.

        Timestamp of the resource creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this TbResourceInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TbResourceInfo.  # noqa: E501


        :return: The tenant_id of this TbResourceInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TbResourceInfo.


        :param tenant_id: The tenant_id of this TbResourceInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this TbResourceInfo.  # noqa: E501

        Resource title.  # noqa: E501

        :return: The title of this TbResourceInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TbResourceInfo.

        Resource title.  # noqa: E501

        :param title: The title of this TbResourceInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def resource_type(self):
        """Gets the resource_type of this TbResourceInfo.  # noqa: E501

        Resource type.  # noqa: E501

        :return: The resource_type of this TbResourceInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TbResourceInfo.

        Resource type.  # noqa: E501

        :param resource_type: The resource_type of this TbResourceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["JKS", "LWM2M_MODEL", "PKCS_12"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resource_key(self):
        """Gets the resource_key of this TbResourceInfo.  # noqa: E501

        Resource key.  # noqa: E501

        :return: The resource_key of this TbResourceInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        """Sets the resource_key of this TbResourceInfo.

        Resource key.  # noqa: E501

        :param resource_key: The resource_key of this TbResourceInfo.  # noqa: E501
        :type: str
        """

        self._resource_key = resource_key

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
        if issubclass(TbResourceInfo, dict):
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
        if not isinstance(other, TbResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
