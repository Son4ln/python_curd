# Generated by Django 2.0.5 on 2018-05-31 02:51

import curd_manage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd_manage', '0005_auto_20180530_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(upload_to=curd_manage.models.upload_avatar),
        ),
    ]