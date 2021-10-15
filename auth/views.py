from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate , login as auth_login
from auth import forms
# Create your views here.
def login(request):
    loginForm=forms.LoginForm()
    error= None

    if request.method =="POST":
        loginForm=forms.LoginForm(request.POST)
        if loginForm.is_valid():
            username=loginForm.cleaned_data['username']
            password=loginForm.cleaned_data['password']
            user =authenticate(username=username,password=password)
            if user:
                auth_login(request,user)
                return HttpResponseRedirect('/')
        
            else:
                error="invalid"

           
    context = {
        "form":loginForm,
        "error":error
    }
    return render(request,'auth/login.html',context)
    # return HttpResponse("hi")