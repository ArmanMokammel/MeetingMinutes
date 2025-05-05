from django.shortcuts import render

# Create your views here.

def first(request):
    return render(request, 'first.html')

def login(request):
    return render(request, 'login.html')

def minutes(request):
    return render(request, 'minutes.html')

def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    return render(request, 'signup.html')