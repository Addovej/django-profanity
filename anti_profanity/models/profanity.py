from django.db import models
from django.utils.translation import ugettext_lazy as _
from pymorphy2 import MorphAnalyzer

from .base import BaseModel

__all__ = ['Profanity']

morph = MorphAnalyzer()


class Profanity(BaseModel):
    word = models.CharField(
        verbose_name=_('Normalizes form of profanity word'),
        max_length=64,
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Profanity')
        verbose_name_plural = _('Profanities')

    def __str__(self):
        return self.word

    def pre_instance_save(self):
        self.word = self.word.strip().lower()
        try:
            self.word = morph.parse(self.word)[0].normal_form
        except IndexError:
            pass
