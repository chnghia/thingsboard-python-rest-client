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

class EntityGroupInfo(object):
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
        'id': 'EntityGroupId',
        'created_time': 'int',
        'owner_id': 'EntityId',
        'name': 'str',
        'type': 'str',
        'additional_info': 'JsonNode',
        'configuration': 'JsonNode',
        'group_all': 'bool',
        'edge_group_all': 'bool',
        'owner_ids': 'list[EntityId]'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'owner_id': 'ownerId',
        'name': 'name',
        'type': 'type',
        'additional_info': 'additionalInfo',
        'configuration': 'configuration',
        'group_all': 'groupAll',
        'edge_group_all': 'edgeGroupAll',
        'owner_ids': 'ownerIds'
    }

    def __init__(self, id=None, created_time=None, owner_id=None, name=None, type=None, additional_info=None, configuration=None, group_all=None, edge_group_all=None, owner_ids=None):  # noqa: E501
        """EntityGroupInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._owner_id = None
        self._name = None
        self._type = None
        self._additional_info = None
        self._configuration = None
        self._group_all = None
        self._edge_group_all = None
        self._owner_ids = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if owner_id is not None:
            self.owner_id = owner_id
        self.name = name
        self.type = type
        if additional_info is not None:
            self.additional_info = additional_info
        if configuration is not None:
            self.configuration = configuration
        if group_all is not None:
            self.group_all = group_all
        if edge_group_all is not None:
            self.edge_group_all = edge_group_all
        self.owner_ids = owner_ids

    @property
    def id(self):
        """Gets the id of this EntityGroupInfo.  # noqa: E501


        :return: The id of this EntityGroupInfo.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityGroupInfo.


        :param id: The id of this EntityGroupInfo.  # noqa: E501
        :type: EntityGroupId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EntityGroupInfo.  # noqa: E501

        Timestamp of the entity group creation, in milliseconds  # noqa: E501

        :return: The created_time of this EntityGroupInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EntityGroupInfo.

        Timestamp of the entity group creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EntityGroupInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def owner_id(self):
        """Gets the owner_id of this EntityGroupInfo.  # noqa: E501


        :return: The owner_id of this EntityGroupInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this EntityGroupInfo.


        :param owner_id: The owner_id of this EntityGroupInfo.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this EntityGroupInfo.  # noqa: E501

        Name of the entity group  # noqa: E501

        :return: The name of this EntityGroupInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityGroupInfo.

        Name of the entity group  # noqa: E501

        :param name: The name of this EntityGroupInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this EntityGroupInfo.  # noqa: E501


        :return: The type of this EntityGroupInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityGroupInfo.


        :param type: The type of this EntityGroupInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ASSET", "CUSTOMER", "DASHBOARD", "DEVICE", "EDGE", "ENTITY_VIEW", "USER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityGroupInfo.  # noqa: E501


        :return: The additional_info of this EntityGroupInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityGroupInfo.


        :param additional_info: The additional_info of this EntityGroupInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def configuration(self):
        """Gets the configuration of this EntityGroupInfo.  # noqa: E501


        :return: The configuration of this EntityGroupInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this EntityGroupInfo.


        :param configuration: The configuration of this EntityGroupInfo.  # noqa: E501
        :type: JsonNode
        """

        self._configuration = configuration

    @property
    def group_all(self):
        """Gets the group_all of this EntityGroupInfo.  # noqa: E501

        Indicates special group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :return: The group_all of this EntityGroupInfo.  # noqa: E501
        :rtype: bool
        """
        return self._group_all

    @group_all.setter
    def group_all(self, group_all):
        """Sets the group_all of this EntityGroupInfo.

        Indicates special group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :param group_all: The group_all of this EntityGroupInfo.  # noqa: E501
        :type: bool
        """

        self._group_all = group_all

    @property
    def edge_group_all(self):
        """Gets the edge_group_all of this EntityGroupInfo.  # noqa: E501

        Indicates special edge group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :return: The edge_group_all of this EntityGroupInfo.  # noqa: E501
        :rtype: bool
        """
        return self._edge_group_all

    @edge_group_all.setter
    def edge_group_all(self, edge_group_all):
        """Sets the edge_group_all of this EntityGroupInfo.

        Indicates special edge group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :param edge_group_all: The edge_group_all of this EntityGroupInfo.  # noqa: E501
        :type: bool
        """

        self._edge_group_all = edge_group_all

    @property
    def owner_ids(self):
        """Gets the owner_ids of this EntityGroupInfo.  # noqa: E501

        List of the entity group owners.  # noqa: E501

        :return: The owner_ids of this EntityGroupInfo.  # noqa: E501
        :rtype: list[EntityId]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this EntityGroupInfo.

        List of the entity group owners.  # noqa: E501

        :param owner_ids: The owner_ids of this EntityGroupInfo.  # noqa: E501
        :type: list[EntityId]
        """
        if owner_ids is None:
            raise ValueError("Invalid value for `owner_ids`, must not be `None`")  # noqa: E501

        self._owner_ids = owner_ids

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
        if issubclass(EntityGroupInfo, dict):
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
        if not isinstance(other, EntityGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
