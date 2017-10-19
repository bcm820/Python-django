from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/$', views.main),
    url(r'^books/add/$', views.add),
    url(r'^books/(?P<id>\d+)/$', views.show_book),
    url(r'^users/(?P<id>\d+)/$', views.show_user),
    # posts:
    url(r'^books/(?P<id>\d+)/review/$', views.review),
    url(r'^books/add/new/$', views.new), # post book
    url(r'^register/$', views.register), # post user
    url(r'^login/$', views.login), # post login
    url(r'^logout/$', views.logout) # post logout
]