from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def post(request):
    return render(request, 'accounts/login.html')

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

def profile(request):
    return render(request, 'accounts/profile.html')