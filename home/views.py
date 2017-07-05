from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, 'home/home_class.html')
def home_place(request):
    return render(request, 'home/home_place.html')
def home_school(request):
    return render(request, 'home/home_school.html')
