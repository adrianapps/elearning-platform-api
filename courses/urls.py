from django.urls import path
from .views import (
    api_root, UserList, CategoryList, CategoryDetail
)

app_name = 'courses'

urlpatterns = [
    path('', api_root, name='api-root'),
    path('users/', UserList.as_view(), name='user-list'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
]
