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


class TestCase(BaseModel):
    class MethodType(models.TextChoices):
        GET = 'get', 'get'
        POST = 'post', 'post'
        HEAD = 'head', 'head'
        PUT = 'put', 'put'
        PATCH = 'patch', 'patch'
        DELETE = 'delete', 'delete'
        CONNECT = 'connect', 'connect'
        TRACE = 'trace', 'trace'

    class ResponseType(models.TextChoices):
        JSON = 'JSON', 'JSON'
        XML = 'XML', 'XML'
        HTML = 'HTML', 'HTML'

    REQUEST_FIELD_HELP = 'json格式的字符串，可选键与requests模块发送请求的参数一致'
    ASSERTION_HELP = '''断言表达式，嵌套的数组json字符串[[期望值,条件,jsonpath提取表达式],..]，
    例如：[[0,"eq","$..code"],["OK","eq","$..msg"]]'''
    MARKS_HELP = '字符串，用例标记，多个标记使用逗号隔开，例如：success,flow'
    EXTRACT_HELP = '提取响应结果表达式,嵌套数组json字符串[[变量名,提取表达式],..]'
    title = models.CharField('用例名称', max_length=200, help_text='用例名称')
    interface = models.ForeignKey(Interface, verbose_name='所属接口',
                                  on_delete=models.PROTECT, help_text='所属接口id',
                                  related_name='testcases')
    test_suit = models.ForeignKey(TestSuite, verbose_name='所属测试套件',
                                  on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='testcases', help_text='所属测试套件id')
    method = models.CharField('请求方法', max_length=12, choices=MethodType.choices,
                              default=MethodType.GET,
                              help_text='请求方法')
    request = models.TextField('请求数据', help_text=REQUEST_FIELD_HELP, null=True,
                               blank=True)
    tester = models.CharField('测试工程师', max_length=48, null=True, blank=True,
                              help_text='编写这条用例的测试工程师')
    marks = models.CharField('标记', max_length=200, help_text=MARKS_HELP, null=True,
                             blank=True)
    status_code = models.SmallIntegerField('响应状态码', null=True, blank=True,
                                           help_text='请求响应状态码')
    res_type = models.CharField('响应类型', max_length=24,
                                choices=ResponseType.choices, default=ResponseType.JSON,
                                help_text='字符串，响应类型，可选值 JSON XML HTML 必须大写')
    assertion = models.TextField('断言表达式', help_text=ASSERTION_HELP, null=True,
                                 blank=True)
    db_assertion = models.TextField('数据库断言表达式', help_text='数据库断言表达式，格式同断言表达式', null=True, blank=True)
    extract = models.TextField('响应结果提取数据表达式', help_text=EXTRACT_HELP,
                               null=True, blank=True)
    order = models.SmallIntegerField('序号', null=True, blank=True, help_text='序号')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_test_case'
        verbose_name = '测试用例'
        verbose_name_plural = verbose_name
        ordering = ['order', 'id']

