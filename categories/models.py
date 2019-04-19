from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Nazwa", null=False, blank=False
    )
    slug = AutoSlugField(populate_from=["title"], verbose_name="Uproszczona nazwa")

    def __str__(self):
        return self.title
