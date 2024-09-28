from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.views import APIView
from . import models
from . import serializer

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

class PatientViewsets(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializer.PatientSerializers

class RegistrationsView(APIView):
    serializer_class = serializer.RegistrationSerializers

    def post(self, request):
        serializers = self.serializer_class(data = request.data)

        if serializers.is_valid(): # json data valid hoile er condition e jabe
            user = serializers.save()
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return response.Response("Check your mail for confirmation")
        return response.Response(serializer.errors)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("registration")
    else:
        return redirect("registration")
    
class LoginView(APIView):
    def post(self, request):
        serializers = serializer.LoginSerializers(data = request.data)
        if serializers.is_valid():
            username = serializers.validated_data['username']
            password = serializers.validated_data['password']

            user = authenticate(username = username, password = password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return response.Response({'token' : token.key, 'user_id' : user.id})
            else:
                return response.Response({'error' : "Invalid Credential"})
        return response.Response(serializer.errors)

class LogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')