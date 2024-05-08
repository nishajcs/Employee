from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def SignupPage(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, email, password1, password2)
        if (password1 != password2):
            return HttpResponse("Password was not entered correctly")
        else:
            user1 = User.objects.create_user(username, email, password1)
            user1.save()
            return redirect("login")
    return render(request, "signup.html")

def loginPage(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or password was incorrect")
    return render(request, "login.html")

@login_required(login_url="login")
def home(request):
    return render(request, "home.html")

def logoutPage(request):
    logout(request)
    return redirect("login")