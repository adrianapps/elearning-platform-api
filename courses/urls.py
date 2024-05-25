from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root, CategoryList, CategoryDetail, CourseList, CourseDetail
)

app_name = 'courses'

urlpatterns = [
    path('', api_root, name='api-root'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<slug:slug>/', CourseDetail.as_view(), name='course-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
