from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, 'home/home_class.html')
    return render(request, 'home/home_place.html')
    return render(request, 'home/home_school.html')
