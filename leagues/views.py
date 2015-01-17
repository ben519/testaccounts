from django.views.generic import CreateView

from temporary.views import RequestFromKwargsMixin

from .forms import LeagueForm
from .models import League


class LeagueCreateView(RequestFromKwargsMixin, CreateView):
    template_name = "leagues/addleague.html"
    model = League
    form_class = LeagueForm
    success_url = "/"
