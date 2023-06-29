from rest_framework import serializers

from .models import Task, TestSuite, TestCase
from rest_framework.validators import UniqueTogetherValidator

from rest_framework.exceptions import ValidationError
from projects.models import Project


class TestCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCase
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        def validate(self, attrs):
            # 验证选择的接口是不是当前项目的接口
            interface = attrs.get('interface')
            test_suit = attrs.get('test_suit')
            if interface.module.project != test_suit.task.project:
                raise ValidationError('数据错误！')

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['title', 'test_suit'])
        ]


class TestSuitSerializer(serializers.ModelSerializer):
    testcases = TestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = TestSuite
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['name', 'task'])
        ]


class TaskSerializer(serializers.ModelSerializer):
    test_suits = TestSuitSerializer(many=True, read_only=True)  # 展示对应的test——suit

    class Meta:
        model = Task
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['name', 'project'])
        ]

    # 判断modules的数据是否符合要求
    def validate_modules(self, value):
        project_id = self.initial_data.get('project')  # 获取当前项目的模型
        queryset = Project.objects.filter(pk=project_id)

        if not queryset:
            raise ValidationError('id为{}的项目不存在'.format(project_id))

        ids = queryset.first().module_set.values_list('id')   # 拿到当前项目的id列表
        ids = [item[0] for item in ids]

        for i in value:
            if i.id not in ids:
                raise ValidationError('id为{}的项目不存在'.format(i.id))
        return value


