# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.networking.firewall.
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


class Inbound(VapiInterface):
    """
    The ``Inbound`` class provides methods to manage inbound firewall rules.
    This class was added in vSphere API 6.7 U1.
    """

    _VAPI_SERVICE_ID = 'com.vmware.appliance.networking.firewall.inbound'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InboundStub)

    class Policy(Enum):
        """
        ``Inbound.Policy`` class Defines firewall rule policies. This enumeration
        was added in vSphere API 6.7 U1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IGNORE = None
        """
        Drop packet with correpsonding address. This class attribute was added in
        vSphere API 6.7 U1.

        """
        ACCEPT = None
        """
        Allow packet with corresponding address. This class attribute was added in
        vSphere API 6.7 U1.

        """
        REJECT = None
        """
        Drop packet with corresponding address sending destination is not
        reachable. This class attribute was added in vSphere API 6.7 U1.

        """
        RETURN = None
        """
        Apply default or port-specific rules to packet with corresponding address.
        This class attribute was added in vSphere API 6.7 U1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Policy` instance.
            """
            Enum.__init__(string)

    Policy._set_values([
        Policy('IGNORE'),
        Policy('ACCEPT'),
        Policy('REJECT'),
        Policy('RETURN'),
    ])
    Policy._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.firewall.inbound.policy',
        Policy))


    class Rule(VapiStruct):
        """
        ``Inbound.Rule`` class Structure that defines a single address-based
        firewall rule. This class was added in vSphere API 6.7 U1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     prefix=None,
                     policy=None,
                     interface_name=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IPv4 or IPv6 address. This attribute was added in vSphere API 6.7
                U1.
            :type  prefix: :class:`long`
            :param prefix: CIDR prefix used to mask address. For example, an IPv4 prefix of 24
                ignores the low-order 8 bits of address. This attribute was added
                in vSphere API 6.7 U1.
            :type  policy: :class:`Inbound.Policy`
            :param policy: The allow or deny policy of this rule. This attribute was added in
                vSphere API 6.7 U1.
            :type  interface_name: :class:`str` or ``None``
            :param interface_name: The interface to which this rule applies. An empty string indicates
                that the rule applies to all interfaces. This attribute was added
                in vSphere API 6.7 U1.
            """
            self.address = address
            self.prefix = prefix
            self.policy = policy
            self.interface_name = interface_name
            VapiStruct.__init__(self)

    Rule._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.firewall.inbound.rule', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
            'policy': type.ReferenceType(__name__, 'Inbound.Policy'),
            'interface_name': type.OptionalType(type.StringType()),
        },
        Rule,
        False,
        None))



    def set(self,
            rules,
            ):
        """
        Set the ordered list of firewall rules to allow or deny traffic from
        one or more incoming IP addresses. This overwrites the existing
        firewall rules and creates a new rule list. Within the list of traffic
        rules, rules are processed in order of appearance, from top to bottom.
        For example, the list of rules can be as follows: 
        
        #. "address": "10.112.0.1", "prefix": 0, "interface_name":
           "\*","policy": "REJECT"
        "address": "10.112.0.1", "prefix": 0, "interface_name":
        "nic0","policy": "ACCEPT"
        
        In the above example, the first rule drops all packets originating from
        10.112.0.1 and
        the second rule accepts all packets originating from 10.112.0.1 only on
        nic0. In effect, the second rule is always ignored which is not
        desired, hence the order has to be swapped. When a connection matches a
        firewall rule, further processing for the connection stops, and the
        appliance ignores any additional firewall rules you have set. This
        method was added in vSphere API 6.7 U1.

        :type  rules: :class:`list` of :class:`Inbound.Rule`
        :param rules: List of address-based firewall rules.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'rules': rules,
                            })

    def get(self):
        """
        Get the ordered list of firewall rules. Within the list of traffic
        rules, rules are processed in order of appearance, from top to bottom.
        When a connection matches a firewall rule, further processing for the
        connection stops, and the appliance ignores any additional firewall
        rules you have set. This method was added in vSphere API 6.7 U1.


        :rtype: :class:`list` of :class:`Inbound.Rule`
        :return: List of address-based firewall rules.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class _InboundStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'rules': type.ListType(type.ReferenceType(__name__, 'Inbound.Rule')),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/networking/firewall/inbound',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/firewall/inbound',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Inbound.Rule')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'set': set_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.firewall.inbound',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Inbound': Inbound,
    }

