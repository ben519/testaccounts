from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	"""

	Customer user class
	"""

	email = models.EmailField(unique=True, db_index=True)

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.email