from django.contrib.auth.models import User
# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active')