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

class HomeDashboardInfo(object):
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
        'dashboard_id': 'DashboardId',
        'hide_dashboard_toolbar': 'bool'
    }

    attribute_map = {
        'dashboard_id': 'dashboardId',
        'hide_dashboard_toolbar': 'hideDashboardToolbar'
    }

    def __init__(self, dashboard_id=None, hide_dashboard_toolbar=None):  # noqa: E501
        """HomeDashboardInfo - a model defined in Swagger"""  # noqa: E501
        self._dashboard_id = None
        self._hide_dashboard_toolbar = None
        self.discriminator = None
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if hide_dashboard_toolbar is not None:
            self.hide_dashboard_toolbar = hide_dashboard_toolbar

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this HomeDashboardInfo.  # noqa: E501


        :return: The dashboard_id of this HomeDashboardInfo.  # noqa: E501
        :rtype: DashboardId
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this HomeDashboardInfo.


        :param dashboard_id: The dashboard_id of this HomeDashboardInfo.  # noqa: E501
        :type: DashboardId
        """

        self._dashboard_id = dashboard_id

    @property
    def hide_dashboard_toolbar(self):
        """Gets the hide_dashboard_toolbar of this HomeDashboardInfo.  # noqa: E501

        Hide dashboard toolbar flag. Useful for rendering dashboards on mobile.  # noqa: E501

        :return: The hide_dashboard_toolbar of this HomeDashboardInfo.  # noqa: E501
        :rtype: bool
        """
        return self._hide_dashboard_toolbar

    @hide_dashboard_toolbar.setter
    def hide_dashboard_toolbar(self, hide_dashboard_toolbar):
        """Sets the hide_dashboard_toolbar of this HomeDashboardInfo.

        Hide dashboard toolbar flag. Useful for rendering dashboards on mobile.  # noqa: E501

        :param hide_dashboard_toolbar: The hide_dashboard_toolbar of this HomeDashboardInfo.  # noqa: E501
        :type: bool
        """

        self._hide_dashboard_toolbar = hide_dashboard_toolbar

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
        if issubclass(HomeDashboardInfo, dict):
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
        if not isinstance(other, HomeDashboardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
