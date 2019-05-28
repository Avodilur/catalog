# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connection
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from catalog.helpers import navigation, get_objects, get_product


def category(request, path):
    before = len(connection.queries)
    route = navigation(request.path) if path else []
    list_products = get_objects(path)
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    print(len(connection.queries) - before)
    return render(request, 'catalog/catalog.html', {'products': products,
                                                    'route': route, 'path': path})


def product(request, path, id):
    product = get_product(path, id)
    return render(request, 'catalog/product.html', {'product': product})