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

class DefaultTenantProfileConfiguration(object):
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
        'alarms_ttl_days': 'int',
        'default_storage_ttl_days': 'int',
        'max_assets': 'int',
        'max_created_alarms': 'int',
        'max_customers': 'int',
        'max_dp_storage_days': 'int',
        'max_dashboards': 'int',
        'max_devices': 'int',
        'max_emails': 'int',
        'max_js_executions': 'int',
        'max_ota_packages_in_bytes': 'int',
        'max_re_executions': 'int',
        'max_resources_in_bytes': 'int',
        'max_rule_chains': 'int',
        'max_rule_node_executions_per_message': 'int',
        'max_sms': 'int',
        'max_transport_data_points': 'int',
        'max_transport_messages': 'int',
        'max_users': 'int',
        'rpc_ttl_days': 'int',
        'transport_device_msg_rate_limit': 'str',
        'transport_device_telemetry_data_points_rate_limit': 'str',
        'transport_device_telemetry_msg_rate_limit': 'str',
        'transport_tenant_msg_rate_limit': 'str',
        'transport_tenant_telemetry_data_points_rate_limit': 'str',
        'transport_tenant_telemetry_msg_rate_limit': 'str',
        'warn_threshold': 'float'
    }

    attribute_map = {
        'alarms_ttl_days': 'alarmsTtlDays',
        'default_storage_ttl_days': 'defaultStorageTtlDays',
        'max_assets': 'maxAssets',
        'max_created_alarms': 'maxCreatedAlarms',
        'max_customers': 'maxCustomers',
        'max_dp_storage_days': 'maxDPStorageDays',
        'max_dashboards': 'maxDashboards',
        'max_devices': 'maxDevices',
        'max_emails': 'maxEmails',
        'max_js_executions': 'maxJSExecutions',
        'max_ota_packages_in_bytes': 'maxOtaPackagesInBytes',
        'max_re_executions': 'maxREExecutions',
        'max_resources_in_bytes': 'maxResourcesInBytes',
        'max_rule_chains': 'maxRuleChains',
        'max_rule_node_executions_per_message': 'maxRuleNodeExecutionsPerMessage',
        'max_sms': 'maxSms',
        'max_transport_data_points': 'maxTransportDataPoints',
        'max_transport_messages': 'maxTransportMessages',
        'max_users': 'maxUsers',
        'rpc_ttl_days': 'rpcTtlDays',
        'transport_device_msg_rate_limit': 'transportDeviceMsgRateLimit',
        'transport_device_telemetry_data_points_rate_limit': 'transportDeviceTelemetryDataPointsRateLimit',
        'transport_device_telemetry_msg_rate_limit': 'transportDeviceTelemetryMsgRateLimit',
        'transport_tenant_msg_rate_limit': 'transportTenantMsgRateLimit',
        'transport_tenant_telemetry_data_points_rate_limit': 'transportTenantTelemetryDataPointsRateLimit',
        'transport_tenant_telemetry_msg_rate_limit': 'transportTenantTelemetryMsgRateLimit',
        'warn_threshold': 'warnThreshold'
    }

    def __init__(self, alarms_ttl_days=None, default_storage_ttl_days=None, max_assets=None, max_created_alarms=None, max_customers=None, max_dp_storage_days=None, max_dashboards=None, max_devices=None, max_emails=None, max_js_executions=None, max_ota_packages_in_bytes=None, max_re_executions=None, max_resources_in_bytes=None, max_rule_chains=None, max_rule_node_executions_per_message=None, max_sms=None, max_transport_data_points=None, max_transport_messages=None, max_users=None, rpc_ttl_days=None, transport_device_msg_rate_limit=None, transport_device_telemetry_data_points_rate_limit=None, transport_device_telemetry_msg_rate_limit=None, transport_tenant_msg_rate_limit=None, transport_tenant_telemetry_data_points_rate_limit=None, transport_tenant_telemetry_msg_rate_limit=None, warn_threshold=None):  # noqa: E501
        """DefaultTenantProfileConfiguration - a model defined in Swagger"""  # noqa: E501
        self._alarms_ttl_days = None
        self._default_storage_ttl_days = None
        self._max_assets = None
        self._max_created_alarms = None
        self._max_customers = None
        self._max_dp_storage_days = None
        self._max_dashboards = None
        self._max_devices = None
        self._max_emails = None
        self._max_js_executions = None
        self._max_ota_packages_in_bytes = None
        self._max_re_executions = None
        self._max_resources_in_bytes = None
        self._max_rule_chains = None
        self._max_rule_node_executions_per_message = None
        self._max_sms = None
        self._max_transport_data_points = None
        self._max_transport_messages = None
        self._max_users = None
        self._rpc_ttl_days = None
        self._transport_device_msg_rate_limit = None
        self._transport_device_telemetry_data_points_rate_limit = None
        self._transport_device_telemetry_msg_rate_limit = None
        self._transport_tenant_msg_rate_limit = None
        self._transport_tenant_telemetry_data_points_rate_limit = None
        self._transport_tenant_telemetry_msg_rate_limit = None
        self._warn_threshold = None
        self.discriminator = None
        if alarms_ttl_days is not None:
            self.alarms_ttl_days = alarms_ttl_days
        if default_storage_ttl_days is not None:
            self.default_storage_ttl_days = default_storage_ttl_days
        if max_assets is not None:
            self.max_assets = max_assets
        if max_created_alarms is not None:
            self.max_created_alarms = max_created_alarms
        if max_customers is not None:
            self.max_customers = max_customers
        if max_dp_storage_days is not None:
            self.max_dp_storage_days = max_dp_storage_days
        if max_dashboards is not None:
            self.max_dashboards = max_dashboards
        if max_devices is not None:
            self.max_devices = max_devices
        if max_emails is not None:
            self.max_emails = max_emails
        if max_js_executions is not None:
            self.max_js_executions = max_js_executions
        if max_ota_packages_in_bytes is not None:
            self.max_ota_packages_in_bytes = max_ota_packages_in_bytes
        if max_re_executions is not None:
            self.max_re_executions = max_re_executions
        if max_resources_in_bytes is not None:
            self.max_resources_in_bytes = max_resources_in_bytes
        if max_rule_chains is not None:
            self.max_rule_chains = max_rule_chains
        if max_rule_node_executions_per_message is not None:
            self.max_rule_node_executions_per_message = max_rule_node_executions_per_message
        if max_sms is not None:
            self.max_sms = max_sms
        if max_transport_data_points is not None:
            self.max_transport_data_points = max_transport_data_points
        if max_transport_messages is not None:
            self.max_transport_messages = max_transport_messages
        if max_users is not None:
            self.max_users = max_users
        if rpc_ttl_days is not None:
            self.rpc_ttl_days = rpc_ttl_days
        if transport_device_msg_rate_limit is not None:
            self.transport_device_msg_rate_limit = transport_device_msg_rate_limit
        if transport_device_telemetry_data_points_rate_limit is not None:
            self.transport_device_telemetry_data_points_rate_limit = transport_device_telemetry_data_points_rate_limit
        if transport_device_telemetry_msg_rate_limit is not None:
            self.transport_device_telemetry_msg_rate_limit = transport_device_telemetry_msg_rate_limit
        if transport_tenant_msg_rate_limit is not None:
            self.transport_tenant_msg_rate_limit = transport_tenant_msg_rate_limit
        if transport_tenant_telemetry_data_points_rate_limit is not None:
            self.transport_tenant_telemetry_data_points_rate_limit = transport_tenant_telemetry_data_points_rate_limit
        if transport_tenant_telemetry_msg_rate_limit is not None:
            self.transport_tenant_telemetry_msg_rate_limit = transport_tenant_telemetry_msg_rate_limit
        if warn_threshold is not None:
            self.warn_threshold = warn_threshold

    @property
    def alarms_ttl_days(self):
        """Gets the alarms_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The alarms_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._alarms_ttl_days

    @alarms_ttl_days.setter
    def alarms_ttl_days(self, alarms_ttl_days):
        """Sets the alarms_ttl_days of this DefaultTenantProfileConfiguration.


        :param alarms_ttl_days: The alarms_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._alarms_ttl_days = alarms_ttl_days

    @property
    def default_storage_ttl_days(self):
        """Gets the default_storage_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The default_storage_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._default_storage_ttl_days

    @default_storage_ttl_days.setter
    def default_storage_ttl_days(self, default_storage_ttl_days):
        """Sets the default_storage_ttl_days of this DefaultTenantProfileConfiguration.


        :param default_storage_ttl_days: The default_storage_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._default_storage_ttl_days = default_storage_ttl_days

    @property
    def max_assets(self):
        """Gets the max_assets of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_assets of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_assets

    @max_assets.setter
    def max_assets(self, max_assets):
        """Sets the max_assets of this DefaultTenantProfileConfiguration.


        :param max_assets: The max_assets of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_assets = max_assets

    @property
    def max_created_alarms(self):
        """Gets the max_created_alarms of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_created_alarms of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_created_alarms

    @max_created_alarms.setter
    def max_created_alarms(self, max_created_alarms):
        """Sets the max_created_alarms of this DefaultTenantProfileConfiguration.


        :param max_created_alarms: The max_created_alarms of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_created_alarms = max_created_alarms

    @property
    def max_customers(self):
        """Gets the max_customers of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_customers of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_customers

    @max_customers.setter
    def max_customers(self, max_customers):
        """Sets the max_customers of this DefaultTenantProfileConfiguration.


        :param max_customers: The max_customers of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_customers = max_customers

    @property
    def max_dp_storage_days(self):
        """Gets the max_dp_storage_days of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_dp_storage_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_dp_storage_days

    @max_dp_storage_days.setter
    def max_dp_storage_days(self, max_dp_storage_days):
        """Sets the max_dp_storage_days of this DefaultTenantProfileConfiguration.


        :param max_dp_storage_days: The max_dp_storage_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_dp_storage_days = max_dp_storage_days

    @property
    def max_dashboards(self):
        """Gets the max_dashboards of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_dashboards of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_dashboards

    @max_dashboards.setter
    def max_dashboards(self, max_dashboards):
        """Sets the max_dashboards of this DefaultTenantProfileConfiguration.


        :param max_dashboards: The max_dashboards of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_dashboards = max_dashboards

    @property
    def max_devices(self):
        """Gets the max_devices of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_devices of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_devices

    @max_devices.setter
    def max_devices(self, max_devices):
        """Sets the max_devices of this DefaultTenantProfileConfiguration.


        :param max_devices: The max_devices of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_devices = max_devices

    @property
    def max_emails(self):
        """Gets the max_emails of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_emails of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_emails

    @max_emails.setter
    def max_emails(self, max_emails):
        """Sets the max_emails of this DefaultTenantProfileConfiguration.


        :param max_emails: The max_emails of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_emails = max_emails

    @property
    def max_js_executions(self):
        """Gets the max_js_executions of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_js_executions of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_js_executions

    @max_js_executions.setter
    def max_js_executions(self, max_js_executions):
        """Sets the max_js_executions of this DefaultTenantProfileConfiguration.


        :param max_js_executions: The max_js_executions of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_js_executions = max_js_executions

    @property
    def max_ota_packages_in_bytes(self):
        """Gets the max_ota_packages_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_ota_packages_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_ota_packages_in_bytes

    @max_ota_packages_in_bytes.setter
    def max_ota_packages_in_bytes(self, max_ota_packages_in_bytes):
        """Sets the max_ota_packages_in_bytes of this DefaultTenantProfileConfiguration.


        :param max_ota_packages_in_bytes: The max_ota_packages_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_ota_packages_in_bytes = max_ota_packages_in_bytes

    @property
    def max_re_executions(self):
        """Gets the max_re_executions of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_re_executions of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_re_executions

    @max_re_executions.setter
    def max_re_executions(self, max_re_executions):
        """Sets the max_re_executions of this DefaultTenantProfileConfiguration.


        :param max_re_executions: The max_re_executions of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_re_executions = max_re_executions

    @property
    def max_resources_in_bytes(self):
        """Gets the max_resources_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_resources_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_resources_in_bytes

    @max_resources_in_bytes.setter
    def max_resources_in_bytes(self, max_resources_in_bytes):
        """Sets the max_resources_in_bytes of this DefaultTenantProfileConfiguration.


        :param max_resources_in_bytes: The max_resources_in_bytes of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_resources_in_bytes = max_resources_in_bytes

    @property
    def max_rule_chains(self):
        """Gets the max_rule_chains of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_rule_chains of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_rule_chains

    @max_rule_chains.setter
    def max_rule_chains(self, max_rule_chains):
        """Sets the max_rule_chains of this DefaultTenantProfileConfiguration.


        :param max_rule_chains: The max_rule_chains of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_rule_chains = max_rule_chains

    @property
    def max_rule_node_executions_per_message(self):
        """Gets the max_rule_node_executions_per_message of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_rule_node_executions_per_message of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_rule_node_executions_per_message

    @max_rule_node_executions_per_message.setter
    def max_rule_node_executions_per_message(self, max_rule_node_executions_per_message):
        """Sets the max_rule_node_executions_per_message of this DefaultTenantProfileConfiguration.


        :param max_rule_node_executions_per_message: The max_rule_node_executions_per_message of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_rule_node_executions_per_message = max_rule_node_executions_per_message

    @property
    def max_sms(self):
        """Gets the max_sms of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_sms of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_sms

    @max_sms.setter
    def max_sms(self, max_sms):
        """Sets the max_sms of this DefaultTenantProfileConfiguration.


        :param max_sms: The max_sms of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_sms = max_sms

    @property
    def max_transport_data_points(self):
        """Gets the max_transport_data_points of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_transport_data_points of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_transport_data_points

    @max_transport_data_points.setter
    def max_transport_data_points(self, max_transport_data_points):
        """Sets the max_transport_data_points of this DefaultTenantProfileConfiguration.


        :param max_transport_data_points: The max_transport_data_points of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_transport_data_points = max_transport_data_points

    @property
    def max_transport_messages(self):
        """Gets the max_transport_messages of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_transport_messages of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_transport_messages

    @max_transport_messages.setter
    def max_transport_messages(self, max_transport_messages):
        """Sets the max_transport_messages of this DefaultTenantProfileConfiguration.


        :param max_transport_messages: The max_transport_messages of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_transport_messages = max_transport_messages

    @property
    def max_users(self):
        """Gets the max_users of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The max_users of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this DefaultTenantProfileConfiguration.


        :param max_users: The max_users of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._max_users = max_users

    @property
    def rpc_ttl_days(self):
        """Gets the rpc_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The rpc_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._rpc_ttl_days

    @rpc_ttl_days.setter
    def rpc_ttl_days(self, rpc_ttl_days):
        """Sets the rpc_ttl_days of this DefaultTenantProfileConfiguration.


        :param rpc_ttl_days: The rpc_ttl_days of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: int
        """

        self._rpc_ttl_days = rpc_ttl_days

    @property
    def transport_device_msg_rate_limit(self):
        """Gets the transport_device_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_device_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_device_msg_rate_limit

    @transport_device_msg_rate_limit.setter
    def transport_device_msg_rate_limit(self, transport_device_msg_rate_limit):
        """Sets the transport_device_msg_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_device_msg_rate_limit: The transport_device_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_device_msg_rate_limit = transport_device_msg_rate_limit

    @property
    def transport_device_telemetry_data_points_rate_limit(self):
        """Gets the transport_device_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_device_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_device_telemetry_data_points_rate_limit

    @transport_device_telemetry_data_points_rate_limit.setter
    def transport_device_telemetry_data_points_rate_limit(self, transport_device_telemetry_data_points_rate_limit):
        """Sets the transport_device_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_device_telemetry_data_points_rate_limit: The transport_device_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_device_telemetry_data_points_rate_limit = transport_device_telemetry_data_points_rate_limit

    @property
    def transport_device_telemetry_msg_rate_limit(self):
        """Gets the transport_device_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_device_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_device_telemetry_msg_rate_limit

    @transport_device_telemetry_msg_rate_limit.setter
    def transport_device_telemetry_msg_rate_limit(self, transport_device_telemetry_msg_rate_limit):
        """Sets the transport_device_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_device_telemetry_msg_rate_limit: The transport_device_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_device_telemetry_msg_rate_limit = transport_device_telemetry_msg_rate_limit

    @property
    def transport_tenant_msg_rate_limit(self):
        """Gets the transport_tenant_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_tenant_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_tenant_msg_rate_limit

    @transport_tenant_msg_rate_limit.setter
    def transport_tenant_msg_rate_limit(self, transport_tenant_msg_rate_limit):
        """Sets the transport_tenant_msg_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_tenant_msg_rate_limit: The transport_tenant_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_tenant_msg_rate_limit = transport_tenant_msg_rate_limit

    @property
    def transport_tenant_telemetry_data_points_rate_limit(self):
        """Gets the transport_tenant_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_tenant_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_tenant_telemetry_data_points_rate_limit

    @transport_tenant_telemetry_data_points_rate_limit.setter
    def transport_tenant_telemetry_data_points_rate_limit(self, transport_tenant_telemetry_data_points_rate_limit):
        """Sets the transport_tenant_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_tenant_telemetry_data_points_rate_limit: The transport_tenant_telemetry_data_points_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_tenant_telemetry_data_points_rate_limit = transport_tenant_telemetry_data_points_rate_limit

    @property
    def transport_tenant_telemetry_msg_rate_limit(self):
        """Gets the transport_tenant_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The transport_tenant_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._transport_tenant_telemetry_msg_rate_limit

    @transport_tenant_telemetry_msg_rate_limit.setter
    def transport_tenant_telemetry_msg_rate_limit(self, transport_tenant_telemetry_msg_rate_limit):
        """Sets the transport_tenant_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.


        :param transport_tenant_telemetry_msg_rate_limit: The transport_tenant_telemetry_msg_rate_limit of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: str
        """

        self._transport_tenant_telemetry_msg_rate_limit = transport_tenant_telemetry_msg_rate_limit

    @property
    def warn_threshold(self):
        """Gets the warn_threshold of this DefaultTenantProfileConfiguration.  # noqa: E501


        :return: The warn_threshold of this DefaultTenantProfileConfiguration.  # noqa: E501
        :rtype: float
        """
        return self._warn_threshold

    @warn_threshold.setter
    def warn_threshold(self, warn_threshold):
        """Sets the warn_threshold of this DefaultTenantProfileConfiguration.


        :param warn_threshold: The warn_threshold of this DefaultTenantProfileConfiguration.  # noqa: E501
        :type: float
        """

        self._warn_threshold = warn_threshold

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
        if issubclass(DefaultTenantProfileConfiguration, dict):
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
        if not isinstance(other, DefaultTenantProfileConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
