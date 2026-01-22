from django.shortcuts import render
from .models import student
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def get_user(req):
    if req.method=='GET':
        std_data=student.objects.all() # for fetching all the records from the table.
        dict_data=std_data.values() #values() -> helps to convert quarysets to dict data.
        list_data=list(dict_data) # even it convert into dict data still it cannot be print ,so we need to convert into list using type cnvertion. 
        return JsonResponse({"all data":list_data})
    
@csrf_exempt
def reg_user(req):
    std_id=req.POST.get('std_id')
    std_name=req.POST.get('std_name')
    std_branch=req.POST.get('std_branch')
    std_number=req.POST.get('std_number')
    Student=student.objects.create(std_id=std_id,std_name=std_name,std_branch=std_branch,std_number=std_number)
    Student.save()
    return HttpResponse('sucessfully reqister')

@csrf_exempt
def update_user(req,id):
    try:                               # user data converts into string formate using json dumps at the api itself, then it gives though request. from request we can perform actions by conerting that through json loads or serilizers 
        user_data=json.loads(req.body) # json.loads helps to convert bytes string (single string that we get from apis) into python dictionary (json formate) to access and store it in database
    except json.JSONDecodeError:
        return JsonResponse({"error:Invalid JSON"})
    try:
        Student=student.objects.get(std_id=id)
    except student.DoesNotExist:
        return HttpResponse('error: user not exists')
    
    if 'std_id' in user_data:
        Student.std_id=user_data['std_id']
    if 'std_name' in  user_data:
        Student.std_name=user_data['std_name']
    if 'std_branch' in user_data:
        Student.std_branch=user_data['std_branch']
    if 'std_number' in user_data:
        Student.std_number=user_data['std_number']
    Student.save()
    return JsonResponse({'Transaction Status':'sucessfully updated'})

@csrf_exempt
def delete_user(req,id):
    try:
        Student=student.objects.get(std_id=id)
    except:
        return HttpResponse('error: user dose not exists')
    Student.delete()
    return JsonResponse({'Transaction Status':'Deleted sucessfully'})