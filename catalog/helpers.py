from catalog.models import Category, Product
from django.http import Http404
from django.db import connection


def navigation(path):
    before = len(connection.queries)
    categories = Category.objects.select_related('parent').all()
    path = path.rstrip('/').split('/')
    route = []
    slugs = path[2:]
    parent = None
    for slug in slugs:
        for category in categories:
            if slug == category.slug and category.parent == parent:
                parent = category
                route += ([(category, category.get_absolute_url())])
    print 'navigation:', len(connection.queries) - before
    if len(route) == len(slugs):
        return route
    else:
        raise Http404


def get_objects(path):
    before = len(connection.queries)
    products = Product.objects.all()
    if path is not None:
        path = path.rstrip('/').split('/')[-1]
        list_categories = Category.objects.filter(parent__slug=path)
        if not list_categories:
            products = products.filter(category__slug=path)
        else:
            products = products.filter(category__in=list_categories)
    print 'get_objects:', len(connection.queries) - before
    return products


def get_product(path, id):
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        raise Http404()

