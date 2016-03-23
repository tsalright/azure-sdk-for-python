# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IpSecurityRestriction(Model):
    """
    Represents an ip security restriction on a web app.

    :param ip_address: IP address the security restriction is valid for
    :type ip_address: str
    :param subnet_mask: Subnet mask for the range of IP addresses the
     restriction is valid for
    :type subnet_mask: str
    """ 

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'subnet_mask': {'key': 'subnetMask', 'type': 'str'},
    }

    def __init__(self, ip_address=None, subnet_mask=None, **kwargs):
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
