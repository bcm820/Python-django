from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^add/$', views.create), # post
    url(r'^(?P<id>\d+)/$', views.show),
    url(r'^(?P<id>\d+)/review/$', views.review), # post
    url(r'^(?P<id>\d+)/confirm/$', views.confirm),
    url(r'^(?P<id>\d+)/delete/$', views.delete) # post
]