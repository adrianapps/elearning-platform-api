from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from .models import Category, Course
from .serializers import CategorySerializer, CourseSerializer
from .permissions import IsTeacherOrReadOnly, IsCourseTeacherOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'category': reverse('courses:category-list', request=request, format=format),
        'course': reverse('courses:course-list', request=request, format=format)
    })


class CategoryList(APIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
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


class CourseList(APIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = self.serializer_class(courses, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(teacher=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsCourseTeacherOrReadOnly]

    def get_object(self, slug):
        return get_object_or_404(Course, slug=slug)

    def get(self, request, slug, format=None):
        course = self.get_object(slug)
        serializer = self.serializer_class(course, context={'request': request})
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        course = self.get_object(slug)
        serializer = self.serializer_class(course, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(teacher=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        course = self.get_object(slug)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
