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
    
class StudentById(APIView):

    def get_student(self, id):

        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            return Response('Http404')
    
    def get(self, request, id):

        students = self.get_student(id=id)
        student_serializer = StudentSerializer(students)
        return Response(student_serializer.data)
    
    def delete(self, request, id):

        students = self.get_student(id=id)
        students.delete()
        students_serializer = StudentSerializer(students)
        return Response(students_serializer.data)
    
    def put(self, request, id):

        student = self.get_student(id=id)
        student_serializer = StudentSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response('Error, baby!')

class StudentByAge(APIView):

    def get(self, request, age):

        student = StudentModel.objects.filter(age=age)
        student_serializer = StudentSerializer(student, many=True)
        return Response(student_serializer.data)
