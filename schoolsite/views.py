from django.views.generic import *
from articles.models import Article
from django.views.decorators.gzip import gzip_page
from django.utils.decorators import method_decorator


# @method_decorator(gzip_page, name="dispatch")
class HomeView(ListView):
    template_name = "home.html"
    model = Article
    paginate_by = 100

    def get_queryset(self):
        return self.model.objects.filter(is_visible=True).order_by("-publish_date")
    

@method_decorator(gzip_page, name="dispatch")
class ContactView(TemplateView):
    template_name = "contact.html"
