# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
    slug = models.SlugField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent is None:
            return '/catalog/%s' % self.slug
        else:
            return '%s/%s' % (self.parent.get_absolute_url(), self.slug)


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    category = models.ForeignKey(Category, related_name='products', null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '%s/product/%s' % (self.category.get_absolute_url(), self.id)

    def get_image(self):
        if not self.image:
            return Category.objects.get(products=self.id, parent=None).image
        else:
            return self.image
