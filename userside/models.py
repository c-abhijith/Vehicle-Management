from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


Usertype=(
    ('SuperAdmin', 'SuperAdmin'),
    ('Admin', 'Admin'),
    ('User', 'User')

)
class UserDetails(AbstractUser):
    usertype = models.CharField(max_length=10,choices = Usertype,default = 'User')
   
    REQUIRED_FIELDS = [usertype,] # removes email from REQUIRED_FIELDS