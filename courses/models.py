from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', overwrite=True, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=('first_name', 'last_name'), overwrite=True, unique=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Profile, related_name='enrolled_students')
    year = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return self.title

    # def clean(self):
    #     if not self.teacher.is_teacher:
    #         raise ValidationError(f"{self.teacher.user.username} is not a teacher")
    #     for student in self.students.all():
    #         if student.is_teacher:
    #             raise ValidationError(f"{student.user.username} is not a student")
    #

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
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    due_date = models.DateTimeField()
    upload_date = models.DateTimeField()
    slug = AutoSlugField(populate_from='title', overwrite=True, unique=True)

    def __str__(self):
        return f"{self.student.user.username} submitted {self.file}"
