from django.shortcuts import render
#from django.http import HttpRequest , HttpResponse
from .models import * 

def student(request,*args,**kwargs):
    s=request.user

    return render(request,"stdpanel.html",{})

def teacher(request,*args,**kwargs):
    s=request.user

    return render(request,"tchpanel.html",{})

def sendexercise (request,*args,**kwargs):
    s=request.user

    return render(request,"sendexercise.html",{})

