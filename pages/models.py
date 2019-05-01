# posts/models.py
from django.db import models

# Create your models here

class Person(models.Model):
    name = models.TextField()
    age = models.SmallIntegerField(default=None)


    def __str__(self):
        return self.name