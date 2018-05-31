import os
import uuid
from django.db import models


class CommonModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Position(CommonModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return self.name


def upload_avatar(instance, filename):
    extension = os.path.splitext(filename)[1]
    avatar_path = 'avatar/'
    format_pattern = '{}-{}' + extension
    return avatar_path + format_pattern.format(uuid.uuid4(), uuid.uuid4())


class Employee(CommonModel):
    SEX_CHOICES = (
        (1, 'Male'),
        (2, 'Female')
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    avatar = models.ImageField(upload_to=upload_avatar)
    address = models.TextField()
    sex = models.IntegerField(default=1, choices=SEX_CHOICES)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'