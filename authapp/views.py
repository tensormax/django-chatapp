from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required 

# Create your views here.

def index(request):
    return render(request, 'authapp/index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"Signup succeeded: {user.username}")  # debug
            return redirect('authapp:login')
        else:
            print("Form invalid:", form.errors)  # debug
    else:
        form = SignupForm()
    return render(request, 'authapp/signup.html', {'form': form})

        

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('chatapp:chat_page') 
    else:
        form = LoginForm()

    return render(request, 'authapp/login.html', {'form': form})
 


@login_required
def user_dashboard(request):
    return redirect('chatapp:chat_page')


def user_logout(request):
    logout(request)
    return redirect('authapp:login')