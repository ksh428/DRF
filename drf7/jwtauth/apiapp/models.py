from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

@receiver(post_save,sender=User) #SIGNAL TO CREATE A TOKEN WHENEVER A USER IS CREATED
def create_auth_token(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)



    
