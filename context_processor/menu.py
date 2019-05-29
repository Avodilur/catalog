from catalog.models import Category
from django.db import connection


def menu(request):
    categories = Category.objects.select_related('parent').all()
    child_count = {}
    for category in categories:
        child_count[category] = []

    for category in categories:
        if category.parent_id:
            child_count[category.parent].append(category)

    categories_parent = [category for category in categories if category.parent is None]
    return {'categories': dict((k, child_count[k]) for k in categories_parent), 'child_count': child_count}
