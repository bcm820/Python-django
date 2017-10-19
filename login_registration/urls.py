from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success/$', views.success),
    url(r'^register/$', views.register), # post
    url(r'^login/$', views.login), # post
    url(r'^logout/$', views.logout) # post
]