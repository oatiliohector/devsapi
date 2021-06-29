from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import StudentModel
from .serializer import StudentSerializer

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = StudentModel.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)