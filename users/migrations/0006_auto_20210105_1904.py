# Generated by Django 3.1.3 on 2021-01-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210101_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, verbose_name='Имя пользователя'),
        ),
    ]
