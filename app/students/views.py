from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StudentModel
from .serializer import StudentSerializer


class AllStudent(APIView):

    def get(self, request):

        student = StudentModel.objects.all()
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)