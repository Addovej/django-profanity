from django.db import models

__all__ = ['BaseModel']


class BaseModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pre_instance_save()
        super().save(*args, **kwargs)
        self.post_instance_save()

    def pre_instance_save(self):
        return

    def post_instance_save(self):
        return
