from django.shortcuts import render

# Create your views here.
def google(request):
    return render(request,'google.html')
def youtube(request):
    return render(request,'youtube.html')
def oyo(request):
    return render(request,'oyo.html')
def insta(request):
    return render(request,'instagram.html')