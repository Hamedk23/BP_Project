from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class login(models.Model):
    email=models.CharField()
    key=models.CharField()
    