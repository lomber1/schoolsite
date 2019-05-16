from django.urls import path

from .views import IndexView, ArticlesTabView, LogsTabView, CategoriesTabView


app_name = "adminpanel"

urlpatterns = [
    path("", IndexView.as_view(), name="overview_tab"),
    path("wiadomosci/", ArticlesTabView.as_view(), name="articles_tab"),
    path("kategorie/", CategoriesTabView.as_view(), name="categories_tab"),
    path("raport/", ArticlesTabView.as_view(), name="logs_tab"),
    path("ustawienia/", ArticlesTabView.as_view(), name="settings_tab"),
]
