"""URL configuration for tech_blog_api project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Tech Blog API",
        default_version="v1",
        description="API endpoint for tech blog",
        contact=openapi.Contact(email="humanresourceifi@gmail.com"),
        license=openapi.License(name="MIT Licence")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Tech Blog API Admin"
admin.site.site_title = "Tech Blog API Portal"
admin.site.index_title = "Welcom to the Tech Blog"