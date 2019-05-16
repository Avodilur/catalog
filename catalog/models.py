# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gettext import Catalog

from django.db import models

# Create your models here.

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.IntegerField(default=0)
    url = models.CharField(max_length=30)
    image = models.CharField(max_length=30)

    def __str__(self):
        return [self.name, self.url, self.image]


class Product(models.Model):
    name = models.CharField(max_length=20),
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=30)
    image = models.CharField(max_length=30, default='')
    count = models.IntegerField
    price = models.IntegerField

    def __str__(self):
        return [self.name, self.image]


class Relation(models.Model):
    product_id = models.ForeignKey(Product)
    category_id = models.ForeignKey(Category)

    def __str__(self):
        return [self.product_id, self.category_id]