from django.db import models
from django.contrib.auth.models import AbstractUser



class ArookoUser(AbstractUser):
    matric_no = models.CharField(max_length=14)
    
    