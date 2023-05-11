# Generated by Django 4.1.7 on 2023-05-11 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_module_module_unique_module_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('name', models.CharField(help_text='接口名称', max_length=128, verbose_name='接口名称')),
                ('url', models.CharField(help_text='接口地址', max_length=128, verbose_name='接口地址')),
                ('devloper', models.CharField(help_text='所属开发人员', max_length=128, verbose_name='所属开发人员')),
                ('module', models.ForeignKey(help_text='所属模块', on_delete=django.db.models.deletion.CASCADE, to='projects.module')),
            ],
            options={
                'verbose_name': '接口模块',
                'verbose_name_plural': '接口模块',
                'db_table': 'tb_interface',
            },
        ),
        migrations.AddConstraint(
            model_name='interface',
            constraint=models.UniqueConstraint(fields=('name', 'module'), name='unique_interface_name'),
        ),
    ]