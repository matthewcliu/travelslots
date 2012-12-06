from django.conf.urls.defaults import patterns, url

from flight_search import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)