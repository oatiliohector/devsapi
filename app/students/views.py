from rest_framework import generics

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudents(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class CreateStudent(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class UpdateStudent(generics.UpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer