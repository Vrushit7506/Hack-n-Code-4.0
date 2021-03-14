from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/index.html')

def earth(request):
    return render(request, 'main/earth.html')

def child(request):
    return render(request, 'main/child.html')
