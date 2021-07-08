from app import students
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
            'age': request.data.get('age')

        }

        student_serializer = StudentSerializer(data=data)

        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)

class StudentById(APIView):

    def get_object(self, id):
        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            return Response('Http404')

    def get(self, request, id, format=None):

        students = self.get_object(id=id)
        students_serializer = StudentSerializer(students)
        return Response(students_serializer.data)

    def delete(self, request, id):

        students = self.get_object(id=id)
        students.delete()
        return Response('Sucessfull!')

    def put(self, request,id):

        students = self.get_object(id=id)
        students_serializer = StudentSerializer(students, data=request.data)
        if students_serializer.is_valid():
            students_serializer.save()
            return Response('Sucessfull')
        else:
            return Response('ohhhhh tente de novo!')