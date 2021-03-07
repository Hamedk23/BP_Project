from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest , HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import * 
from .forms import *


def indexView(request):
    return render(request,'index.html')
@login_required()
@permission_required('is_staff')
def dashboardView(request):
    return render(request,'tchpanel.html')

@login_required()
def dashboardView(request):
    return render(request,'stdpanel.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

def student(request,*args,**kwargs):
    s=request.user

    return render(request,"stdpanel.html",{})

def teacher(request,*args,**kwargs):
    s=request.user

    return render(request,"tchpanel.html",{})

def answers(request,*args,**kwargs):
    answers=Answer.objects.all()
    context = {
        "answers":answers
    }

    return render(request,"answers.html",context)

def sendanswer (request,*args,**kwargs):
    if request.method=="POST":
        new_form= getanswer(request.POST ,request.FILES)
        if new_form.is_valid():
            print(new_form.cleaned_data)
            new_form.save()
        else:
            print(new_form.errors)
        new_form = getanswer()
    else:
        new_form=getanswer()
    data={
        "form": new_form
    }
    return render(request,"sendanswer.html",data)

