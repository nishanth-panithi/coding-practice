from django.urls import path
from .import views

urlpatterns=[
    path('reg_user/',view=views.reg_user),
    path('login_user/',view=views.login_user),
    path('get_users/',view=views.get_users),
    path('get_user/<int:id>',view=views.get_user),
    path('update_user/<int:id>',view=views.update_user),
    path('delete_user/<int:id>',view=views.delete_user),
    path('send_file',view=views.send_file),
]