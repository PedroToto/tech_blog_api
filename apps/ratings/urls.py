from .views import RatingCreateView
from django.urls import path

urlpatterns = [
    path("article/<uuid:article_id>/", RatingCreateView.as_view(), name="rating-article")
]