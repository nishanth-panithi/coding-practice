from django.db import models

# Create your models here.


class student(models.Model):
    std_id=models.IntegerField(primary_key=True)
    std_name=models.CharField(max_length=50)
    std_pic=models.FileField(upload_to='profile/')