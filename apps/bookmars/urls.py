from django.urls import path
from .views import BookmarkCreateView, BookmarkDestroyView

urlpatterns = [
    path("add/<uuid:article_id>/", BookmarkCreateView.as_view(), name="add-bookmark"),
    path("remove/<uuid:article_id>/", BookmarkDestroyView.as_view(), name="remove-bookmark"),
]