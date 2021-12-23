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

class LwM2mObject(object):
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
        'id': 'int',
        'key_id': 'str',
        'name': 'str',
        'multiple': 'bool',
        'mandatory': 'bool',
        'instances': 'list[LwM2mInstance]'
    }

    attribute_map = {
        'id': 'id',
        'key_id': 'keyId',
        'name': 'name',
        'multiple': 'multiple',
        'mandatory': 'mandatory',
        'instances': 'instances'
    }

    def __init__(self, id=None, key_id=None, name=None, multiple=None, mandatory=None, instances=None):  # noqa: E501
        """LwM2mObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._key_id = None
        self._name = None
        self._multiple = None
        self._mandatory = None
        self._instances = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if key_id is not None:
            self.key_id = key_id
        if name is not None:
            self.name = name
        if multiple is not None:
            self.multiple = multiple
        if mandatory is not None:
            self.mandatory = mandatory
        if instances is not None:
            self.instances = instances

    @property
    def id(self):
        """Gets the id of this LwM2mObject.  # noqa: E501

        LwM2M Object id.  # noqa: E501

        :return: The id of this LwM2mObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LwM2mObject.

        LwM2M Object id.  # noqa: E501

        :param id: The id of this LwM2mObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key_id(self):
        """Gets the key_id of this LwM2mObject.  # noqa: E501

        LwM2M Object key id.  # noqa: E501

        :return: The key_id of this LwM2mObject.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this LwM2mObject.

        LwM2M Object key id.  # noqa: E501

        :param key_id: The key_id of this LwM2mObject.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def name(self):
        """Gets the name of this LwM2mObject.  # noqa: E501

        LwM2M Object name.  # noqa: E501

        :return: The name of this LwM2mObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LwM2mObject.

        LwM2M Object name.  # noqa: E501

        :param name: The name of this LwM2mObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def multiple(self):
        """Gets the multiple of this LwM2mObject.  # noqa: E501

        LwM2M Object multiple.  # noqa: E501

        :return: The multiple of this LwM2mObject.  # noqa: E501
        :rtype: bool
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this LwM2mObject.

        LwM2M Object multiple.  # noqa: E501

        :param multiple: The multiple of this LwM2mObject.  # noqa: E501
        :type: bool
        """

        self._multiple = multiple

    @property
    def mandatory(self):
        """Gets the mandatory of this LwM2mObject.  # noqa: E501

        LwM2M Object mandatory.  # noqa: E501

        :return: The mandatory of this LwM2mObject.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this LwM2mObject.

        LwM2M Object mandatory.  # noqa: E501

        :param mandatory: The mandatory of this LwM2mObject.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def instances(self):
        """Gets the instances of this LwM2mObject.  # noqa: E501

        LwM2M Object instances.  # noqa: E501

        :return: The instances of this LwM2mObject.  # noqa: E501
        :rtype: list[LwM2mInstance]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this LwM2mObject.

        LwM2M Object instances.  # noqa: E501

        :param instances: The instances of this LwM2mObject.  # noqa: E501
        :type: list[LwM2mInstance]
        """

        self._instances = instances

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
        if issubclass(LwM2mObject, dict):
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
        if not isinstance(other, LwM2mObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
