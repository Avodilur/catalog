def navigation(request):
    from catalog.models import Category
    path = request.path.rstrip('/').split('/')
    route = []
    arr = path[2:]
    arr.reverse()
    for item in arr:
        route += ([(Category.objects.get(slug=item).name, '/'.join(path))])
        path.pop()
    return list(reversed(route))


def get_objects(path, category, product):
    Category, Product = category, product
    if path[0] is not None:
        path = path[0].rstrip('/').split('/')
        category = Category.objects.get(slug=path[-1])
        catalog = Category.objects.get(slug=path[0])
        return Category.objects.filter(parent=catalog), Product.objects.filter(category=category)
    else:
        return Category.objects.filter(parent=None), Product.objects.all()