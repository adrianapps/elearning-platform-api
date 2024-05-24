from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomUserSerializer, PublicCustomUserSerializer
from .models import CustomUser


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug, format=None):
        user = get_object_or_404(CustomUser, slug=slug)
        serializer = PublicCustomUserSerializer(user)
        return Response(serializer.data)
