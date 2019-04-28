import bleach
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import *

from .models import Article


class ArticleDetails(DetailView):
    model = Article
    template_name = "articles/article_details.html"

    def get_queryset(self):
        article = self.model.objects.filter(slug=self.kwargs["slug"])
        article.update(views=F("views") + 1)

        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = "adminpanel/forms/article/article_form.html"
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:articles_tab")
    raise_exception = True

    def form_valid(self, form):
        bleach.sanitizer.ALLOWED_TAGS.append("p")
        bleach.sanitizer.ALLOWED_TAGS.append("u")
        bleach.sanitizer.ALLOWED_TAGS.append("td")
        bleach.sanitizer.ALLOWED_TAGS.append("tr")
        bleach.sanitizer.ALLOWED_TAGS.append("hr")
        bleach.sanitizer.ALLOWED_TAGS.append("img")
        bleach.sanitizer.ALLOWED_TAGS.append("span")
        bleach.sanitizer.ALLOWED_TAGS.append("h1")
        bleach.sanitizer.ALLOWED_TAGS.append("h2")
        bleach.sanitizer.ALLOWED_TAGS.append("h3")
        bleach.sanitizer.ALLOWED_TAGS.append("h4")
        bleach.sanitizer.ALLOWED_TAGS.append("h5")
        bleach.sanitizer.ALLOWED_TAGS.append("h6")
        bleach.sanitizer.ALLOWED_TAGS.append("kbd")
        bleach.sanitizer.ALLOWED_TAGS.append("cite")
        bleach.sanitizer.ALLOWED_TAGS.append("s")
        bleach.sanitizer.ALLOWED_TAGS.append("table")
        bleach.sanitizer.ALLOWED_TAGS.append("tbody")
        form.instance.body = bleach.clean(form.instance.body)

        return super().form_valid(form)


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
