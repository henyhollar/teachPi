from django.db import models
from django.contrib.auth.models import AbstractUser



class StudentUser(AbstractUser):
    matric_no = models.CharField(max_length=14, unique=True)
    
    
