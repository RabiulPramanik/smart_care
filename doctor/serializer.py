from rest_framework import serializers
from . import models 

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'

class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'

class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'

class DoctorSerializers(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Doctor
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
