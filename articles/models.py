from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nazwa", null=False, blank=False)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Tytuł")
    body = models.TextField(blank=True, null=False, verbose_name="Tekst")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Autor")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategoria")
    is_visible = models.BooleanField(default=True, verbose_name="Aktywny?")
    slug = AutoSlugField(populate_from=["title"], verbose_name="Uproszczona nazwa")

    def __str__(self):
        return self.title
