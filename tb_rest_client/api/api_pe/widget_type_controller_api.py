# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class WidgetTypeControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_widget_type_using_delete(self, widget_type_id, **kwargs):  # noqa: E501
        """Delete widget type (deleteWidgetType)  # noqa: E501

        Deletes the  Widget Type. Referencing non-existing Widget Type Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widget_type_using_delete(widget_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widget_type_id: A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_widget_type_using_delete_with_http_info(widget_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_widget_type_using_delete_with_http_info(widget_type_id, **kwargs)  # noqa: E501
            return data

    def delete_widget_type_using_delete_with_http_info(self, widget_type_id, **kwargs):  # noqa: E501
        """Delete widget type (deleteWidgetType)  # noqa: E501

        Deletes the  Widget Type. Referencing non-existing Widget Type Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_widget_type_using_delete_with_http_info(widget_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widget_type_id: A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widget_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_widget_type_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widget_type_id' is set
        if ('widget_type_id' not in params or
                params['widget_type_id'] is None):
            raise ValueError("Missing the required parameter `widget_type_id` when calling `delete_widget_type_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widget_type_id' in params:
            path_params['widgetTypeId'] = params['widget_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetType/{widgetTypeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundle_widget_types_details_using_get(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get all Widget types details for specified Bundle (getBundleWidgetTypes)  # noqa: E501

        Returns an array of Widget Type Details objects that belong to specified Widget Bundle.Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_details_using_get(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetTypeDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundle_widget_types_details_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundle_widget_types_details_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
            return data

    def get_bundle_widget_types_details_using_get_with_http_info(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get all Widget types details for specified Bundle (getBundleWidgetTypes)  # noqa: E501

        Returns an array of Widget Type Details objects that belong to specified Widget Bundle.Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_details_using_get_with_http_info(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetTypeDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_system', 'bundle_alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundle_widget_types_details_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'is_system' is set
        if ('is_system' not in params or
                params['is_system'] is None):
            raise ValueError("Missing the required parameter `is_system` when calling `get_bundle_widget_types_details_using_get`")  # noqa: E501
        # verify the required parameter 'bundle_alias' is set
        if ('bundle_alias' not in params or
                params['bundle_alias'] is None):
            raise ValueError("Missing the required parameter `bundle_alias` when calling `get_bundle_widget_types_details_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_system' in params:
            query_params.append(('isSystem', params['is_system']))  # noqa: E501
        if 'bundle_alias' in params:
            query_params.append(('bundleAlias', params['bundle_alias']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetTypesDetails{?bundleAlias,isSystem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WidgetTypeDetails]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundle_widget_types_infos_using_get(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get Widget Type Info objects (getBundleWidgetTypesInfos)  # noqa: E501

        Get the Widget Type Info objects based on the provided parameters. Widget Type Info is a lightweight object that represents Widget Type but does not contain the heavyweight widget descriptor JSON  Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_infos_using_get(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetTypeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundle_widget_types_infos_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundle_widget_types_infos_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
            return data

    def get_bundle_widget_types_infos_using_get_with_http_info(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get Widget Type Info objects (getBundleWidgetTypesInfos)  # noqa: E501

        Get the Widget Type Info objects based on the provided parameters. Widget Type Info is a lightweight object that represents Widget Type but does not contain the heavyweight widget descriptor JSON  Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_infos_using_get_with_http_info(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetTypeInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_system', 'bundle_alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundle_widget_types_infos_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'is_system' is set
        if ('is_system' not in params or
                params['is_system'] is None):
            raise ValueError("Missing the required parameter `is_system` when calling `get_bundle_widget_types_infos_using_get`")  # noqa: E501
        # verify the required parameter 'bundle_alias' is set
        if ('bundle_alias' not in params or
                params['bundle_alias'] is None):
            raise ValueError("Missing the required parameter `bundle_alias` when calling `get_bundle_widget_types_infos_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_system' in params:
            query_params.append(('isSystem', params['is_system']))  # noqa: E501
        if 'bundle_alias' in params:
            query_params.append(('bundleAlias', params['bundle_alias']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetTypesInfos{?bundleAlias,isSystem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WidgetTypeInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundle_widget_types_using_get(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get all Widget types for specified Bundle (getBundleWidgetTypes)  # noqa: E501

        Returns an array of Widget Type objects that belong to specified Widget Bundle.Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_using_get(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundle_widget_types_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundle_widget_types_using_get_with_http_info(is_system, bundle_alias, **kwargs)  # noqa: E501
            return data

    def get_bundle_widget_types_using_get_with_http_info(self, is_system, bundle_alias, **kwargs):  # noqa: E501
        """Get all Widget types for specified Bundle (getBundleWidgetTypes)  # noqa: E501

        Returns an array of Widget Type objects that belong to specified Widget Bundle.Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundle_widget_types_using_get_with_http_info(is_system, bundle_alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :return: list[WidgetType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_system', 'bundle_alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundle_widget_types_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'is_system' is set
        if ('is_system' not in params or
                params['is_system'] is None):
            raise ValueError("Missing the required parameter `is_system` when calling `get_bundle_widget_types_using_get`")  # noqa: E501
        # verify the required parameter 'bundle_alias' is set
        if ('bundle_alias' not in params or
                params['bundle_alias'] is None):
            raise ValueError("Missing the required parameter `bundle_alias` when calling `get_bundle_widget_types_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_system' in params:
            query_params.append(('isSystem', params['is_system']))  # noqa: E501
        if 'bundle_alias' in params:
            query_params.append(('bundleAlias', params['bundle_alias']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetTypes{?bundleAlias,isSystem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WidgetType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widget_type_by_id_using_get(self, widget_type_id, **kwargs):  # noqa: E501
        """Get Widget Type Details (getWidgetTypeById)  # noqa: E501

        Get the Widget Type Details based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget_type_by_id_using_get(widget_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widget_type_id: A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: WidgetTypeDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widget_type_by_id_using_get_with_http_info(widget_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widget_type_by_id_using_get_with_http_info(widget_type_id, **kwargs)  # noqa: E501
            return data

    def get_widget_type_by_id_using_get_with_http_info(self, widget_type_id, **kwargs):  # noqa: E501
        """Get Widget Type Details (getWidgetTypeById)  # noqa: E501

        Get the Widget Type Details based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget_type_by_id_using_get_with_http_info(widget_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str widget_type_id: A string value representing the widget type id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: WidgetTypeDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['widget_type_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widget_type_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'widget_type_id' is set
        if ('widget_type_id' not in params or
                params['widget_type_id'] is None):
            raise ValueError("Missing the required parameter `widget_type_id` when calling `get_widget_type_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'widget_type_id' in params:
            path_params['widgetTypeId'] = params['widget_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetType/{widgetTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetTypeDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_widget_type_using_get(self, is_system, bundle_alias, alias, **kwargs):  # noqa: E501
        """Get Widget Type (getWidgetType)  # noqa: E501

        Get the Widget Type based on the provided parameters. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.  Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget_type_using_get(is_system, bundle_alias, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :param str alias: Widget Type alias (required)
        :return: WidgetType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_widget_type_using_get_with_http_info(is_system, bundle_alias, alias, **kwargs)  # noqa: E501
        else:
            (data) = self.get_widget_type_using_get_with_http_info(is_system, bundle_alias, alias, **kwargs)  # noqa: E501
            return data

    def get_widget_type_using_get_with_http_info(self, is_system, bundle_alias, alias, **kwargs):  # noqa: E501
        """Get Widget Type (getWidgetType)  # noqa: E501

        Get the Widget Type based on the provided parameters. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.  Available for any authorized user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_widget_type_using_get_with_http_info(is_system, bundle_alias, alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_system: System or Tenant (required)
        :param str bundle_alias: Widget Bundle alias (required)
        :param str alias: Widget Type alias (required)
        :return: WidgetType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_system', 'bundle_alias', 'alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_widget_type_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'is_system' is set
        if ('is_system' not in params or
                params['is_system'] is None):
            raise ValueError("Missing the required parameter `is_system` when calling `get_widget_type_using_get`")  # noqa: E501
        # verify the required parameter 'bundle_alias' is set
        if ('bundle_alias' not in params or
                params['bundle_alias'] is None):
            raise ValueError("Missing the required parameter `bundle_alias` when calling `get_widget_type_using_get`")  # noqa: E501
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `get_widget_type_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_system' in params:
            query_params.append(('isSystem', params['is_system']))  # noqa: E501
        if 'bundle_alias' in params:
            query_params.append(('bundleAlias', params['bundle_alias']))  # noqa: E501
        if 'alias' in params:
            query_params.append(('alias', params['alias']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetType{?alias,bundleAlias,isSystem}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_widget_type_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Widget Type (saveWidgetType)  # noqa: E501

        Create or update the Widget Type. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. When creating the Widget Type, platform generates Widget Type Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Type Id will be present in the response. Specify existing Widget Type id to update the Widget Type. Referencing non-existing Widget Type Id will cause 'Not Found' error.  Widget Type alias is unique in the scope of Widget Bundle. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create request is sent by user with 'SYS_ADMIN' authority.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widget_type_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetTypeDetails body:
        :return: WidgetTypeDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_widget_type_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_widget_type_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_widget_type_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Widget Type (saveWidgetType)  # noqa: E501

        Create or update the Widget Type. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. When creating the Widget Type, platform generates Widget Type Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Type Id will be present in the response. Specify existing Widget Type id to update the Widget Type. Referencing non-existing Widget Type Id will cause 'Not Found' error.  Widget Type alias is unique in the scope of Widget Bundle. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create request is sent by user with 'SYS_ADMIN' authority.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_widget_type_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WidgetTypeDetails body:
        :return: WidgetTypeDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_widget_type_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/widgetType', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WidgetTypeDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
