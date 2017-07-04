from django.conf.urls import url
from . import views
urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.post),
    url(r'^home_place/$', views.home_place, name='home_place'),
    url(r'^home_school/$',  views.home_school, name='home_school'),
]
=======
    url(r'^$', views.home),
    url(r'^home_place/$', views.home_place, name='home_place'),
]
>>>>>>> 47db58ecda0e57ed182893b3185e7d72e7670b8f
