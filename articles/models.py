from django.db import models
from django.utils.html import strip_tags
from django.utils.timezone import now
from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField

from categories.models import Category


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Tytuł"
    )
    body = RichTextField(config_name='awesome_ckeditor')
    publish_date = models.DateTimeField(default=now, verbose_name="Data dodania")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategoria"
    )
    is_visible = models.BooleanField(default=True, verbose_name="Czy widoczny?")
    slug = AutoSlugField(populate_from=["title"], verbose_name="Uproszczona nazwa")
    views = models.IntegerField(default=0, verbose_name="Wyświetlenia")
    thumbnail = models.ImageField(default="default_thumbnail.jpeg", blank=True, verbose_name="Miniaturka")

    def get_short_body(self):
        return strip_tags(self.body[:250])

    def __str__(self):
        return self.title
