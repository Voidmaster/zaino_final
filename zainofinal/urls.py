from django.conf.urls import patterns, include, url

from zaino.views import index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', 'zaino.views.index', name='index'),
    url(r'^admin/$', include(admin.site.urls)),
)
