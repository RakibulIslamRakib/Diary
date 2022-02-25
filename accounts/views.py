from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
#from django.contrib import decorator
from Mydiary.views import show

# Create your views here.

def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request,'home.html',{"error":"Invalid credentials!"})
    return render(request,'home.html')


def logout(request):
    auth.logout(request)
    return redirect(home)    


def signup(request):
    if request.method == "POST":
        #create user
        if request.POST['password'] == request.POST['confirmpassword']:
            #password matched, now check the username is already used or not
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'register.html',{"error":"Username has already taken!"})
            except User.DoesNotExist: 
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                return redirect(home)   
        else:
            return render(request,'register.html',{"error":"Passwords doesn't matched!!"})

    else:    
        return render(request,'register.html')
