from django.urls import path
from .views import CustomUserCreate, CustomUserDetail

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name='user-create'),
    path('user/<slug:slug>/', CustomUserDetail.as_view(), name='user-detail'),
]