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

class EdgeSearchQuery(object):
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
        'relation_type': 'str',
        'edge_types': 'list[str]',
        'parameters': 'RelationsSearchParameters'
    }

    attribute_map = {
        'relation_type': 'relationType',
        'edge_types': 'edgeTypes',
        'parameters': 'parameters'
    }

    def __init__(self, relation_type=None, edge_types=None, parameters=None):  # noqa: E501
        """EdgeSearchQuery - a model defined in Swagger"""  # noqa: E501
        self._relation_type = None
        self._edge_types = None
        self._parameters = None
        self.discriminator = None
        if relation_type is not None:
            self.relation_type = relation_type
        if edge_types is not None:
            self.edge_types = edge_types
        if parameters is not None:
            self.parameters = parameters

    @property
    def relation_type(self):
        """Gets the relation_type of this EdgeSearchQuery.  # noqa: E501

        Type of the relation between root entity and edge (e.g. 'Contains' or 'Manages').  # noqa: E501

        :return: The relation_type of this EdgeSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this EdgeSearchQuery.

        Type of the relation between root entity and edge (e.g. 'Contains' or 'Manages').  # noqa: E501

        :param relation_type: The relation_type of this EdgeSearchQuery.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def edge_types(self):
        """Gets the edge_types of this EdgeSearchQuery.  # noqa: E501

        Array of edge types to filter the related entities (e.g. 'Silos', 'Stores').  # noqa: E501

        :return: The edge_types of this EdgeSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._edge_types

    @edge_types.setter
    def edge_types(self, edge_types):
        """Sets the edge_types of this EdgeSearchQuery.

        Array of edge types to filter the related entities (e.g. 'Silos', 'Stores').  # noqa: E501

        :param edge_types: The edge_types of this EdgeSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._edge_types = edge_types

    @property
    def parameters(self):
        """Gets the parameters of this EdgeSearchQuery.  # noqa: E501


        :return: The parameters of this EdgeSearchQuery.  # noqa: E501
        :rtype: RelationsSearchParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this EdgeSearchQuery.


        :param parameters: The parameters of this EdgeSearchQuery.  # noqa: E501
        :type: RelationsSearchParameters
        """

        self._parameters = parameters

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
        if issubclass(EdgeSearchQuery, dict):
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
        if not isinstance(other, EdgeSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
