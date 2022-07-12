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

class DeviceProfileAlarm(object):
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
        'id': 'str',
        'alarm_type': 'str',
        'create_rules': 'dict(str, AlarmRule)',
        'clear_rule': 'AlarmRule',
        'propagate': 'bool',
        'propagate_to_owner': 'bool',
        'propagate_to_tenant': 'bool',
        'propagate_relation_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'alarm_type': 'alarmType',
        'create_rules': 'createRules',
        'clear_rule': 'clearRule',
        'propagate': 'propagate',
        'propagate_to_owner': 'propagateToOwner',
        'propagate_to_tenant': 'propagateToTenant',
        'propagate_relation_types': 'propagateRelationTypes'
    }

    def __init__(self, id=None, alarm_type=None, create_rules=None, clear_rule=None, propagate=None, propagate_to_owner=None, propagate_to_tenant=None, propagate_relation_types=None):  # noqa: E501
        """DeviceProfileAlarm - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._alarm_type = None
        self._create_rules = None
        self._clear_rule = None
        self._propagate = None
        self._propagate_to_owner = None
        self._propagate_to_tenant = None
        self._propagate_relation_types = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if create_rules is not None:
            self.create_rules = create_rules
        if clear_rule is not None:
            self.clear_rule = clear_rule
        if propagate is not None:
            self.propagate = propagate
        if propagate_to_owner is not None:
            self.propagate_to_owner = propagate_to_owner
        if propagate_to_tenant is not None:
            self.propagate_to_tenant = propagate_to_tenant
        if propagate_relation_types is not None:
            self.propagate_relation_types = propagate_relation_types

    @property
    def id(self):
        """Gets the id of this DeviceProfileAlarm.  # noqa: E501

        String value representing the alarm rule id  # noqa: E501

        :return: The id of this DeviceProfileAlarm.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceProfileAlarm.

        String value representing the alarm rule id  # noqa: E501

        :param id: The id of this DeviceProfileAlarm.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def alarm_type(self):
        """Gets the alarm_type of this DeviceProfileAlarm.  # noqa: E501

        String value representing type of the alarm  # noqa: E501

        :return: The alarm_type of this DeviceProfileAlarm.  # noqa: E501
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this DeviceProfileAlarm.

        String value representing type of the alarm  # noqa: E501

        :param alarm_type: The alarm_type of this DeviceProfileAlarm.  # noqa: E501
        :type: str
        """

        self._alarm_type = alarm_type

    @property
    def create_rules(self):
        """Gets the create_rules of this DeviceProfileAlarm.  # noqa: E501

        Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details  # noqa: E501

        :return: The create_rules of this DeviceProfileAlarm.  # noqa: E501
        :rtype: dict(str, AlarmRule)
        """
        return self._create_rules

    @create_rules.setter
    def create_rules(self, create_rules):
        """Sets the create_rules of this DeviceProfileAlarm.

        Complex JSON object representing create alarm rules. The unique create alarm rule can be created for each alarm severity type. There can be 5 create alarm rules configured per a single alarm type. See method implementation notes and AlarmRule model for more details  # noqa: E501

        :param create_rules: The create_rules of this DeviceProfileAlarm.  # noqa: E501
        :type: dict(str, AlarmRule)
        """

        self._create_rules = create_rules

    @property
    def clear_rule(self):
        """Gets the clear_rule of this DeviceProfileAlarm.  # noqa: E501


        :return: The clear_rule of this DeviceProfileAlarm.  # noqa: E501
        :rtype: AlarmRule
        """
        return self._clear_rule

    @clear_rule.setter
    def clear_rule(self, clear_rule):
        """Sets the clear_rule of this DeviceProfileAlarm.


        :param clear_rule: The clear_rule of this DeviceProfileAlarm.  # noqa: E501
        :type: AlarmRule
        """

        self._clear_rule = clear_rule

    @property
    def propagate(self):
        """Gets the propagate of this DeviceProfileAlarm.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to parent entities of alarm originator  # noqa: E501

        :return: The propagate of this DeviceProfileAlarm.  # noqa: E501
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        """Sets the propagate of this DeviceProfileAlarm.

        Propagation flag to specify if alarm should be propagated to parent entities of alarm originator  # noqa: E501

        :param propagate: The propagate of this DeviceProfileAlarm.  # noqa: E501
        :type: bool
        """

        self._propagate = propagate

    @property
    def propagate_to_owner(self):
        """Gets the propagate_to_owner of this DeviceProfileAlarm.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator  # noqa: E501

        :return: The propagate_to_owner of this DeviceProfileAlarm.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_to_owner

    @propagate_to_owner.setter
    def propagate_to_owner(self, propagate_to_owner):
        """Sets the propagate_to_owner of this DeviceProfileAlarm.

        Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator  # noqa: E501

        :param propagate_to_owner: The propagate_to_owner of this DeviceProfileAlarm.  # noqa: E501
        :type: bool
        """

        self._propagate_to_owner = propagate_to_owner

    @property
    def propagate_to_tenant(self):
        """Gets the propagate_to_tenant of this DeviceProfileAlarm.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to the tenant entity  # noqa: E501

        :return: The propagate_to_tenant of this DeviceProfileAlarm.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_to_tenant

    @propagate_to_tenant.setter
    def propagate_to_tenant(self, propagate_to_tenant):
        """Sets the propagate_to_tenant of this DeviceProfileAlarm.

        Propagation flag to specify if alarm should be propagated to the tenant entity  # noqa: E501

        :param propagate_to_tenant: The propagate_to_tenant of this DeviceProfileAlarm.  # noqa: E501
        :type: bool
        """

        self._propagate_to_tenant = propagate_to_tenant

    @property
    def propagate_relation_types(self):
        """Gets the propagate_relation_types of this DeviceProfileAlarm.  # noqa: E501

        JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.  # noqa: E501

        :return: The propagate_relation_types of this DeviceProfileAlarm.  # noqa: E501
        :rtype: list[str]
        """
        return self._propagate_relation_types

    @propagate_relation_types.setter
    def propagate_relation_types(self, propagate_relation_types):
        """Sets the propagate_relation_types of this DeviceProfileAlarm.

        JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.  # noqa: E501

        :param propagate_relation_types: The propagate_relation_types of this DeviceProfileAlarm.  # noqa: E501
        :type: list[str]
        """

        self._propagate_relation_types = propagate_relation_types

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
        if issubclass(DeviceProfileAlarm, dict):
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
        if not isinstance(other, DeviceProfileAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
