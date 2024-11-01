from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
import uuid
from rest_framework.decorators import action



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ['get', 'put']
    
    
    def get_queryset(self):
        return User.objects.all().order_by('-created')
    
    
    def get_object(self):
        
        obj = User.objects.get_object_by_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    
    def user_follow_method(self, request, *args, **kwargs):
        user_follower = self.get_object()
        user = request.user
        user_follow = user.follow_user(user_follower)
        serializer = self.serializer_class(user_follow)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
   
        
    

