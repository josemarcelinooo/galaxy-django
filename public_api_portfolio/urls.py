from django.urls import path
from .services import fetch_public_api_list

urlpatterns = [
    path('fetch-public-api-list/', fetch_public_api_list, name='fetch_public_api_list'),
]