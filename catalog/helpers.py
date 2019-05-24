from catalog.models import Category, Product
from django.shortcuts import get_object_or_404


def navigation(path):
    path = path.rstrip('/').split('/')
    route = []
    arr = reversed(path[2:])
    for item in arr:
        route += ([(get_object_or_404(Category, slug=item), '/'.join(path))])
        path.pop()
    return list(reversed(route))


def get_objects(path):
    categories = Category.objects.filter(parent=None)
    if path is not None:
        path = path.rstrip('/').split('/')
        category = get_object_or_404(Category, slug=path[-1])
        categories = Category.objects.get(slug=path[-1]).child.all()
        return categories, Product.objects.filter(category=category)
    else:
        return categories, Product.objects.all()

