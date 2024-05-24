from rest_framework import serializers
from .models import Category, Course, Lesson, Material, StudentSubmission




class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='courses:category-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = ['url', 'name', 'slug']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'title', 'description', 'teacher', 'students', 'year', 'slug']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['url', 'title', 'course', 'description', 'date', 'slug']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['url', 'title', 'lesson', 'description', 'file', 'upload_date', 'slug']


class StudentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubmission
        fields = ['url', 'title', 'student', 'lesson', 'file', 'grade', 'due_date', 'upload_date', 'slug']
