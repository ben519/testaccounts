from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import LeagueCreateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testaccounts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/', LeagueCreateView.as_view()),
)
