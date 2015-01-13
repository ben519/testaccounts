from django.shortcuts import render
from django.views.generic import CreateView
from .forms import LeagueForm
from .models import League

class LeagueCreateView(CreateView):
	template_name = "leagues/addleague.html"
	model = League
	form_class = LeagueForm
	success_url = "/"