from .base_setting import *


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
