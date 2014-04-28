# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^aisproxy/$', 'aisproxy', name='aisproxy'),

)
