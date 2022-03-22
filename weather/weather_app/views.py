import http

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile, Subscription


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

# current_user = api_view(['GET'])(authentication_classes([TokenAuthentication])(permission_classes([IsAuthenticated])(current_user)))

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscriptions(request):
    if request.method == 'GET':
        subs = Subscription.objects.filter(user=request.user)
        subs_list = []
        for sub in subs:
            subs_list.append({'id': sub.id, 'country': sub.country, 'city': sub.city})
        return Response(subs_list)
    elif request.method == 'POST':
        Subscription.objects.create(country=request.data['country'], city=request.data['city'], user=request.user)
        return Response(status=http.HTTPStatus.CREATED)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscription_details(request, id):
    sub = Subscription.objects.get(user=request.user, id=id)
    sub.delete()
    return Response(200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscription_import(request):
    file_content = request.FILES['file'].file.read()
    print(file_content)
    return Response(200)