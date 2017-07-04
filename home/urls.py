from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^home_place/$', views.home_place, name='home_place'),
]
