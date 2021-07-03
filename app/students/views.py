from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudents(APIView):

    def get(self, request):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age')
        }

        students = StudentSerializer(data=data)

        if students.is_valid():
            students.save()
            return Response(students.data)
        else:
            return Response(students.erros)