from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
class PatientSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'

class RegistrationSerializers(serializers.ModelSerializer):
    comfirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'comfirm_password']
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password1 = self.validated_data['comfirm_password']

        if password != password1:
            raise serializers.ValidationError({'error': "password dose not mactched!"})
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({"error": "This email Allready exist!"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
        