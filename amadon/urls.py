from django.conf.urls import url
from . import views # imports 'views.py' from current dir (.)

urlpatterns = [
    url(r'^$', views.form),
    url(r'^buy/$', views.buy),
    url(r'^checkout/$', views.checkout)
]