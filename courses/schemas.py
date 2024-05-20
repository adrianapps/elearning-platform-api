from ninja import ModelSchema
from .models import Category, Profile, Course, Lesson, Material, StudentSubmission, User


class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ProfileSchema(ModelSchema):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'join_date', 'is_teacher', 'slug')




class CourseSchema(ModelSchema):
    teacher: ProfileSchema | None = None
    students: list[ProfileSchema]
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'teacher', 'students', 'year', 'slug')


class LessonSchema(ModelSchema):
    course: CourseSchema
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'course', 'description', 'date', 'slug')


class MaterialSchema(ModelSchema):
    lesson: LessonSchema
    class Meta:
        model = Material
        fields = ('id', 'title', 'lesson', 'description', 'file', 'upload_date', 'slug')


class StudentSubmissionSchema(ModelSchema):
    student: ProfileSchema
    lesson: LessonSchema
    class Meta:
        model = StudentSubmission
        fields = ('id', 'title', 'student', 'lesson', 'file', 'grade', 'due_date', 'upload_date', 'slug')
