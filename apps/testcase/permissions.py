from utils.permission import IsSuperOrReadOnly
from .models import Project, Task


class TaskPermission(IsSuperOrReadOnly):

    def has_create_permission(self, request, view, obj):
        pk = request.data.get('project')
        queryset = Project.objects.filter(pk=pk)
        return queryset and queryset.first().leader == request.user

    def has_update_delete_permission(self, request, view, obj):
        return obj.project.leader == request.user


class TestSuitPermission(IsSuperOrReadOnly):

    def has_create_permission(self, request, view, obj):
        task_id = request.data.get('task')
        queryset = Task.objects.filter(pk=task_id)
        return queryset and queryset.first().project.leader == request.user

    def has_update_delete_permission(self, request, view, obj):
        return obj.task.project.leader == request.user
