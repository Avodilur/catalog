# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category
from .models import Product


def catalog(request):
    category = Category.objects.filter(parent=None)
    list_products = Product.objects.all()
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/catalog.html', {'categories': category, 'products': products})


def category(request, category, subcategory=''):
    category_url = category
    category = Category.objects.get(url=category)
    subcategories = Category.objects.filter(parent=category)
    if subcategory:
        subcategory = Category.objects.get(url=subcategory)
        list_products = Product.objects.filter(category=subcategory)
    else:
        list_products = Category.objects.filter(category=category)
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/category.html', {'subcategories': subcategories, 'products': products,
                                                     'category': category_url})
