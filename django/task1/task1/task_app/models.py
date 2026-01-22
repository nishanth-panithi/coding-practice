from django.db import models

# Create your models here.

class student(models.Model): #attribute= fields
    std_id=models.IntegerField(primary_key=True)
    std_name=models.CharField(max_length=50)
    std_branch=models.CharField(max_length=50)
    std_number=models.CharField(max_length=10,unique=True)

