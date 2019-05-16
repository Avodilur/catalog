# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)
    parent = models.IntegerField(default=0)
    url = models.CharField(max_length=30)

    def __str__(self):
        return {self.id: self.name}


class Product(models.Model):
    name = models.CharField(max_length=20),
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=30)
    image = models.CharField()
    count = models.IntegerField
    price = models.IntegerField

    def __str__(self):
        return {self.id: self.name}
