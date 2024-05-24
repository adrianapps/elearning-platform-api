from django.contrib import admin
from .models import Course, Category, Lesson, Material, StudentSubmission


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(StudentSubmission)
