from rest_framework import serializers

from .models import Project, Environment, Module, Interface
from rest_framework.validators import UniqueTogetherValidator  # 联合唯一校验器


class ProjectSerializer(serializers.ModelSerializer):
    """项目序列化器"""
    leader = serializers.StringRelatedField()

    class Meta:
        model = Project
        exclude = ['is_delete', 'u_time']  # 不显示的字段


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['project', 'name'])
        ]


class InterfaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interface
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['module', 'name'])
        ]


class ModuleSerializer(serializers.ModelSerializer):

    interfaces = InterfaceSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        exclude = ['is_delete', 'u_time']  # 不显示的字段

        # 手写联合唯一校验
        validators = [
            UniqueTogetherValidator(queryset=model.objects.all(), fields=['project', 'name'])
        ]

