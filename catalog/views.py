# -*- coding: utf-8 -*-
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Category, Product
from catalog.helpers import navigation, get_objects


def category(request, path):
    categories, list_products = get_objects(path)
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    route = navigation(request.path)
    for item in products:
        if not item.image:
            item.image = Category.objects.get(product=item, parent=None).image
    return render(request, 'catalog/catalog.html', {'categories': categories, 'products': products,
                                                    'route': route, 'path': path})
