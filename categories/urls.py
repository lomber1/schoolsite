from django.urls import path

from .views import CategoryList, CategoryAdd, CategoryUpdate, CategoryDelete


app_name = "categories"

urlpatterns = [
    path("", CategoryList.as_view(), name="category_list"),
    path("dodaj/", CategoryAdd.as_view(), name="category_create"),
    path("<slug:slug>/edytuj/", CategoryUpdate.as_view(), name="category_update"),
    path("<slug:slug>/usun/", CategoryDelete.as_view(), name="category_delete"),

]
