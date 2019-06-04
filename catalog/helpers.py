from catalog.models import Category, Product
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def tree_categories():
    child_count = {}
    categories = Category.objects.all()
    for category in categories:
        child_count[category] = []
    for category in categories:
        if category.parent_id:
            child_count[category.parent].append(category)
    return child_count


def breadcrumb(category):
    child_count = tree_categories()
    for (parent, child) in child_count.items():
        if category in child:
            return breadcrumb(parent) + [category]
    return [category]


def get_categories(category, child_count):
    categories = [category]
    for child in child_count[category]:
        if child_count[child]:
            categories.extend(get_categories(child, child_count))
        categories.append(child)
    return categories


def get_objects(path=None, q=''):
    products = Product.objects.all()
    child_count = tree_categories()
    route = []
    if path is not None:
        route, category = check_404(path)
        list_categories = get_categories(category, child_count)
        products = products.filter(category__in=list_categories)
    return products.filter(name__icontains=q), route


def check_404(path):
    category = path.rstrip('/').split('/')[-1]
    try:
        category = Category.objects.get(slug=category)
    except Category.DoesNotExist:
        raise Http404
    route = breadcrumb(category)
    if path.rstrip('/') != '/'.join([category.slug for category in route]):
        raise Http404
    return route, category


def get_product(path, pk):
    route, category = check_404(path)
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404()
    return product, route


def pagination(list_products, page):
    paginator = Paginator(list_products, 12)
    try:
        list_products = paginator.page(page)
    except PageNotAnInteger:
        list_products = paginator.page(1)
    except EmptyPage:
        list_products = paginator.page(paginator.num_pages)
    return list_products