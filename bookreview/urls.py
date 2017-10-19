from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/$', views.main),
    url(r'^books/add/$', views.add),
    url(r'^books/(?P<id>\d+)/$', views.show_book),
    url(r'^users/(?P<id>\d+)/$', views.show_user),
    url(r'^books/(?P<id>\d+)/review/$', views.review),
    url(r'^reviews/(?P<id>\d+)/remove/$', views.remove),
    url(r'^books/add/new/$', views.new),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout)
]