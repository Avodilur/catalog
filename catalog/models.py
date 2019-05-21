# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse


def address(category):
    n = Category.objects.get(name=category)
    if n.parent is not None:
        return address(Category.objects.get(name=n.parent))+'/'+str(n.url)
    else:
        return str(n.url)


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)
    url = models.CharField(max_length=30)
    image = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[address(self.name)])


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=30, null=True, blank=True)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
