from pathlib import Path
import sys
import django.conf.global_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 优化导入路径
sys.path.insert(0, str(BASE_DIR / 'apps'))

print(sys.path)

car = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}

dog = car.pop("model")


print(car)
print(dog)

# fields = ['username', 'password', 'password_confirm', 'email', 'mobile']

# 额外校验
# extra_kwargs = {
#     'username': {
#         'min_length': 6,
#         'max_length': 20,
#         'error_messages': {
#             'min_length': '密码至少需要6位！',
#             'max_length': '密码至多为20位！'
#         }
#     },
#     'password': {
#         'min_length': 8,
#         'max_length': 20,
#         'error_messages': {
#             'min_length': '密码至少需要8位！',
#             'max_length': '密码至多为20位！'
#         },
#         'write_only': True
#     },
#     'email': {
#         'required': True,
#         'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已被注册！')]
#     }
# }

# 重写create方法，删除password_confirm字段
# def create(self, validated_data):
#     validated_data.pop('password_confirm')
#     return User.objects.create_user(**validated_data)  # 需要调用create_user方法才会给密码加密
#     # super(SignInSerializer, self).create(validated_data)
#
# # 校验密码是否一致
# def validate_password_confirm(self, data):
#     if data!= self.initial_data.get('password'):
#         raise serializers.ValidationError('两次输入的密码不一致！')
#     return data

# 第二种面膜校验方法
# def validate(self, attrs):
#     if attrs['password'] != attrs['password_confirm']:
#         raise serializers.ValidationError('两次输入的密码不一致！')
#     return attrs


# password_confirm = serializers.CharField(label='确认密码', help_text='确认密码', min_length=8, max_length=20,
#                                          error_messages={
#                                              'min_length': '密码至少需要8位！',
#                                              'max_length': '密码至多为20位！'
#                                          }, write_only=True)