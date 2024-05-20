from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters 

from .models import Post
from .serializers import PostSerializer, PostListSrerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields = ['title']


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSrerializer
        return self.serializer_class

    def get_serializer_context(self):
        return {'request':self.request}