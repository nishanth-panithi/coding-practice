from rest_framework import serializers
from .models import emp
 
class empSerializer (serializers.ModelSerializer):
    class Meta():
        model=emp
        fields="__all__" #this accepts all fields
        # fields=['emp-id','emp_name','emp_mail','emp_num'] # this accepts  selected fields

