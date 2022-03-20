from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    # path("subscriptions/", views.subscriptions),
    path("users/current", views.current_user),
    # path("user_settings/current", views.current_user_settings),

    path('token/', obtain_auth_token),
    # adding DELETE to token
]