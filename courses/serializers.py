from rest_framework import serializers
from .models import Category, Profile, Course, Lesson, Material, StudentSubmission, User


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='courses:category-detail',
        lookup_field='slug'
    )
    class Meta:
        model = Category
        fields = ['url', 'name', 'slug']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'user', 'first_name', 'last_name', 'join_date', 'is_teacher', 'slug']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'title', 'description', 'teacher', 'students', 'year', 'slug']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['url', 'title', 'course', 'description', 'date', 'slug']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['url', 'title', 'lesson', 'description', 'file', 'upload_date', 'slug']


class StudentSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentSubmission
        fields = ['url', 'title', 'student', 'lesson', 'file', 'grade', 'due_date', 'upload_date', 'slug']
