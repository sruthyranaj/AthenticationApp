# api/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize fields of user model
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    customize jwt token
    """
    @classmethod
    def get_token(cls, user):
        """
        method to add additional fields in jwt token claims
        """
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims - first_name in token
        token['first_name'] = user.first_name
        return token

    def validate(self, attrs):
        """
        Method to check the user exist with given username or email
        """
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        # get the user object with entered username or email.
        user_obj = User.objects.filter(email=attrs.get("username"))\
            .first() or User.objects.filter(username=attrs.get("username"))\
            .first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)
