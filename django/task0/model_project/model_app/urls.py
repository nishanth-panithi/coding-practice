from django.urls import path
from . import views

urlpatterns=[
    path("greet/",view=views.greet),
    path("student_data/",view=views.student_data),
    path("employee_data/",view=views.employee_data),
]