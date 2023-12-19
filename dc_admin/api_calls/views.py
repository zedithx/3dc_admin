from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Members, Projects
from . import serializers
from django.db.models import Subquery, Prefetch, Count, Sum

# TODO - change to class views
@api_view(['GET'])
def hello_world(request):
    members = Members.objects.all()
    result = serializers.MembersSerializers(members, many=True).data
    return Response(result, status=status.HTTP_200_OK)