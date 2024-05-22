from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('courses:user-list', request=request, format=format),
        'category': reverse('courses:category-list', request=request, format=format),
    })


class UserList(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class CategoryList(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'name': request.data.get('name')}
        serializer = self.serializer_class(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    serializer_class = CategorySerializer

    def get_object(self, slug):
        return get_object_or_404(Category, slug=slug)

    def get(self, request, slug, format=None):
        category = self.get_object(slug)
        serializer = self.serializer_class(category, context={'request': request})
        return Response(serializer.data)
