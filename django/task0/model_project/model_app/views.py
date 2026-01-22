from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import student
from .models import employee


# Create your views here.


def greet(request):
    return HttpResponse ("welcome to django!")

@csrf_exempt
def student_data(req):
    first_name=req.POST.get('first_name')
    last_name=req.POST.get('last_name')
    age=req.POST.get('age')
    roll_number=req.POST.get('roll_number')
    Student=student.objects.create(first_name=first_name,last_name=last_name,age=age,roll_number=roll_number)
    Student.save()
    return HttpResponse("Sucessfully student data inserted")

@csrf_exempt
def employee_data(req):
    first_name=req.POST.get('first_name')
    last_name=req.POST.get('last_name')
    employee_id=int(req.POST.get('employee_id'))
    department=req.POST.get('department')
    salary=req.POST.get('salary')
    Employee=employee.objects.create(first_name=first_name,last_name=last_name,employee_id=employee_id,department=department,salary=salary)
    Employee.save()
    return HttpResponse("Sucessfully employee data inserted")

    