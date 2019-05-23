# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin


from .models import Category
from .models import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'image']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'price', 'image']
    list_filter = ['category', 'count']
    list_editable = ['count', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)