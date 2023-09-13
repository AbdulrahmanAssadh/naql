from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    identity=models.CharField(max_length=200)
    identity_Type=models.IntegerField()
    identity_num=models.IntegerField()
    nationality = models.CharField(max_length=200)
    phone=models.IntegerField()
    name_ar=models.CharField(max_length=255)
    name_en=models.CharField(max_length=255)
    confirmed=models.BooleanField(default=0)
    user_id=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    
    
    
# class temp(models.Model):
#     name=models.CharField(max_length=10)    