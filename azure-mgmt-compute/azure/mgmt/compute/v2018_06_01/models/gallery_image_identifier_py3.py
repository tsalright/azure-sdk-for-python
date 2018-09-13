# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GalleryImageIdentifier(Model):
    """This is the gallery image identifier.

    All required parameters must be populated in order to send to Azure.

    :param publisher: Required. The gallery image publisher name.
    :type publisher: str
    :param offer: Required. The gallery image offer name.
    :type offer: str
    :param sku: Required. The gallery image sku name.
    :type sku: str
    """

    _validation = {
        'publisher': {'required': True},
        'offer': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
    }

    def __init__(self, *, publisher: str, offer: str, sku: str, **kwargs) -> None:
        super(GalleryImageIdentifier, self).__init__(**kwargs)
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
