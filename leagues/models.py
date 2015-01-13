from django.db import models

# Create your models here.


class League(models.Model):
	league_name = models.CharField(max_length=60)

	def __str__(self):
		return self.league_name