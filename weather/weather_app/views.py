from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile


# note order of decorators
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    curr_user = request.user
    # if curr_user.is_anonymous
    # userprofile = UserProfile.objects.get(user=curr_user)
    data = {
        "first_name": curr_user.first_name,
        "last_name": curr_user.last_name
    }
    return Response(data)


