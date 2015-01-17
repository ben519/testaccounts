# -*- coding: utf-8 -*-

from django.conf import settings  # pylint: disable=W0611

from appconf import AppConf


class TemporarySettings(AppConf):
    SESSION_KEY = 'tmp_list'
    AGE = 60 * 60 * 24  # default is one day

    class Meta:
        prefix = 'temporary'
        holder = 'temporary.conf.settings'
