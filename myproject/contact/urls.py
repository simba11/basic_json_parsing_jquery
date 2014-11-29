from django.conf.urls import patterns, url
from contact import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', 'contact.views.new'),
    url(r'^(?P<contact_id>\d+)/$', 'contact.views.detail'),
    url(r'^(?P<contact_id>\d+)\.(?P<extension>(json))$', 'contact.views.JSONResponse'),
)