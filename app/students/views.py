from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudents(APIView):

    def get(self, request):

        students = StudentModel.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)

class AddStudent(APIView):

    def post(self, request):

        data = {

            'name': request.data.get('name'),
            'age': request.data.get('age'),

        }

        student_serializer = StudentSerializer(data=data)

        if student_serializer.is_valid():
            student_serializer.save()   
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)