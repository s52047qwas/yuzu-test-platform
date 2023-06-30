from django.urls import path

from .views import request_view

urlpatterns = [
    path('',request_view,name='request')
]