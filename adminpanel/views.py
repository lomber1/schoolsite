from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from articles.models import Article, Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "adminpanel/index.html"


class ArticlesTabView(LoginRequiredMixin, ListView):
    template_name = "adminpanel/articles.html"
    model = Article
    paginate_by = 10
    ordering = ["-publish_date"]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class LogsTabView(LoginRequiredMixin, TemplateView):
    template_name = "adminpanel/logs.html"
    raise_exception = True


class SettingsTabView(LoginRequiredMixin, TemplateView):
    template_name = "adminpanel/settings.html"
    raise_exception = True


class CategoriesTabView(LoginRequiredMixin, ListView):
    template_name = "adminpanel/categories.html"
    model = Category
    paginate_by = 100
    ordering = ["title"]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(CategoriesTabView, self).get_context_data(**kwargs)
        
        return context
