"""
权限控制
"""
from rest_framework.permissions import BasePermission, SAFE_METHODS
from projects.models import Project, Module


class IsSupeUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSuperOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        if obj is None:
            return self.has_create_permission(request, view, obj)
        else:
            return self.has_update_delete_permission(request, view, obj)

    def has_create_permission(self, request, view, obj):
        return False

    def has_update_delete_permission(self, request, view, obj):
        return False


class EnvPermission(IsSuperOrReadOnly):

    def has_create_permission(self, request, view, obj):
        project_id = request.data.get('project')
        queryset = Project.objects.filter(id=project_id)
        return bool(queryset and queryset.first().leader == request.user)

    def has_update_delete_permission(self, request, view, obj):
        return bool(request.user == obj.project.user)

    # def has_object_permission(self, request, view, obj):
    #     if request.method in SAFE_METHODS:
    #         return True
    #
    #     if request.user.is_superuser:
    #         return True
    #
    #     if obj is None:
    #         # 创建的权限，并且判断创建项目的leader和创建人是否一致
    #         project_id = request.data.get('project')
    #         queryset = Project.objects.filter(id=project_id)
    #         return bool(queryset and queryset.first().leader == request.user)
    #
    #     if request.user == obj.project.user:
    #         return True
    #
    #     return False


class ModulePermission(EnvPermission):
    pass


class InterfacePermission(IsSuperOrReadOnly):

    def has_create_permission(self, request, view, obj):
        module_id = request.data.get('module')
        queryset = Module.objects.filter(id=module_id)
        return bool(queryset and queryset.first().project.leader == request.user)

    def has_update_delete_permission(self, request, view, obj):
        return bool(request.user == obj.module.project.leader)
