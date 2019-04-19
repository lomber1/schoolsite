from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .models import Article
 

class ArticleDetails(DetailView):
    model = Article
    template_name = "articles/article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleCreate(CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")


class ArticleUpdate(UpdateView):
    model = Article
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("adminpanel:articles_tab")


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("adminpanel:articles_tab")
