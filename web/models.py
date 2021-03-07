import random 
import string 
from django.db import models
from django.contrib.auth.models import User
from django import forms,utils
from datetime import datetime


"""
class Token( models.Model):
    token=models.CharField(''.join(random.choices(string.ascii_uppercase + string.digits, k=32)))
    def __init__():
        return token
        """
class Student (models.Model):
    #token=models.OneToOneField(Token)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    number=models.BigIntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=16)
    username=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Teacher (models.Model):
    #token=models.OneToOneField(Token)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)
    number=models.BigIntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=16)
    username=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Exercise (models.Model):
    name        =models.CharField(max_length=50,default="HW0")
    timelimit   =models.DateTimeField()
    teacher     =models.ForeignKey(Teacher,on_delete=models.CASCADE)
    caption     =models.CharField(max_length=255)
    pdffile     =models.FileField(upload_to="exercises/",blank=True,null=True)
    def __str__(self):
        return self.name

class Video (models.Model):
    name        =models.CharField(max_length=50,default="UV0")
    timeuploded =models.DateTimeField(default=datetime.now())
    teacher     =models.ForeignKey(Teacher,on_delete=models.CASCADE)
    caption     =models.CharField(max_length=255)
    vfile       =models.FileField(upload_to="videos/",blank=True,null=True)
    def __str__(self):
        return self.name

class Answer (models.Model):
    name        =models.CharField(max_length=50,default="AHW0")
    time        =models.DateTimeField("Time submited",default=datetime.now())
    student     =models.ForeignKey(Student,on_delete=models.CASCADE)
    caption     =models.TextField(default="")
    mark        =models.CharField(max_length=3,blank=True)
    pdffile     =models.FileField(upload_to="answers/",blank=True,null=True)
    def __str__(self):
        return self.name

