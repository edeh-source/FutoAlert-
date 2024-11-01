from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ReplySerializer
from .models import Reply
from rest_framework.response import Response
from .permissions import IsAuthororReadOnly



class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class =  ReplySerializer
    permission_classes = [IsAuthororReadOnly, IsAuthenticated]
    http_method_names = ['get', 'put', 'patch', 'post', 'delete']
    
    
    def get_queryset(self):
        return Reply.objects.filter(active=True)
    
    
    def get_object(self):
        obj = Reply.objects.get(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
        
        
    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    
    
    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user, edited=True) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    
    
    


