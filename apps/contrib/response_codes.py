# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

# >> SNS

NOT_SNS_REQUEST = {
    'code': 'ops.NotSNSRequests',
    'detail': _('This resource is forbidden for not SNS requests.'),
}

METHOD_NOT_ALLOWED = {
    'code': 'sns.MethodNotAllowed',
    'detail': _('This method is not allowed for SNS requests'),
}

INVALID_SNS_SIGNATURE = {
    'code': 'ops.InvalidSNSSignature',
    'detail': _('Invalid SNS Signature.'),
}

SNS_ENDPOINT_SUBSCRIBE_FAILED = {
    'code': 'ops.SNSEndpointSubscribeFailed',
    'detail': _('SNS endpoint subscribe failed.'),
}

SNS_ENDPOINT_SUBSCRIBE_CONFIRMED = {
    'code': 'ops.SNSEndpointSubscribeConfirmed',
    'detail': _('SNS endpoint subscribe confirmed.'),
}
