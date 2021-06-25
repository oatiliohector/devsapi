from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllStudents.as_view(), name='all_students'),
    path('create/', views.CreateStudent.as_view(), name='create_student'),

]