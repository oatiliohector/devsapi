from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllStudents.as_view()),
]

