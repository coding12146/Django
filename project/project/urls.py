from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView as schema,
    SpectacularRedocView as redoc,
    SpectacularSwaggerView as swagger,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("task/", include("task.urls")),
    # 스키마
    path("schema/", schema.as_view(), name="schema"),
    # 스웨거
    path("schema/swagger-ui/", swagger.as_view(url_name="schema"), name="swagger-ui"),
    # 문서화
    path("schema/redoc/", redoc.as_view(url_name="schema"), name="redoc"),
]
