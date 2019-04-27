from django.contrib import admin

from .models import Category, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "publish_date",
        "category",
        "is_visible",
        "slug",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

    fieldsets = (("Standard info", {"fields": ("title",)}),)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
