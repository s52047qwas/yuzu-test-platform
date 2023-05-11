from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, Environment
from .serializers import ProjectSerializer, EnvironmentSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permission import EnvPermission


# Create your views here.
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 将当前用户和创建的项目关联
        serializer.save(leader=self.request.user)

    # 复写get_queryset,除了超级管理员，用户只能看到自己的没用被删除的数据
    def get_queryset(self):
        # 如果不是超级管理员，看不到被删除的数据
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            # queryset = queryset.filter(is_delete=False, leader=self.request.user)
            queryset = queryset.filter(is_delete=False, leader=self.request.user)
        return queryset

    # 复写perform_destroy方法，实现逻辑删除
    # def perform_destroy(self, instance):
    #     instance.is_delete = True
    #     instance.save()


class EnvironmentViewSet(ModelViewSet):
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
    permission_classes = [IsAuthenticated, EnvPermission]

    # 过滤对应项目的环境，只显示当前项目的环境
    def get_queryset(self):
        queryset = super().get_queryset()
        project = self.request.query_params.get('project')
        if project:
            queryset = queryset.filter(project=project)
        return queryset

    # 当为post的时候，不会校验权限，需要主动走权限流程
    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        super().create(self, request, *args, **kwargs)

