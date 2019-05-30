from catalog.models import Category
from django.http import Http404


def menu(request):
    categories = Category.objects.select_related('parent').all()
    path = request.path.rstrip('/').split('/')
    route, child_count, parent = [], {}, None
    slugs = path[2:]
    if 'product' in slugs:
        slugs = slugs[:-2]
    for slug in slugs:
        for category in categories:
            if slug == category.slug and category.parent == parent:
                parent = category
                route += ([(category, category.get_absolute_url())])
    if len(route) != len(slugs):
        raise Http404
    for category in categories:
        child_count[category] = []
    for category in categories:
        if category.parent_id:
            child_count[category.parent].append(category)
    categories_parent = [category for category in categories if category.parent is None]
    return {'categories': categories_parent, 'child_count': child_count, 'route': route}
