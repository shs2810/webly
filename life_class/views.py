from django.shortcuts import render

# Create your views here.

def life(request):
    return render(request, 'life_class/life_class_right.html')