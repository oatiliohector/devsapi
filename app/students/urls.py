from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllStudents.as_view(), name='all_students'),
    path('create/', views.CreateStudent.as_view(), name='create_student'),
    path('update/<int:id>/', views.UpdateStudent.as_view(), name='update_student'),
    path('delete/<int:id>/', views.DestroyStudent.as_view(), name='delete_student'),

]