from catalog.models import Category, Product
from django.http import Http404


categories = Category.objects.all()


def tree_categories():
    child_count = {}
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


def get_objects(path):
    products = Product.objects.all()
    child_count = tree_categories()
    route = []
    if path is not None:
        route, category = check_404(path)
        list_categories = get_categories(category, child_count)
        products = products.filter(category__in=list_categories)
    return products, route


def check_404(path):
    try:
        category = path.rstrip('/').split('/')[-1]
        category = categories.get(slug=category)
        route = breadcrumb(category)
        if path.rstrip('/') != '/'.join([category.slug for category in route]):
            raise Http404
        return route, category
    except Category.DoesNotExist:
        raise Http404


def get_product(path, id):
    try:
        route, category = check_404(path)
        product = Product.objects.get(id=id)
        return product, route
    except Product.DoesNotExist:
        raise Http404()
