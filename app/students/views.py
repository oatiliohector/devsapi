from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudents(APIView):

    def get(self, request):

        students = StudentModel.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)