from django.conf.urls.defaults import patterns, url

from flight_search import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.index, name='search'),
    
)