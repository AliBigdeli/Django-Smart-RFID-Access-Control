from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,views
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import (
    ProfileSerializer,
    RegisterSerializer,
)
from accounts.models import Profile
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterApiView(generics.GenericAPIView):
    """Creates new user with the given info and credentials"""

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Register class
        """

        serializer = RegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        """
        Login view to get user credentials
        """
        serializer = self.get_serializer(data=request.data, many=False)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            if user is not None and user.is_active:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LogoutApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        """
        Logout class
        """
        logout(request)
        return Response(
            {"non_field_errors": "successfully logged out"},
            status=status.HTTP_200_OK,
        )
