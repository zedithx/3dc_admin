from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# TODO - change to class views
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})