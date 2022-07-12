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

class Dashboard(object):
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
        'external_id': 'DashboardId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'owner_id': 'EntityId',
        'title': 'str',
        'image': 'str',
        'assigned_customers': 'list[ShortCustomerInfo]',
        'mobile_hide': 'bool',
        'mobile_order': 'int',
        'name': 'str',
        'configuration': 'JsonNode'
    }

    attribute_map = {
        'external_id': 'externalId',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'owner_id': 'ownerId',
        'title': 'title',
        'image': 'image',
        'assigned_customers': 'assignedCustomers',
        'mobile_hide': 'mobileHide',
        'mobile_order': 'mobileOrder',
        'name': 'name',
        'configuration': 'configuration'
    }

    def __init__(self, external_id=None, created_time=None, tenant_id=None, customer_id=None, owner_id=None, title=None, image=None, assigned_customers=None, mobile_hide=None, mobile_order=None, name=None, configuration=None):  # noqa: E501
        """Dashboard - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._owner_id = None
        self._title = None
        self._image = None
        self._assigned_customers = None
        self._mobile_hide = None
        self._mobile_order = None
        self._name = None
        self._configuration = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if owner_id is not None:
            self.owner_id = owner_id
        if title is not None:
            self.title = title
        if image is not None:
            self.image = image
        if assigned_customers is not None:
            self.assigned_customers = assigned_customers
        if mobile_hide is not None:
            self.mobile_hide = mobile_hide
        if mobile_order is not None:
            self.mobile_order = mobile_order
        if name is not None:
            self.name = name
        if configuration is not None:
            self.configuration = configuration

    @property
    def external_id(self):
        """Gets the external_id of this Dashboard.  # noqa: E501


        :return: The external_id of this Dashboard.  # noqa: E501
        :rtype: DashboardId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Dashboard.


        :param external_id: The external_id of this Dashboard.  # noqa: E501
        :type: DashboardId
        """

        self._external_id = external_id

    @property
    def created_time(self):
        """Gets the created_time of this Dashboard.  # noqa: E501

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :return: The created_time of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Dashboard.

        Timestamp of the dashboard creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Dashboard.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Dashboard.  # noqa: E501


        :return: The tenant_id of this Dashboard.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Dashboard.


        :param tenant_id: The tenant_id of this Dashboard.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Dashboard.  # noqa: E501


        :return: The customer_id of this Dashboard.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Dashboard.


        :param customer_id: The customer_id of this Dashboard.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def owner_id(self):
        """Gets the owner_id of this Dashboard.  # noqa: E501


        :return: The owner_id of this Dashboard.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Dashboard.


        :param owner_id: The owner_id of this Dashboard.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def title(self):
        """Gets the title of this Dashboard.  # noqa: E501

        Title of the dashboard.  # noqa: E501

        :return: The title of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Dashboard.

        Title of the dashboard.  # noqa: E501

        :param title: The title of this Dashboard.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def image(self):
        """Gets the image of this Dashboard.  # noqa: E501

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :return: The image of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Dashboard.

        Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.  # noqa: E501

        :param image: The image of this Dashboard.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def assigned_customers(self):
        """Gets the assigned_customers of this Dashboard.  # noqa: E501

        List of assigned customers with their info.  # noqa: E501

        :return: The assigned_customers of this Dashboard.  # noqa: E501
        :rtype: list[ShortCustomerInfo]
        """
        return self._assigned_customers

    @assigned_customers.setter
    def assigned_customers(self, assigned_customers):
        """Sets the assigned_customers of this Dashboard.

        List of assigned customers with their info.  # noqa: E501

        :param assigned_customers: The assigned_customers of this Dashboard.  # noqa: E501
        :type: list[ShortCustomerInfo]
        """

        self._assigned_customers = assigned_customers

    @property
    def mobile_hide(self):
        """Gets the mobile_hide of this Dashboard.  # noqa: E501

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :return: The mobile_hide of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._mobile_hide

    @mobile_hide.setter
    def mobile_hide(self, mobile_hide):
        """Sets the mobile_hide of this Dashboard.

        Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.  # noqa: E501

        :param mobile_hide: The mobile_hide of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._mobile_hide = mobile_hide

    @property
    def mobile_order(self):
        """Gets the mobile_order of this Dashboard.  # noqa: E501

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :return: The mobile_order of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._mobile_order

    @mobile_order.setter
    def mobile_order(self, mobile_order):
        """Sets the mobile_order of this Dashboard.

        Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications  # noqa: E501

        :param mobile_order: The mobile_order of this Dashboard.  # noqa: E501
        :type: int
        """

        self._mobile_order = mobile_order

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.

        Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.  # noqa: E501

        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def configuration(self):
        """Gets the configuration of this Dashboard.  # noqa: E501


        :return: The configuration of this Dashboard.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this Dashboard.


        :param configuration: The configuration of this Dashboard.  # noqa: E501
        :type: JsonNode
        """

        self._configuration = configuration

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
        if issubclass(Dashboard, dict):
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
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
