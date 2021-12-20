from typing_extensions import Required
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, UserManager
from django.forms import models
from rest_framework import serializers

        # user = CustomUser.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        # return user

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    password = serializers.CharField(
        write_only=True,
        required=False,
    )
    class Meta:
        model = User
        fields = ["username", "email"]
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data.get('password'))
            User.objects.create_user(**validated_data)
            models.objects.create(user=UserModel)
            return UserChangeForm