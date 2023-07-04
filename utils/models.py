from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class AbstractModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('created by'),related_name="created_by_%(app_label)s_%(class)s",null=True,blank=True,  on_delete=models.CASCADE)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('modified by'),related_name="modified_by_%(app_label)s_%(class)s",null=True,blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(_('status'), default=True)
    class Meta:
        abstract = True