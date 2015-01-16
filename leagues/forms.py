from django.forms import ModelForm

from temporary.forms import TemporaryFormMixin

from .models import League


class LeagueForm(TemporaryFormMixin, ModelForm):

    class Meta:
        model = League
        fields = ['league_name']
