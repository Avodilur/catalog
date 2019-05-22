# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse


def address(category):
    n = Category.objects.get(name=category)
    if n.parent is not None:
        return address(Category.objects.get(name=n.parent)) + '/' + str(n.slug)
    else:
        return str(n.slug)


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)
    slug = models.SlugField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent is None:
            return self.slug
        else:
            return '/' '/'.join([self.slug])


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.id
