# Generated by Django 2.0.5 on 2018-05-25 07:32

import curd_manage.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField()),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('avatar', models.ImageField(upload_to=curd_manage.models.upload_avatar)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd_manage.Position'),
        ),
    ]
