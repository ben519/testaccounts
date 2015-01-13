from django.forms import ModelForm
from .models import League

class LeagueForm(ModelForm):
	class Meta:
		model = League