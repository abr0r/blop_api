from django.urls import path

from .views import UserDetailView, UserListView

urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/', UserListView.as_view(), name='user_list'),
]


