"""URL configuration for tech_blog_api project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView
from apps.users.views import CustomuserDetailsView

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
    path("api/v1/auth/user/", CustomuserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/", 
        PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("api/v1/profiles/", include("apps.profiles.urls")),
    path("api/v1/articles/", include("apps.articles.urls")),
    path("api/v1/ratings/", include("apps.ratings.urls")),
    path("api/v1/bookmarks/", include("apps.bookmars.urls")),
]

admin.site.site_header = "Tech Blog API Admin"
admin.site.site_title = "Tech Blog API Portal"
admin.site.index_title = "Welcom to the Tech Blog"