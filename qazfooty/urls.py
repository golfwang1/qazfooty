# qazfooty/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from clubs import views as clubs_views

# Swagger / drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="QazFooty API",
        default_version="v1",
        description="Документация для API (JWT авторизация: /api/auth/token/ → Bearer <access>)",
        contact=openapi.Contact(email="support@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Веб-часть
    path("", clubs_views.home, name="home"),
    path("clubs/", clubs_views.clubs_all, name="clubs_all"),
    path("club/<int:pk>/", clubs_views.club_detail, name="club_detail"),
    path("search/", clubs_views.search, name="search"),
    path("news/", clubs_views.news_list, name="news_list"),

    # Users (namespace)
    path("users/", include(("users.urls", "users"), namespace="users")),

    # API (включая JWT-роуты из api/urls.py)
    path("api/", include("api.urls")),

    # Swagger / Redoc
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








