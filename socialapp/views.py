from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment
from .serializers import PostSerializer, PostPreviewSerializer, CommentSerializer
from drf_yasg.utils import swagger_auto_schema



class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostPreviewListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostPreviewSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CommentListAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all().order_by("-likes_count")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostCreateAPIView(APIView):
    
    @swagger_auto_schema(request_body=PostSerializer)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetailAPIView(APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CommentDetailAPIView(APIView):
    def get(self, request, id):
        try:
            comment = Comment.objects.get(id=id)
              
        except Comment.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    