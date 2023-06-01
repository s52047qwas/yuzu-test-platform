from django.db import models

# Create your models here.

from utils.model import BaseModel
from projects.models import Project, Module, Interface, Environment


class Task(BaseModel):
    name = models.CharField('任务名称', max_length=200, help_text='测试任务名称')
    project = models.ForeignKey(Project, verbose_name='所属项目', on_delete=models.PROTECT, help_text='项目id',
                                related_name='tasks')
    modules = models.ManyToManyField(Module, verbose_name='负责的模块', help_text='包含模块')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_task'
        verbose_name = '测试任务'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=['name', 'project'], name='unique_task_name')
        ]


class TestSuite(BaseModel):
    name = models.CharField('测试套件名称', max_length=200, help_text='测试套件名称')
    task = models.ForeignKey(Task, verbose_name='测试任务', on_delete=models.PROTECT, help_text='测试任务id',
                             related_name='test_suits')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_test_suit'
        verbose_name = '测试套件'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=['name', 'task'], name='unique_testsuit_name')
        ]

