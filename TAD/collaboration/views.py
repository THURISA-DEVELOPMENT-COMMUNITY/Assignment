from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from .models import CollaboratorModel
from .serializers import CollaborationSerializer


@api_view(['GET'])
def test1(request):
    data = {'message': 'Hello, this is a basic function-based API view!'}
    return Response(data)


@api_view(['GET', 'POST'])
def test2(request):
    if request.method == 'GET':
        data = {'message': 'This is a GET request!'}
        return Response(data)
    elif request.method == 'POST':
        # Handle POST data here
        return Response(status=status.HTTP_201_CREATED)


class APIViewTest(APIView):
    def get(self, request):
        data = {'message': 'Hello, this is a class-based API view!'}
        return Response(data)

    def post(self, request):
        # Handle POST data here
        return Response(status=status.HTTP_201_CREATED)


class CollaboratorView(generics.ListAPIView):
    queryset = CollaboratorModel.objects.all()
    serializer_class = CollaborationSerializer
