# -*- coding: utf-8 -*-

from collections import OrderedDict

from django import forms
from django.utils.translation import ugettext_lazy as _

from allauth.account.forms import SignupForm

attrs_dict = {'class': 'required'}


class SignupForm(SignupForm):

    name = forms.CharField(label=_("Name"), required=False, max_length=64,
                           widget=forms.TextInput(
                               attrs=dict(placeholder='Display name', **attrs_dict)))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        fields_key_order = ['name', 'email', 'password1', 'password2']
        self.fields = OrderedDict((k, self.fields[k]) for k in fields_key_order)

    def save(self, *args, **kwargs):
        user = super(SignupForm, self).save(*args, **kwargs)
        user.name = self.cleaned_data['name']
        user.save()

        return user
