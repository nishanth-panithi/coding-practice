from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from .models import emp
from django.views.decorators.csrf import csrf_exempt
from .serializer import empSerializer
# Create your views here.

############## Register User ##############

#regiter user using serializer

@csrf_exempt
def reg_user(req):
    user_data=json.loads(req.body)
    newEmp=emp.objects.create(emp_id=user_data['emp_id'],
                              emp_name=user_data['emp_name'],
                              emp_mail=user_data['emp_mail'],
                              emp_num=user_data['emp_num'])
    return HttpResponse('Sucessfully registered new user')

#-------------------------------------------------

# @csrf_exempt
# def reg_user(req):
#     user_data={}
#     for field in req.POST:
#         user_data[field]=req.POST[field] #here table field and api field name must be same
#     serialized_data=empSerializer(data=user_data,many=True)
#         if serialized_data.is_valid():
#             serialized_data.save
#             return HttpResponse("user reqistered sucessfully")

############## Get user ##############

#get_user using serializers

def get_user(req):
    data=emp.objects.all()
    serialized_data=empSerializer(data,many=True)
    # print(serialized_data.data)
    return JsonResponse({'emp_details':serialized_data.data})

#-------------------------------------------------

#get_user using without serializers

# def get_user(req):
#     data=emp.objects.all().values()
#     list_data=[]
#     for single_data in data:
#         list_data.append(single_data)
#     return JsonResponse({'emp_details':list_data})

############## Update User ##############

# update_user using serializers

def update_user(req,id):
    try:
        emp_data=emp.objects.get(emp_id=id)
        user_data=json.loads(req.body)
        serialized_data=empSerializer(emp_data,data=user_data,partial=True) #record to be updated/updated data/partial updated
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse('user updated')
        else:
            return HttpResponse('invalid data')
    except:
        return HttpResponse('user not found!') 

#-------------------------------------------------

# def update_user(req,id):
#     user_to_be_updated=emp.objects.get(emp_id=id)
#     new_data={}
#     for field in req.POST:
#         new_data[field]=req.POST[field]  #here table field and api field name must be same
#     serialized_data=empSerializer(user_to_be_updated,data=new_data,partial=True)
#     if serialized_data.is_valid():
#         serialized_data.save()
#         return HttpResponse("user updated")
        
#-------------------------------------------------
    
# update_user using serializers

# def update_user(req,id):
#     try:
#         user_data=json.loads(req.body)
#     except json.JSONDecodeError:
#         return HttpResponse('error:invalid JSON')
#     try:
#         emp_data=emp.objects.get(emp_id=id)
#     except emp.DoesNotExist:
#         return HttpResponse('error: user not exists')
#     if 'emp_id' in user_data:
#         emp.emp_id=user_data['emp_id']
#     if 'emp_name' in user_data:
#         emp.emp_name=user_data['emp_name']
#     if 'emp_mail' in user_data:
#         emp.emp_mail=user_data['emp_mail']
#     if 'emp_num' in user_data:
#         emp.emp_num=user_data['emp_num']
#     emp_data.save()
#     return HttpResponse('user updated')

############## Delete User ##############

def delete_user(req,id):
    emp_data=emp.objects.get(emp_id=id)
    emp_data.delete()