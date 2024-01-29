#accounts / views.py
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    """
    새로운 User를 만들어주는 역할을 합니다.

    function
    - create: 회원가입
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveAPIView):
    """
    특정 사용자의 프로필을 보여줍니다.

    function
    - get: 프로필 보기

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return self.request.user
