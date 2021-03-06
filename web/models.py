import random 
import string 
from django.db import models
from django.contrib.auth.models import User
from django import forms
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
    name=models.CharField(max_length=50)
    timelimit=models.DateField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    caption=models.CharField(max_length=255)
    file=forms.FileField()
    def __str__(self):
        return self.name

class Video (models.Model):
    name=models.CharField(max_length=50)
    timeuploded=models.DateField(default=datetime.now())
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    caption=models.CharField(max_length=255)
    file=forms.FileField()
    def __str__(self):
        return self.name

class Answer (models.Model):
    name=models.CharField(max_length=50)
    time=models.DateTimeField("Time submited",default=datetime.now())
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    caption=models.CharField(max_length=255)
    mark=models.CharField(max_length=3,blank=True)
    file=forms.FileField()
    def __str__(self):
        return self.name

