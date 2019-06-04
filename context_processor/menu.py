from catalog.models import Category


def menu(request):
    categories = Category.objects.all()
    child_count = {}
    for category in categories:
        child_count[category] = []
    for category in categories:
        if category.parent_id:
            child_count[category.parent].append(category)
    categories_parent = [category for category in categories if category.parent is None]
    return {'categories': categories_parent, 'child_count': child_count}
