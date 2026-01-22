from django.db import models

# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    roll_number=models.IntegerField(primary_key=True)
    
class employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    employee_id=models.IntegerField(primary_key=True)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
