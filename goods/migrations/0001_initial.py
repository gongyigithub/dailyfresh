# Generated by Django 2.2 on 2019-05-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='typeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20, verbose_name='商品分类')),
                ('isDelete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
        ),
    ]
