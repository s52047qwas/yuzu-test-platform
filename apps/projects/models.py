from django.db import models
from django.conf import settings
from utils.model import BaseModel
from users.models import User
from rest_framework.validators import ValidationError
# Create your models here.


class Project(BaseModel):
    name = models.CharField('项目名称', max_length=40, unique=True, help_text='项目名称')
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='负责人', null=True, on_delete=models.SET_NULL,
                               related_name='projects')
    desc = models.CharField('项目描述', max_length=200, null=True, blank=True, default='', help_text='项目描述')

    class Meta:
        db_table = 'tb_project'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name
        ordering = ['-u_time']

    def __str__(self):
        return self.name


def validate_host(value):
    if value.endswith('/'):
        raise ValidationError('host不能以/结尾！')


class Environment(BaseModel):
    db_config_help = '''json数据{
            "host":"some.com",
            "user": "root",
            "password": "123456",
            "db": "some",
            "charset": "utf8",
            "autocommit": True
        }'''
    name = models.CharField('环境名称', max_length=128, help_text='环境名称')
    host = models.URLField('项目主机', validators=[validate_host], help_text='url不要以/结尾')
    db_config = models.JSONField('数据库设置', null=True, blank=True, help_text=db_config_help)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='所属项目')

    def __str__(self):
        return '{}_{}'.format(self.project.name, self.name)

    class Meta:
        db_table = 'tb_environment'
        verbose_name = '项目环境'
        verbose_name_plural = verbose_name

        # 联合唯一
        constraints = [
            models.UniqueConstraint(fields=['name', 'project'], name='unique_env_name')
        ]


class Module(BaseModel):

    name = models.CharField('模块名称', max_length=128, help_text='项目模块名称')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='所属项目')

    def __str__(self):
        return '{}_{}'.format(self.project.name, self.name)

    class Meta:
        db_table = 'tb_module'
        verbose_name = '项目模块'
        verbose_name_plural = verbose_name

        constraints = [
            models.UniqueConstraint(fields=['name', 'project'], name='unique_module_name')
        ]


class Interface(BaseModel):
    name = models.CharField('接口名称', max_length=128, help_text='接口名称')
    url = models.CharField('接口地址', max_length=128, help_text='接口地址')
    module = models.ForeignKey(Module, on_delete=models.PROTECT, help_text='所属模块', related_name='interfaces')
    developer = models.CharField('所属开发人员', max_length=128, help_text='所属开发人员', default='')

    def __str__(self):
        return '{}_{}_{}'.format(self.module.project.leader, self.module.name, self.name)

    class Meta:
        db_table = 'tb_interface'
        verbose_name = '接口模块'
        verbose_name_plural = verbose_name

        constraints = [
            models.UniqueConstraint(fields=['name', 'module'], name='unique_interface_name')
        ]
