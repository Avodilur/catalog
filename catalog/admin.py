# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from django import forms


from .models import Category
from .models import Product


class MyCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'level': forms.HiddenInput(),
        }

    def clean_level(self):
        parent = self.cleaned_data['parent']
        self.cleaned_data['level'] = parent.level + 1
        if self.cleaned_data['level'] == 3:
            raise forms.ValidationError('')
        else:
            return self.cleaned_data['level']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'image')
    prepopulated_fields = {'slug': ('name', )}
    form = MyCategoryAdminForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'count', 'price', 'image']
    list_filter = ['category', 'count']
    list_editable = ['category', 'count', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)