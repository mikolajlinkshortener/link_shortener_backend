from django.db import models
from django.core import validators
from django.conf import settings


class ShortLink(models.Model):
    link = models.TextField(validators=[validators.URLValidator()])
    short_link = models.CharField(
        max_length=settings.SHORT_LINK_LENGTH, null=True, blank=True, unique=True
    )
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(null=True, blank=True)
    visit_number = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
