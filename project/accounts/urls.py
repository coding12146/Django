#accounts / urls.py
from django.urls import path
from .views import UserCreateView, UserDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as get_token,
    TokenRefreshView as refresh_token,
    token_verify,
)

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("user/", UserDetailView.as_view(), name="user-detail"),
    path("token/", get_token.as_view(), name="token_obtain_pair"),
    path("token/refresh/", refresh_token.as_view(), name="token_refresh"),
    path("token/verify/", token_verify, name="token_verify"),
]
