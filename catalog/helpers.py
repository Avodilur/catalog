from catalog.models import Category, Product
from django.http import Http404


def navigation(path):
    categories = Category.objects.all()
    path = path.rstrip('/').split('/')
    route = []
    slugs = path[2:]
    parent = None
    for slug in slugs:
        for category in categories:
            if slug == category.slug and category.parent == parent:
                parent = category
                route += ([(category, category.get_absolute_url())])
    if len(route) == len(slugs):
        return route
    else:
        raise Http404


def get_objects(path):
    products = Product.objects.all()
    if path is not None:
        path = path.rstrip('/').split('/')[-1]
        list_categories = Category.objects.filter(parent__slug=path)
        if not list_categories:
            products = products.filter(category__slug=path)
        else:
            products = products.filter(category__in=list_categories)
    return products


def get_product(path, id):
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        raise Http404()

