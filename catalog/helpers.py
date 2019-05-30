from catalog.models import Category, Product
from django.http import Http404


def get_objects(request, path):
    products = Product.objects.all()
    search_product = request.GET.get('search_product', '')
    if path is not None:
        path = path.rstrip('/').split('/')[-1]
        list_categories = Category.objects.filter(parent__slug=path)
        if not list_categories:
            products = products.filter(category__slug=path)
        else:
            products = products.filter(category__in=list_categories)
    return products.filter(name__icontains=search_product)


def get_product(path, id):
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        raise Http404()

