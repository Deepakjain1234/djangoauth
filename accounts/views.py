from django.shortcuts import render ,redirect
from accounts.models import newtable
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404, response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json


from accounts.models import Person

# Create your views here.
from .forms import RegisterForm, PersonForm


def index(request):
    return render(request,'accounts/index.html') 

def registeruser(request):
    form=RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()        
          
    return render(request,'accounts/register.html',{'form':form})

def loginuser(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        if username and password:
            user=authenticate(username=username, password=password )
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'invalid username and password') 
        else:
            messages.error(request,'field all field')        
    return render(request,'accounts/login.html') 

def home(request):
    return render(request,'accounts/home.html')

def contect(request):
     form= PersonForm
     if request.method =='POST':
        personForm=PersonForm(request.POST)
        personForm.save()

     return render(request,'accounts/contect.html',{'form':form})

@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse('ideal weigth should we:"weight"kg',safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)    



def newtable(requset):
    if requset=='POST':
        if requset.POST.get('username') and requset.POST.get('dis'):
            saverec=newtable()
            saverec.username=requset.POST.get('username')
            saverec.dis=requset.POST.get('dis')
            saverec.save()
    
        return render(requset,'testform.html')  
    else:
        return render(requset,'testform.html')          