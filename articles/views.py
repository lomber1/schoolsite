from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleDetails(DetailView):
    model = Article
    template_name = "articles/article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = "adminpanel/forms/article/article_form.html"
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")
    raise_exception = True


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    template_name = "adminpanel/forms/article/article_update_form.html"
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")
    raise_exception = True


class ArticleDelete(LoginRequiredMixin, DeleteView):
    template_name = "adminpanel/forms/article/article_confirm_delete.html"
    model = Article
    success_url = reverse_lazy("adminpanel:articles_tab")
    raise_exception = True
