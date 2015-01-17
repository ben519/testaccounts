from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = False
        
    def __unicode__(self):
        return self.name or self.email
