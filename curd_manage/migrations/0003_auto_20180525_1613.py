# Generated by Django 2.0.5 on 2018-05-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd_manage', '0002_employee_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
    ]
