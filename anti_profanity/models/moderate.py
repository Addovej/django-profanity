from django.db import models
from django.utils.translation import ugettext_lazy as _

from anti_profanity.utils import PymorphyProc, RegexProc

from .base import BaseModel
from .managers import ModeratedModelManager
from .mixins import ModeratedModelMixin

__all__ = ['ProfanityModerateModel']


class ProfanityModerateModel(ModeratedModelMixin, BaseModel):
    _moderated_fields = []

    moderation_status = models.SmallIntegerField(
        choices=ModeratedModelMixin.MODERATION_STATUSES,
        default=ModeratedModelMixin.MODERATION_ACTIVE,
        verbose_name=_('Moderation Status'),
        db_index=True,
    )
    banned_until = models.DateTimeField(blank=True, null=True, db_index=True)

    objects = ModeratedModelManager()
    objects_all = models.Manager()

    class Meta:
        abstract = True

    def pre_instance_save(self):
        if self._moderated_fields:
            banned = {}

            for field in self._moderated_fields:
                field_value = getattr(self, field, None)
                banned_words = PymorphyProc.detect(field_value)
                banned_words = banned_words + RegexProc.detect(field_value)

                if banned_words:
                    banned[field] = banned_words

            if banned:
                self.moderation_status = self.MODERATION_BANNED_AUTO
