from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField('手机号码', max_length=11, help_text='手机号码', null=True, blank=True, unique=True,
                              error_messages={'unique': '手机号码已注册'})
    # mobile = models.CharField('手机号码', max_length=11, help_text='手机号码', null=True, blank=True, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tb_user'   # 表明
        verbose_name = 'user'   # 站点显示名
        verbose_name_plural = verbose_name    # 复数显示

    REQUIRED_FIELDS = ["mobile"]  # 创建管理员时，提示输入的字段，默认是email，当前调整为mobil


