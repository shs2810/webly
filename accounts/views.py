from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from .forms import SignupForm
from .forms import LoginForm


# Create your views here.
def post(request):
    return render(request, 'accounts/login.html')

"""
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html',{
                  'form':form,})
"""

def profile(request):
    return render(request, 'accounts/profile.html')



def signup(request):
    signupform = SignupForm()
    if request.method == "POST":
        signupform = SignupForm(request.POST, request.FILES)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.lastname = signupform.cleaned_data['lastname']
            user.firstname = signupform.cleaned_data['firstname']
            user.sex = signupform.cleaned_data['sex']
            user.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )

    return render(request, "accounts/signup_form.html", {
        "signupform": signupform,
    })

def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
          authentication_form = LoginForm,
          template_name = 'accounts/login_form.html',
          extra_context={'providers':providers})