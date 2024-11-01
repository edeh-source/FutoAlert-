from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthororReadOnly
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')
    serializer_class = PostSerializer
    permission_classes = [IsAuthororReadOnly, IsAuthenticated,]
    
    
    
    def get_queryset(self):
        return Post.objects.filter(active=True).order_by('-created')
    
    
    def get_object(self):
        obj = Post.objects.get(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user, edited=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)    
    
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        post = user.like_post(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        post = user.unlike_post(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)



