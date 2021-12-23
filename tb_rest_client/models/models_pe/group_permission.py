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

class GroupPermission(object):
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
        'id': 'GroupPermissionId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'user_group_id': 'EntityGroupId',
        'role_id': 'RoleId',
        'entity_group_id': 'EntityGroupId',
        'entity_group_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'public': 'public',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'user_group_id': 'userGroupId',
        'role_id': 'roleId',
        'entity_group_id': 'entityGroupId',
        'entity_group_type': 'entityGroupType',
        'name': 'name'
    }

    def __init__(self, public=None, id=None, created_time=None, tenant_id=None, user_group_id=None, role_id=None, entity_group_id=None, entity_group_type=None, name=None):  # noqa: E501
        """GroupPermission - a model defined in Swagger"""  # noqa: E501
        self._public = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._user_group_id = None
        self._role_id = None
        self._entity_group_id = None
        self._entity_group_type = None
        self._name = None
        self.discriminator = None
        if public is not None:
            self.public = public
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if role_id is not None:
            self.role_id = role_id
        if entity_group_id is not None:
            self.entity_group_id = entity_group_id
        if entity_group_type is not None:
            self.entity_group_type = entity_group_type
        if name is not None:
            self.name = name

    @property
    def public(self):
        """Gets the public of this GroupPermission.  # noqa: E501


        :return: The public of this GroupPermission.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this GroupPermission.


        :param public: The public of this GroupPermission.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def id(self):
        """Gets the id of this GroupPermission.  # noqa: E501


        :return: The id of this GroupPermission.  # noqa: E501
        :rtype: GroupPermissionId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupPermission.


        :param id: The id of this GroupPermission.  # noqa: E501
        :type: GroupPermissionId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this GroupPermission.  # noqa: E501

        Timestamp of the group permission creation, in milliseconds  # noqa: E501

        :return: The created_time of this GroupPermission.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this GroupPermission.

        Timestamp of the group permission creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this GroupPermission.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this GroupPermission.  # noqa: E501


        :return: The tenant_id of this GroupPermission.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this GroupPermission.


        :param tenant_id: The tenant_id of this GroupPermission.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def user_group_id(self):
        """Gets the user_group_id of this GroupPermission.  # noqa: E501


        :return: The user_group_id of this GroupPermission.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this GroupPermission.


        :param user_group_id: The user_group_id of this GroupPermission.  # noqa: E501
        :type: EntityGroupId
        """

        self._user_group_id = user_group_id

    @property
    def role_id(self):
        """Gets the role_id of this GroupPermission.  # noqa: E501


        :return: The role_id of this GroupPermission.  # noqa: E501
        :rtype: RoleId
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this GroupPermission.


        :param role_id: The role_id of this GroupPermission.  # noqa: E501
        :type: RoleId
        """

        self._role_id = role_id

    @property
    def entity_group_id(self):
        """Gets the entity_group_id of this GroupPermission.  # noqa: E501


        :return: The entity_group_id of this GroupPermission.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._entity_group_id

    @entity_group_id.setter
    def entity_group_id(self, entity_group_id):
        """Sets the entity_group_id of this GroupPermission.


        :param entity_group_id: The entity_group_id of this GroupPermission.  # noqa: E501
        :type: EntityGroupId
        """

        self._entity_group_id = entity_group_id

    @property
    def entity_group_type(self):
        """Gets the entity_group_type of this GroupPermission.  # noqa: E501

        Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc.  # noqa: E501

        :return: The entity_group_type of this GroupPermission.  # noqa: E501
        :rtype: str
        """
        return self._entity_group_type

    @entity_group_type.setter
    def entity_group_type(self, entity_group_type):
        """Sets the entity_group_type of this GroupPermission.

        Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc.  # noqa: E501

        :param entity_group_type: The entity_group_type of this GroupPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "BILLING_CUSTOMER", "BLOB_ENTITY", "CONVERTER", "COUPON", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "OTA_PACKAGE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "SUBSCRIPTION", "SUBSCRIPTION_PLAN", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if entity_group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_group_type, allowed_values)
            )

        self._entity_group_type = entity_group_type

    @property
    def name(self):
        """Gets the name of this GroupPermission.  # noqa: E501

        Name of the Group Permissions. Auto-generated  # noqa: E501

        :return: The name of this GroupPermission.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupPermission.

        Name of the Group Permissions. Auto-generated  # noqa: E501

        :param name: The name of this GroupPermission.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GroupPermission, dict):
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
        if not isinstance(other, GroupPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
