from django.urls import path

from django.views.generic import RedirectView
from .views import ArticleDetails, ArticleCreate, ArticleDelete, ArticleUpdate


app_name = "articles"

urlpatterns = [
    path("", RedirectView.as_view(
        url='/'), name="article_list"),
    path("dodaj/", ArticleCreate.as_view(), name="article_create"),
    path("<slug:slug>/usun", ArticleDelete.as_view(), name="article_delete"),
    path("<slug:slug>/edytuj", ArticleUpdate.as_view(), name="article_update"),
    path("<slug:slug>/", ArticleDetails.as_view(), name="article_details"),
]
