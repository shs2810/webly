from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)  # 회원가입에 성공하면, LOGIN 페이지로 이동
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html', {  # 템플릿은 일반적인 form template
        'form': form,
    })
@login_required  #  decorators -> wrapping 역할
def profile(request):
    return render(request, 'accounts/profile.html')