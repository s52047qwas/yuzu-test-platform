"""
序列化器
"""
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import User  # 模型
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator  # 验证是否唯一


class LoginSerialiazer(TokenObtainPairSerializer):
    """登录序列化器"""
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data


class RefreshSerialiazer(TokenRefreshSerializer):
    """刷新token序列化器"""
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data


class RegisterSerializer(serializers.ModelSerializer):
    """注册序列化器"""

    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码', min_length=8, max_length=20,
                                             error_messages={
                                                 'min_length': '密码至少需要8位！',
                                                 'max_length': '密码至多为20位！'
                                             }, write_only=True)

    # password = serializers.CharField(label='密码', help_text='密码', min_length=8, max_length=20, error_messages={
    #                                              'min_length': '密码至少需要8位！',
    #                                              'max_length': '密码至多为20位！'
    #                                          }, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email', 'mobile']

        # 额外校验
        extra_kwargs = {
            'username': {
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码至少需要6位！',
                    'max_length': '密码至多为20位！'
                }
            },
            'password': {
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码至少需要8位！',
                    'max_length': '密码至多为20位！'
                },
                'write_only': True
            },
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已被注册！')]
            }
        }

    # 重写create方法，删除password_confirm字段
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return User.objects.create_user(**validated_data)  # 需要调用create_user方法才会给密码加密
        # super(SignInSerializer, self).create(validated_data)

    # 校验密码是否一致
    def validate_password_confirm(self, data):
        if data!= self.initial_data.get('password'):
            raise serializers.ValidationError('两次输入的密码不一致！')
        return data

    # 第二种面膜校验方法
    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password_confirm']:
    #         raise serializers.ValidationError('两次输入的密码不一致！')
    #     return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'mobile', 'email', 'is_staff', 'is_active', 'is_superuser']

        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        password = validated_data.get('password')
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance


