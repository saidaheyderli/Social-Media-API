from django.urls import path
from .views import (
    PostListAPIView,
    PostPreviewListAPIView,
    CommentListAPIView,
    PostCreateAPIView,
    PostDeleteAPIView
    
)

urlpatterns = [
    path("posts/", PostListAPIView.as_view()),
    path("posts/preview/", PostPreviewListAPIView.as_view()),
    path("comments/", CommentListAPIView.as_view()),
    path("posts/create/", PostCreateAPIView.as_view()),
]
