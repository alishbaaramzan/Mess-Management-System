from django.urls import path
from . import views
from main.views import mainIndex

urlpatterns = [
    path('', views.supervisor_login, name='login'),
    path('index/', views.index, name='index'),
    path('all-students/', views.all_students, name='all_students'),
    path('all-students/<int:id>/', views.view_student, name='view_student'),
    path('weekly_menu/', views.weekly_menu, name='weekly_menu'),
    path('fee_students/', views.fee_students, name='fee_students'),
    path('register/', views.register_student, name='register_student'),
    path('edit_student/<int:id>/', views.edit, name='edit_student'),
    path('delete_student/<int:id>/', views.delete, name='delete_student'),
    path('log_out/', mainIndex, name='log_out'),
]
