# Generated by Django 2.2 on 2019-05-19 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190519_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_title', to='goods.typeInfo', verbose_name='所属分类'),
        ),
    ]
