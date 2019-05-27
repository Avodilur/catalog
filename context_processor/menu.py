from catalog.models import Category


def menu(request):
    categories = Category.objects.filter(parent=None)
    return {'categories': categories}