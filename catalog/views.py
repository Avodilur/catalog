# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Category, Product
from .function.views import navigation, get_objects


def category(request, *args, **kwargs):
    categories, list_products = get_objects(args, category=Category, product=Product)
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    route = navigation(request)
    for item in products:
        if not item.image:
            item.image = Category.objects.get(product=item, parent=None).image
    return render(request, 'catalog/catalog.html', {'categories': categories, 'products': products, 'route': route})