from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User

# Create your views here.

@login_required
def homepage(request):
    return render(request, 'homepage.html')

def login(request):

    if request.method == 'POST':
        if 'login_form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('core:homepage')
            else:
                print('invalid creds')

    return render(request, 'login.html')

@login_required
def minutes(request):
    return render(request, 'minutes.html')

def signup(request):
    
    if request.method == 'POST':
        if 'signup_form' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    print('already exists')
                else:
                    new_user = User.objects.create_user(username=username, password=password, email=email)
                    new_user.save()               
                    return redirect('core:login')


    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('core:login')