from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=50)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=50)
