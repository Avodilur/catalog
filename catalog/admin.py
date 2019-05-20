# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin


from .models import Category
from .models import Product


admin.site.register(Category)
admin.site.register(Product)