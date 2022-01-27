from inspect import modulesbyfile
from winsound import MB_ICONQUESTION
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name