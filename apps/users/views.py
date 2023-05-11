from django.shortcuts import render
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .serializers import LoginSerialiazer, RefreshSerialiazer, RegisterSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import User
from utils.permission import IsSupeUser
# Create your views here.


class LoginView(TokenObtainPairView):
    """登录视图"""
    serializer_class = LoginSerialiazer


class RefreshView(TokenRefreshView):
    """刷新token视图"""
    serializer_class = RefreshSerialiazer


class RegisterView(CreateAPIView):
    """创建用户视图"""
    serializer_class = RegisterSerializer


class UserViewSet(ModelViewSet):
    """用户视图集"""
    serializer_class = UserSerializer   # 序列化器
    queryset = User.objects.all().order_by('-date_joined')   # 数据库数据和排序
    permission_classes = [IsSupeUser]   # 权限控制
