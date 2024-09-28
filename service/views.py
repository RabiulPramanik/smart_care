from django.shortcuts import render
from rest_framework import viewsets
from . import serializer
from . import models

class ServiceViewsets(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializer.ServiceSerializers
