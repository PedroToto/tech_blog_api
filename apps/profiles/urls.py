from django.urls import path
from .views import (
    ProfileDetailAPIView, 
    ProfileListAPIView,
    UpdateProfileAPIView,
    FollowerListView,
    FollowAPIView,
    UnfollowAPIView
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("profile/", ProfileDetailAPIView.as_view(), name="my-profile"),
    path("profile/update/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("profile/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowAPIView.as_view(), name="unfollow"),
]