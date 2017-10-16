from django.conf.urls import url
from . import views

urlpatterns = [
    # Blogs
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<num>\d+)/$', views.show),
    url(r'^(?P<num>\d+)/edit/$', views.edit),
    url(r'^(?P<num>\d+)/delete/$', views.destroy),
    # Surveys
    url(r'^surveys/$', views.surveys),
    url(r'^surveys/new/$', views.new_survey),
    # Users
    url(r'^register/$', views.register),
    url(r'^users/new/$', views.register),
    url(r'^login/$', views.login),
    url(r'^users/$', views.users)
]