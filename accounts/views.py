from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post(request):
    return render(request, 'accounts/profile.html')

def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return auth_login(request,
         authentication_form = LoginForm,
          template_name = 'accounts/login.html',
          extra_context={'providers':providers})

@login_required
def profile(request) :
    return render(request, 'accounts/profile.html')

