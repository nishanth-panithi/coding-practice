from django.db import models

# Create your models here.

class emp(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50,null=False)
    emp_mail=models.CharField(max_length=50,default='emp@org.in')
    emp_num=models.CharField(max_length=10)