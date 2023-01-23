from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    password = None
    document_type = models.CharField(max_length=250)
    document = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    hobbie = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

