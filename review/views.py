from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from post.models import Post

from .models import Comment, Like
from .serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(401)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        Like.objects.filter(user=user, post=post).delete()
    else:
        Like.objects.create(user=user, post=post)
    return Response(201)


