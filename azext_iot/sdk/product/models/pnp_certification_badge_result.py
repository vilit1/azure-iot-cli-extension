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


class PnpCertificationBadgeResult(Model):
    """Pnp badge certification result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar validation_tasks:
    :vartype validation_tasks:
     list[~product.models.DigitalTwinValidationTaskResult]
    :ivar pre_validation_tasks:
    :vartype pre_validation_tasks:
     list[~product.models.PreValidationTaskResult]
    :ivar type: Possible values include: 'IotDevice', 'Pnp',
     'IotEdgeCompatible'
    :vartype type: str or ~product.models.enum
    :param resolution_source: Possible values include: 'Unknown',
     'GlobalRepository', 'PrivateRepository', 'UserUploads'
    :type resolution_source: str or ~product.models.enum
    """

    _validation = {
        'validation_tasks': {'readonly': True},
        'pre_validation_tasks': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'validation_tasks': {'key': 'validationTasks', 'type': '[DigitalTwinValidationTaskResult]'},
        'pre_validation_tasks': {'key': 'preValidationTasks', 'type': '[PreValidationTaskResult]'},
        'type': {'key': 'type', 'type': 'str'},
        'resolution_source': {'key': 'resolutionSource', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PnpCertificationBadgeResult, self).__init__(**kwargs)
        self.validation_tasks = None
        self.pre_validation_tasks = None
        self.type = None
        self.resolution_source = kwargs.get('resolution_source', None)
