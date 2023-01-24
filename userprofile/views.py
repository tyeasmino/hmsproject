from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):  
    if request.user.is_anonymous:
        return redirect("signin")  
    return render(request, 'userprofile/index.html') 

def signin(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        # Check if user has etered correct credentials
        user = authenticate(username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect("/") 
        else:
            return render(request, 'userprofile/signin.html') 

    return render(request, 'userprofile/signin.html') 

def signout(request): 
    logout(request) 
    return redirect("signin")  
