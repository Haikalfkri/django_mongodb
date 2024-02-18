from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogSerializer

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'description', )
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)