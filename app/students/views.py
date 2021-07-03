from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudentModel
from .serializer import StudentSerializer

class AllStudents(APIView):

    def get(self, request):
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    