from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.serializers.captcha_field_serializer import CaptchaFieldSerializer

class RegisterFormSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    captcha = CaptchaFieldSerializer(required=True)
    
    
    # class Meta:
    #     model = User
    #     extra_fields = ['email']
    #     fields = ['username', "password1", "password2"]