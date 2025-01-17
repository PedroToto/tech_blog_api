from django.urls import path
from .views import ResponseListCreateView, ResponseUpdateDeleteView

urlpatterns = [
    path("article/<uuid:article_id>/", ResponseListCreateView.as_view(), name="article-response"),
    path("<uuid:id>/", ResponseUpdateDeleteView.as_view(), name="response-detail"),
]