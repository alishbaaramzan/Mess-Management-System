from django.urls import path
from . import views
from main.views import mainIndex

urlpatterns = [
    path('', views.loginStudent, name='login_student'),
    path('index/', views.index, name='index_student'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('log_out/', mainIndex, name='log_out'),
]
