# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category
from .models import Product


def product(request):
    list_products = Product.objects.all()
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    vars = dict(products=products)


def catalog(request):
    category = Category.objects.filter(parent=0)


def category(request, category):
    id = request.GET.get("page", "1")
    category = Category.objects.get(name=category).id
    subcategory = Category.objects.filter(parent=category)


def subcategory(request, category, subcategory):
    id = request.GET.get("page", "1")
