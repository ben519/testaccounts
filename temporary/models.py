
from django.db import models
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField)

from polymorphic import PolymorphicModel

from .managers import TemporaryManager
from .conf import settings


class Temporary(PolymorphicModel):

    # for internal use...
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    ip_address = models.CharField(max_length=40, editable=False)

    pub_date = CreationDateTimeField(editable=False, db_index=True)
    last_modified = ModificationDateTimeField(editable=False)

    objects = TemporaryManager()
    
    class Meta:
        pass

    
@receiver(signal=user_logged_in)
def fix_ownership(sender, request, user, **kwargs):
    if isinstance(user, get_user_model()):
        Temporary.objects.get_for_request(
            request).filter(user__isnull=True).update(user=user)

        # flush outdated session
        if settings.TEMPORARY_SESSION_KEY in request.session:
            del request.session[settings.TEMPORARY_SESSION_KEY]
