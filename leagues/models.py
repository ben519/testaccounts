
from django.db import models

from temporary.models import Temporary


class League(Temporary):

    league_name = models.CharField(max_length=60)

    class Meta:
        pass

    def __unicode__(self):
        return self.league_name
