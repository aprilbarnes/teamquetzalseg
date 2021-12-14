from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    bio = models.CharField(max_length=520,blank=True)
    personalstatement = models.CharField(max_length=520,blank=True)
    experiencelevel = models.CharField(max_length=50,blank=False)
    username= models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username will have @ followed by atleast three alphanumeric chars',
        )]
    )
    first_name= models.CharField(max_length=50,blank=False)
    last_name= models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True, blank=False)
