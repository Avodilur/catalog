# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from collections import OrderedDict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Category
from .models import Product


def example(request):
    path = request.path.split('/')[:-1]
    route = {}
    arr = path[2:]
    arr.reverse()
    for item in arr:
        route.update([(Category.objects.get(slug=item).name, '/'.join(path))])
        path.pop()
    return route


def category(request, *args, **kwargs):
    if args:
        args = args[0].split('/')
        category = Category.objects.get(slug=args[-1])
        catalog = Category.objects.get(slug=args[0])
        if category.parent is not None:
            categories = Category.objects.filter(parent=category.parent.id)
        else:
            categories = Category.objects.filter(parent=None)
        list_products = Product.objects.filter(category=category)
    else:
        categories = Category.objects.filter(parent=None)
        list_products = Product.objects.all()
    paginator = Paginator(list_products, 12)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    route = example(request)
    route = OrderedDict(reversed(list(route.items())))
    # for item in products:
    #     if item.image is None:
    #         item.image = category.image or category.parent.image
    return render(request, 'catalog/catalog.html', {'categories': categories, 'products': products, 'route': route})