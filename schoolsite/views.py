from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.views.generic import *

from articles.models import Article


@method_decorator(gzip_page, name="dispatch")
class HomeView(ListView):
    template_name = "home.html"
    model = Article
    paginate_by = 100

    def get_queryset(self):
        return self.model.objects.filter(is_visible=True).order_by("-publish_date")


@method_decorator(gzip_page, name="dispatch")
class LessonTableView(TemplateView):
    template_name = "lesson_table.html"


@method_decorator(gzip_page, name="dispatch")
class ContactView(TemplateView):
    template_name = "contact.html"


def view_404(request, exception=None):
    context = {
        "code": 404,
        "message": "Strona nie została znaleziona."
    }

    return render(request, "error.html", context)


def view_403(request, exception=None):
    context = {
        "code": 403,
        "message": "Próbuj dalej XD"
    }

    return render(request, "error.html", context)


def view_401(request, exception=None):
    context = {"code": 401, "message": "Próbuj dalej XD", }

    return render(request, "error.html", context)
