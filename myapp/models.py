from django.db import models
from datetime import datetime

# Create your models here.
class usersignup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    emailid=models.EmailField()
    uname=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    pwd=models.CharField(max_length=20)
    created=models.DateTimeField(default=datetime.now(),blank=True)


class mynotes(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    username=models.EmailField()
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    files=models.FileField(upload_to='My_Files')
    comments=models.TextField()