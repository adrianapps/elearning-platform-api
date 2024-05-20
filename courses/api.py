from ninja import NinjaAPI
from .models import Category, Lesson, Course
from .schemas import CategorySchema, LessonSchema, CourseSchema

api = NinjaAPI()


@api.get("categories/", response=list[CategorySchema])
def get_categories(request):
    return Category.objects.all()


@api.get("courses/", response=list[CourseSchema])
def get_courses(request):
    return Course.objects.all()


@api.get('lessons/', response=list[LessonSchema])
def get_lessons(request):
    return Lesson.objects.all()
