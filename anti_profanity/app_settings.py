from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _


MODERATION_STATUS_BANNED_PERMANENTLY, \
MODERATION_STATUS_BANNED_TEMPORARILY, \
MODERATION_STATUS_ACTIVE, \
MODERATION_STATUS_BANNED_AUTO = range(4)
MODERATION_STATUSES = [
    (MODERATION_STATUS_BANNED_AUTO, _('Banned Auto')),
    (MODERATION_STATUS_BANNED_TEMPORARILY, _('Banned Temporarily')),
    (MODERATION_STATUS_BANNED_PERMANENTLY, _('Banned Permanently')),
    (MODERATION_STATUS_ACTIVE, _('Active')),
]
