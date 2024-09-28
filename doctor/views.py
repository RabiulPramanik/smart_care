from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from . import models
from . import serializer

class SetPagination(pagination.PageNumberPagination):
    page_size = 1 #per page items
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DoctorViewsets(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    pagination_class = SetPagination
    serializer_class = serializer.DoctorSerializers

class SpecializationViewsets(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializer.SpecializationSerializers

class DesignationViewsets(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializer.DesignationSerializers

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset     
class AvailableTimeViewsets(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializer.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewViewsets(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializers
