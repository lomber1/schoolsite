from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import *
from django.views.generic.edit import *

from articles.models import Article, Category


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "adminpanel/index.html"


@method_decorator(login_required, name="dispatch")
class ArticlesTabView(ListView):
    template_name = "adminpanel/articles.html"
    model = Article
    paginate_by = 100
    ordering = ["-publish_date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


@method_decorator(login_required, name="dispatch")
class LogsTabView(TemplateView):
    template_name = "adminpanel/logs.html"


@method_decorator(login_required, name="dispatch")
class SettingsTabView(TemplateView):
    template_name = "adminpanel/settings.html"


@method_decorator(login_required, name="dispatch")
class CategoriesTabView(ListView):
    template_name = "adminpanel/categories.html"
    model = Category
    paginate_by = 100
    ordering = ["title"]

    def get_context_data(self, **kwargs):
        context = super(CategoriesTabView, self).get_context_data(**kwargs)
        
        return context
