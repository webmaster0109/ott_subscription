from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ott_schemas.serializers import UserSerializer
from ott_schemas.models import User

# Create your views here.

def user_registration(request):
    return render(request, template_name='credentials/register.html')

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse('<p>Registration successful!</p>', status=status.HTTP_201_CREATED)
    return HttpResponse('<p>Registration failed! Please try again.</p>', status=status.HTTP_400_BAD_REQUEST)