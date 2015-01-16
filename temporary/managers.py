
from django.db import models

from .conf import settings


class TemporaryManager(models.Manager):

    def get_for_request(self, request):
        if settings.TEMPORARY_SESSION_KEY in request.session:
            return self.filter(
                pk__in=request.session[settings.TEMPORARY_SESSION_KEY])
        return self.none()
