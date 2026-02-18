from django.urls import path
from .views import (
    PostListAPIView,
    PostPreviewListAPIView,
    CommentListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    CommentDetailAPIView
)

urlpatterns = [
    path("posts/", PostListAPIView.as_view()),
    path("posts/preview/", PostPreviewListAPIView.as_view()),
    path("comments/", CommentListAPIView.as_view()),
    path("posts/create/", PostCreateAPIView.as_view()),
    path("posts/<int:id>/", PostDetailAPIView.as_view()),
    path("comments/<int:id>/", CommentDetailAPIView.as_view()),
]
