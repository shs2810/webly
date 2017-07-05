from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post),
    url(r'^home_place/$', views.home_place, name='home_place'),
    url(r'^home_school/$',  views.home_school, name='home_school'),
]
