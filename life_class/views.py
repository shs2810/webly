from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, 'life_class/life_class.html')
def life_class_detail(request):
    return render(request, 'life_class/life_class_detail.html')
def life_class_write(request):
    return render(request, 'life_class/life_class_write.html')