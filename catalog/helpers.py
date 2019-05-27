from catalog.models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import Http404


def navigation(path):
    category = Category.objects.all()
    path = path.rstrip('/').split('/')
    route = []
    arr = reversed(path[2:])
    try:
        for item in arr:
            route += ([(category.get(slug=item), '/'.join(path))])
            path.pop()
        return list(reversed(route))
    except Category.DoesNotExist:
        raise Http404()


def get_objects(path):
    product = Product.objects.all()
    if path is not None:
        path = path.rstrip('/').split('/')[-1]
        product = product.filter(category__slug=path)
    return product


def get_product(path, id):
    try:
        product = get_object_or_404(Product, id=id)
        return product
    except Product.DoesNotExist:
        raise Http404()
