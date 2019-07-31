from django.db import models

from .mixins import ModeratedModelMixin

__all__ = ['ModeratedModelManager']


class ModeratedModelManager(ModeratedModelMixin, models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(moderation_status=self.MODERATION_ACTIVE)
