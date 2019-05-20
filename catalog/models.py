# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gettext import Catalog

# Create your models here.
from IPython.core.debugger import Tracer
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)
    url = models.CharField(max_length=30)
    image = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=30, null=True, blank=True)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
