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

class ContactBasedobject(object):
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
        'additional_info': 'JsonNode',
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'created_time': 'int',
        'email': 'str',
        'id': 'object',
        'name': 'str',
        'phone': 'str',
        'state': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'address': 'address',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'created_time': 'createdTime',
        'email': 'email',
        'id': 'id',
        'name': 'name',
        'phone': 'phone',
        'state': 'state',
        'zip': 'zip'
    }

    def __init__(self, additional_info=None, address=None, address2=None, city=None, country=None, created_time=None, email=None, id=None, name=None, phone=None, state=None, zip=None):  # noqa: E501
        """ContactBasedobject - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._address = None
        self._address2 = None
        self._city = None
        self._country = None
        self._created_time = None
        self._email = None
        self._id = None
        self._name = None
        self._phone = None
        self._state = None
        self._zip = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if created_time is not None:
            self.created_time = created_time
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip

    @property
    def additional_info(self):
        """Gets the additional_info of this ContactBasedobject.  # noqa: E501


        :return: The additional_info of this ContactBasedobject.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ContactBasedobject.


        :param additional_info: The additional_info of this ContactBasedobject.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def address(self):
        """Gets the address of this ContactBasedobject.  # noqa: E501


        :return: The address of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ContactBasedobject.


        :param address: The address of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this ContactBasedobject.  # noqa: E501


        :return: The address2 of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ContactBasedobject.


        :param address2: The address2 of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this ContactBasedobject.  # noqa: E501


        :return: The city of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactBasedobject.


        :param city: The city of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this ContactBasedobject.  # noqa: E501


        :return: The country of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ContactBasedobject.


        :param country: The country of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def created_time(self):
        """Gets the created_time of this ContactBasedobject.  # noqa: E501


        :return: The created_time of this ContactBasedobject.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ContactBasedobject.


        :param created_time: The created_time of this ContactBasedobject.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def email(self):
        """Gets the email of this ContactBasedobject.  # noqa: E501


        :return: The email of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactBasedobject.


        :param email: The email of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this ContactBasedobject.  # noqa: E501


        :return: The id of this ContactBasedobject.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactBasedobject.


        :param id: The id of this ContactBasedobject.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ContactBasedobject.  # noqa: E501


        :return: The name of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactBasedobject.


        :param name: The name of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this ContactBasedobject.  # noqa: E501


        :return: The phone of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactBasedobject.


        :param phone: The phone of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """Gets the state of this ContactBasedobject.  # noqa: E501


        :return: The state of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ContactBasedobject.


        :param state: The state of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this ContactBasedobject.  # noqa: E501


        :return: The zip of this ContactBasedobject.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this ContactBasedobject.


        :param zip: The zip of this ContactBasedobject.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(ContactBasedobject, dict):
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
        if not isinstance(other, ContactBasedobject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
