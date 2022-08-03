from django.shortcuts import render
from django import views


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Customer
from .serializers import CustomerSerializer



class Pagination(PageNumberPagination):
    page_size = 10


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer 
    queryset = Customer.objects.all()
    filterset_fields = [ 'user']