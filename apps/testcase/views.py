from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Task, TestSuite
from .serializers import TaskSerializer, TestSuitSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import TaskPermission, TestSuitPermission
from utils.pagination import TenItemPerPagePagination
from rest_framework import mixins


# Create your views here.
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('-c_time')  # 数据分页排序，根据创建时间排序

    pagination_class = TenItemPerPagePagination  # 分页控制
    filterset_fields = ['project']  # 过滤器
    permission_classes = [IsAuthenticated, TaskPermission]  # 权限控制

    # 当为post的时候，不会校验权限，需要主动走权限流程
    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(self, request, *args, **kwargs)


class TestSuitViewSet(ModelViewSet):
    serializer_class = TestSuitSerializer
    queryset = TestSuite.objects.all().order_by('-c_time')

    pagination_class = TenItemPerPagePagination  # 分页控制
    filterset_fields = ['task']  # 过滤器
    permission_classes = [IsAuthenticated, TestSuitPermission]  # 权限控制

    # 当为post的时候，不会校验权限，需要主动走权限流程
    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(self, request, *args, **kwargs)

# 定制化的序列化器，只有查看，创建功能，无其他删除更新等功能
# class TestSuitViewSet(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       GenericViewSet):
#     serializer_class = TestSuitSerializer
#     queryset = TestSuite.objects.all().order_by('-c_time')
#
#     pagination_class = TenItemPerPagePagination  # 分页控制
#     filterset_fields = ['task']  # 过滤器
#     permission_classes = [IsAuthenticated]  # 权限控制
