# Generated by Django 2.0.6 on 2018-10-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片链接地址')),
                ('name', models.CharField(max_length=64, verbose_name='图片名称')),
                ('trackid', models.CharField(default='1', max_length=50, verbose_name='图片id')),
            ],
            options={
                'verbose_name': '轮播图表',
                'verbose_name_plural': '轮播图表',
                'db_table': 'axf_wheel',
            },
        ),
    ]
