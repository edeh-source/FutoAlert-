from auths.viewsets.login import LoginViewSet
from auths.viewsets.refresh import RefreshViewSet
from auths.viewsets.register import UserRegisterViewSet
from comments.viewsets import CommentViewSet
from posts.viewsets import PostViewSet
from replies.viewsets import ReplyViewSet
from rest_framework.routers import SimpleRouter
from users.viewsets import UserViewSet

from django.urls import path


router = SimpleRouter()

router.register(r'user', UserViewSet, basename='user'),
router.register(r'auth/register', UserRegisterViewSet, basename='auth'),
router.register(r'auth/login', LoginViewSet, basename='login'),
router.register(r'auth/refresh', RefreshViewSet, basename='refresh'),
router.register(r'post', PostViewSet, basename='post'),
router.register(r'comment', CommentViewSet, basename='comment'),
router.register(r'reply', ReplyViewSet, basename='reply')


urlpatterns = [
    *router.urls,
]