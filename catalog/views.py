# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from catalog.helpers import get_objects, get_product, pagination, tree_categories
from catalog.models import Product


products_name = list(Product.objects.all().values_list('name', flat=True))


def category(request, path):
    list_products, route = get_objects(path)
    page = request.GET.get('page', 1)
    products = pagination(list_products, page)
    return render(request, 'catalog/catalog.html', {'products': products, 'route': route})


def product(request, path, id):
    product, route = get_product(path, id)
    return render(request, 'catalog/product.html', {'product': product, 'route': route})


def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '').lower()
        results = [s for s in products_name if q in s.lower()]
        return JsonResponse(list(results), safe=False)
    else:
        q = request.GET.get('q', '')
        page = request.GET.get('page', 1)
        products, route = get_objects(q=q)
        products = pagination(products, page)
        return render(request, 'catalog/catalog.html', {'products': products, 'route': route, 'q': q})