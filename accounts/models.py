from django.db import models
from accounts.models import *


class reg(models.Model):
    username=models.CharField(max_length=150,unique=True)
    email=models.CharField(max_length=150,unique=True)
    password=models.CharField(max_length=150,unique=True)
    confirmpassword=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class log(models.Model):
    username=models.CharField(max_length=150,unique=True)
    password=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return '{}'.format(self.name)
