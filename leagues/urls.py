from django.conf.urls import patterns, include, url

from .views import LeagueCreateView

urlpatterns = patterns('',
    url(r'^add/', LeagueCreateView.as_view()),
)
