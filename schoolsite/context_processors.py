from categories.models import Category


def get_categories(request):
	return {
		"category_list": Category.objects.all()
	}
