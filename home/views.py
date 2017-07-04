from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home_class.html')

def home_place(request) :
    return render(request, 'home/home_place.html')