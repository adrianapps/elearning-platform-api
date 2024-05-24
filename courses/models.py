from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django_extensions.db.fields import AutoSlugField

CustomUser = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', overwrite=True, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(CustomUser, related_name='enrolled_students')
    year = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, models.CASCADE)
    description = models.TextField()
    file = models.FileField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return self.title


class StudentSubmission(models.Model):
    title = models.CharField(max_length=255)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField()
    upload_date = models.DateTimeField()
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return f"{self.student.user.username} submitted {self.file}"
