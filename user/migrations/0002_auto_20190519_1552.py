# Generated by Django 2.2 on 2019-05-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemailAddress',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ustockAddress',
            field=models.CharField(default='', max_length=30),
        ),
    ]