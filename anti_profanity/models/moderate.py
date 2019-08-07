from django.db import models
from django.utils.translation import ugettext_lazy as _

from anti_profanity.utils import PymorphyProc, RegexProc

from .base import BaseModel

__all__ = ['ProfanityModerateModel']


class ProfanityModerateModel(BaseModel):
    _moderated_fields = []

    profanity_banned = models.BooleanField(
        verbose_name=_('Is profanity banned'),
        default=False,
        db_index=True
    )

    class Meta:
        abstract = True

    def pre_instance_save(self):
        if self._moderated_fields:
            banned = False

            for field in self._moderated_fields:
                field_value = getattr(self, field, None)
                # Temporary removed regex method
                # banned |= RegexProc.detect(field_value)
                # It's just for reduce database queries
                if not banned:
                    banned |= PymorphyProc.detect(field_value)

            if banned:
                self.profanity_banned = True
