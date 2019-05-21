# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from django.conf.urls import url


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)
    slug = models.SlugField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent is not None:
            return '/'.join(self.parent.get_absolute_url(), self.slug)
        else:
            return self.slug


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
