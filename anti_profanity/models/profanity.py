from django.db import models
from django.utils.translation import ugettext_lazy as _
from pymorphy2 import MorphAnalyzer

__all__ = ['Profanity']

morph = MorphAnalyzer()


class Profanity(models.Model):
    word = models.CharField(
        verbose_name=_('Normalizes form of profanity word'),
        max_length=64,
        unique=True,
        db_index=True,
    )
    lang = models.CharField(
        max_length=5,
        db_index=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Profanity')
        verbose_name_plural = _('Profanities')

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.word = self.word.strip().lower()
        try:
            self.word = morph.parse(self.word)[0].normal_form
        except IndexError:
            pass
        super().save(*args, **kwargs)
