from django.contrib import admin

from .models import Category, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "get_author",
        "publish_date",
        "category",
        "is_visible",
        "slug",
    )

    def get_author(self, obj):
        return obj.author

    get_author.admin_order_field = "author"
    get_author.short_description = "Autor"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )

    fieldsets = (
        ('Standard info', {
            'fields': ("title", )
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
