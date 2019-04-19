from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = "adminpanel/index.html"


@method_decorator(login_required, name="dispatch")
class ArticlesTabView(TemplateView):
    template_name = "adminpanel/articles.html"


@method_decorator(login_required, name="dispatch")
class LogsTabView(TemplateView):
    template_name = "adminpanel/logs.html"


@method_decorator(login_required, name="dispatch")
class SettingsTabView(TemplateView):
    template_name = "adminpanel/settings.html"
