from django.db import models


class BaseModel(models.Model):
    """模型基类，公共字段"""
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    u_time = models.DateTimeField('更新时间', auto_now=True)
    is_delete = models.BooleanField('逻辑删除', default=False)

    class Meta:
        # 抽象类，用于继承，迁移时不会被创建
        abstract = True
