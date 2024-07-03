from django.urls import path
from . import views
from supervisor.views import supervisor_login
from student.views import loginStudent 

urlpatterns = [
    path('', views.mainIndex, name='mainIndex'),
    path('supervisor/', supervisor_login, name='login_supervisor'),
    path('student/', loginStudent , name='login_student'),
]
