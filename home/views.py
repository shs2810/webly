from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home_class.html')
<<<<<<< HEAD
def home_place(request):
    return render(request, 'home/home_place.html')
def home_school(request):
    return render(request, 'home/home_school.html')
=======

def home_place(request) :
    return render(request, 'home/home_place.html')
>>>>>>> 47db58ecda0e57ed182893b3185e7d72e7670b8f
