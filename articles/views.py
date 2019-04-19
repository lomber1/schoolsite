from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Article


class ArticleDetails(DetailView):
    model = Article
    template_name = "articles/article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

@method_decorator(login_required, name="dispatch")
class ArticleCreate(CreateView):
    template_name = "adminpanel/forms/article/article_form.html"
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")

@method_decorator(login_required, name="dispatch")
class ArticleUpdate(UpdateView):
    template_name = "adminpanel/forms/article/article_update_form.html"
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")

@method_decorator(login_required, name="dispatch")
class ArticleDelete(DeleteView):
    template_name = "adminpanel/forms/article/article_confirm_delete.html"
    model = Article
    success_url = reverse_lazy("adminpanel:articles_tab")
