# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .permissions import IsPostOrIsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # restricted access of apis through permission setting
    permission_classes = [IsPostOrIsAuthenticated]

    def create(self, request):
        """
        Method to customize user creation by generating hashed password
        """
        
        # make password will create the hash value of currently entered
        # password before save in to the database
        request.data['password'] = make_password(
            request.data.get('password'))
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            # return user data if the user creation is successful
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return error message if the user creation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Customized view of token creation
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
