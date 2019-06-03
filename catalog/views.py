# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from catalog.helpers import get_objects, get_product


def category(request, path):
    print path
    list_products, route = get_objects(path)
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/catalog.html', {'products': products, 'path': request.path.rstrip('/'), 'route': route})


def product(request, path, id):
    product, route = get_product(path, id)
    return render(request, 'catalog/product.html', {'product': product, 'route': route})



