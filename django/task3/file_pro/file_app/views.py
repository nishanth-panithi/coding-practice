from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def validate_file(file):
    max_size=5*1024*1024
    if file.size > max_size:
        return False, 'file size must be is between 0-5MB'
    allowed_types=['image/jpeg','image/png']
    if file.content_type not in allowed_types:
        return False, 'invalide_file type. Allowed : JPG, PNG'
    else:
        return True,'valid file'

@csrf_exempt
def reg_user(req):
    std_id=req.POST.get('std_id')
    std_name=req.POST.get('std_name')
    #std_pic=req.FILES.get('std_pic')
    std_pic=req.FILES['std_pic']

    #print(std_pic)
   
    is_valid_file,msg=validate_file(std_pic)
    if is_valid_file:
        pass
    else:
        return HttpResponse(msg)
    
    Std=student.objects.create(std_id=std_id,std_name=std_name,std_pic=std_pic)
    Std.save()
    return HttpResponse('Sucessfully registered')


  