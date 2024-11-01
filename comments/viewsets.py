from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthororReadOnly
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment



class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'patch', 'put', 'delete')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthororReadOnly, IsAuthenticated]
    
    
    def get_queryset(self):
        return Comment.objects.filter(active=True)
    
    
    def get_object(self):
        obj = Comment.objects.get(id=self.kwargs["pk"])
        return obj
    
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user, edited=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
    