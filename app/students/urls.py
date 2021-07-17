from django.urls import path

from . import views

urlpatterns = [

    path('all/', views.AllStudent.as_view()),
    path('create/', views.AddStudent.as_view()),
    path('<int:id>/', views.SpecificStudent.as_view()),

]