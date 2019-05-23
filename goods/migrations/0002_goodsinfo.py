# Generated by Django 2.2 on 2019-05-19 08:56

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='goodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20, verbose_name='商品名称')),
                ('gpic', models.ImageField(blank=True, null=True, upload_to='goods', verbose_name='商品图片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('gunit', models.CharField(default='500g', max_length=20, verbose_name='商品单位')),
                ('gclick', models.IntegerField(default=0, verbose_name='点击量')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('gintro', models.CharField(max_length=200, verbose_name='简介')),
                ('gstock', models.IntegerField(verbose_name='库存')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='详细介绍')),
                ('gtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.typeInfo', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
    ]
