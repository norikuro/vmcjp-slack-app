# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.transport_zones.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Status(VapiInterface):
    """
    
    """
    GET_0_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.get_0`.

    """
    GET_0_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.get_0`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def get(self):
        """
        Get high-level summary of a transport zone. The service layer does not
        support source = realtime or cached.


        :rtype: :class:`com.vmware.nsx.model_client.HeatMapTransportNodesAggregateStatus`
        :return: com.vmware.nsx.model.HeatMapTransportNodesAggregateStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get', None)

    def get_0(self,
              zone_id,
              source=None,
              ):
        """
        Get high-level summary of a transport zone

        :type  zone_id: :class:`str`
        :param zone_id: ID of transport zone (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.HeatMapTransportZoneStatus`
        :return: com.vmware.nsx.model.HeatMapTransportZoneStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get_0',
                            {
                            'zone_id': zone_id,
                            'source': source,
                            })
class Summary(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SummaryStub)


    def get(self,
            zone_id,
            ):
        """
        Returns information about a specified transport zone, including the
        number of logical switches in the transport zone, number of logical
        spitch ports assigned to the transport zone, and number of transport
        nodes in the transport zone.

        :type  zone_id: :class:`str`
        :param zone_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportZoneStatus`
        :return: com.vmware.nsx.model.TransportZoneStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'zone_id': zone_id,
                            })
class TransportNodeStatus(VapiInterface):
    """
    
    """
    GETALL_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`TransportNodeStatus.getall`.

    """
    GETALL_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`TransportNodeStatus.getall`.

    """
    GETALL_STATUS_UP = "UP"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.getall`.

    """
    GETALL_STATUS_DOWN = "DOWN"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.getall`.

    """
    GETALL_STATUS_DEGRADED = "DEGRADED"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.getall`.

    """
    GETALL_STATUS_UNKNOWN = "UNKNOWN"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.getall`.

    """
    LIST_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`TransportNodeStatus.list`.

    """
    LIST_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`TransportNodeStatus.list`.

    """
    LIST_STATUS_UP = "UP"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.list`.

    """
    LIST_STATUS_DOWN = "DOWN"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.list`.

    """
    LIST_STATUS_DEGRADED = "DEGRADED"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.list`.

    """
    LIST_STATUS_UNKNOWN = "UNKNOWN"
    """
    Possible value for ``status`` of method :func:`TransportNodeStatus.list`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TransportNodeStatusStub)


    def getall(self,
               cursor=None,
               included_fields=None,
               page_size=None,
               sort_ascending=None,
               sort_by=None,
               source=None,
               status=None,
               ):
        """
        Read status of all the transport nodes

        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  status: :class:`str` or ``None``
        :param status: Transport node (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeStatusListResult`
        :return: com.vmware.nsx.model.TransportNodeStatusListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('getall',
                            {
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'status': status,
                            })

    def list(self,
             zone_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             source=None,
             status=None,
             ):
        """
        Read status of transport nodes in a transport zone

        :type  zone_id: :class:`str`
        :param zone_id: ID of transport zone (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  status: :class:`str` or ``None``
        :param status: Transport node (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeStatusListResult`
        :return: com.vmware.nsx.model.TransportNodeStatusListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'zone_id': zone_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'status': status,
                            })
class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-zones/status',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        get_0_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-zones/{zone-id}/status',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
                'source': 'source',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'HeatMapTransportNodesAggregateStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'HeatMapTransportZoneStatus'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_zones.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SummaryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-zones/{zone-id}/summary',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportZoneStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_zones.summary',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TransportNodeStatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for getall operation
        getall_input_type = type.StructType('operation-input', {
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'status': type.OptionalType(type.StringType()),
        })
        getall_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        getall_input_value_validator_list = [
        ]
        getall_output_validator_list = [
        ]
        getall_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-zones/transport-node-status',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'status': 'status',
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'zone_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'status': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-zones/{zone-id}/transport-node-status',
            path_variables={
                'zone_id': 'zone-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'status': 'status',
            }
        )

        operations = {
            'getall': {
                'input_type': getall_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeStatusListResult'),
                'errors': getall_error_dict,
                'input_value_validator_list': getall_input_value_validator_list,
                'output_validator_list': getall_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeStatusListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'getall': getall_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_zones.transport_node_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Status': Status,
        'Summary': Summary,
        'TransportNodeStatus': TransportNodeStatus,
    }

