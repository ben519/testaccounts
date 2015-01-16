
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField)

from polymorphic import PolymorphicModel

from .managers import TemporaryManager, OrphansManager
from .conf import settings


class Temporary(PolymorphicModel):

    # for internal use...
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    ip_address = models.CharField(max_length=40, editable=False)

    pub_date = CreationDateTimeField(editable=False, db_index=True)
    last_modified = ModificationDateTimeField(editable=False)

    objects = TemporaryManager()
    orphans = OrphansManager()
    
    class Meta:
        pass

    @property
    def is_expired(self):
        if bool(self.user) is True:
            return True

        # check if this orphan is expired or not
        AGE = settings.TEMPORARY_AGE
        if (self.pub_date + timedelta(seconds=AGE)) <= timezone.localtime(timezone.now()):
            return True
        else:
            return False

    
@receiver(signal=user_logged_in)
def fix_ownership(sender, request, user, **kwargs):
    if isinstance(user, get_user_model()):
        # get all related orphans and update them
        Temporary.orphans.get_for_request(request).update(user=user)

        # flush outdated session...
        if settings.TEMPORARY_SESSION_KEY in request.session:
            del request.session[settings.TEMPORARY_SESSION_KEY]
