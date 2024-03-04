from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Patient
from .import serializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import login,logout

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializers.PaitentSerializer


class UserRagistrationAPIviewset(APIView):
    serializer_class = serializers.PatientRagistrationSerializer
    
    def post(self, request):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            user=serializers.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject="confirm your email"
            email_body=render_to_string('registration_email.html' ,{'confirm_link': confirm_link})
            email=EmailMultiAlternatives(email_subject, '',to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response("cheak your mail for confirmation")

        return Response(serializers.errors)


def activate(request,uid64,token):
    try:
          uid=urlsafe_base64_decode(uid64).decode()
          user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):

        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

     
    
class UserloginApiView(APIView):
    def post(self, request):
        serializer = serializers.Userloginserializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)  # Use unpacking to get the token
                login(request,user)
                return Response({'token': token.key, 'user_id': user.id})  # Access key attribute of the token object
            else:
                return Response({'error': "Invalid user"})
        return Response(serializer.errors)

class UserlogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')