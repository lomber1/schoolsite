from django.shortcuts import render
from django.views.generic import *

from .models import Article


# Create your views here.
class ArticleDetails(DetailView):
    model = Article
    template_name = "articles/article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
