from django.db import models
from django.utils.timezone import now
from django_extensions.db.fields import AutoSlugField

from categories.models import Category


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Tytuł"
    )
    body = models.TextField(blank=True, null=False, verbose_name="Tekst")
    author = models.CharField(max_length=150, null=True, verbose_name="Autor")
    publish_date = models.DateTimeField(default=now, verbose_name="Data dodania")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategoria"
    )
    is_visible = models.BooleanField(default=True, verbose_name="Czy widoczny?")
    slug = AutoSlugField(populate_from=["title"], verbose_name="Uproszczona nazwa")
    views = models.IntegerField(default=0, verbose_name="Wyświetlenia")
    thumbnail = models.ImageField(default="default_thumbnail.jpeg", blank=True)

    def get_short_body(self):
        return self.body[:250]

    def __str__(self):
        return self.title
