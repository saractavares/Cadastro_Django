from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from register.views import register

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=False,
    )

    class Meta:
        model = register.CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = register.CustomUser.objects.create_user(**validated_data)
        register.objects.create(user=user)
        return user