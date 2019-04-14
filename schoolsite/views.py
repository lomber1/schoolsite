from django.views.generic import *
from articles.models import Article


class HomeView(ListView):
    template_name = "home.html"
    model = Article
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ContactView(TemplateView):
    template_name = "contact.html"
