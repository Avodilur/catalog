# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin



from .models import Category
from .models import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'image']
    prepopulated_fields = {'slug': ('name', )}
    exclude = ('level', )

    def save_model(self, request, obj, form, change):
        obj.level = obj.parent.level+1
        obj.full_clean()
        super(CategoryAdmin, self).save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'count', 'price', 'image']
    list_filter = ['category', 'count']
    list_editable = ['category', 'count', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)