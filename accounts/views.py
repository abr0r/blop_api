from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import UserSerializer


class UserListView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer