from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllStudents.as_view()),
    path('create/', views.AddStudent.as_view()),
    path('<int:id>/', views.StudentById.as_view())
    #path('age/<int:age>/', views.StudentByAge.as_view()),
]

