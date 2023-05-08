from .base_setting import *
from datetime import timedelta


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yuzu_test_platform',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '120.25.76.157',
        'PORT': '3306',
    }
}

# JWT配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # token过期时间
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),   # refresh过期时间
}

# 允许使用ip跨域
CORS_ALLOW_ALL_ORIGINS = True
# 允许cookies跨域
CORS_ALLOW_CREDENTIALS = True