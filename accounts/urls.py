from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post),
    url(r'^login/$', views.login, name='login'),

   # url(r'^login/$', auth_views.login, name='login',
   #    kwargs={'template_name' : 'accounts/login.html'}),

    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page' : settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name='profile'),

]