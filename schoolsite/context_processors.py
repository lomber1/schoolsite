

def category_list(request):
    from categories.models import Category

    return {"category_list": Category.objects.all()}
