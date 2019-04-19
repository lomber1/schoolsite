from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category

# Create your views here.
@method_decorator(login_required, name="dispatch")
class CategoryList(ListView):
    template_name = "adminpanel/categories.html"
    model = Category
    paginate_by = 100
    ordering = ["title"]


@method_decorator(login_required, name="dispatch")
class CategoryAdd(CreateView):
    template_name = "adminpanel/forms/category/category_form.html"
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:categories_tab")


@method_decorator(login_required, name="dispatch")
class CategoryUpdate(UpdateView):
    template_name = "adminpanel/forms/category/category_update_form.html"
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("adminpanel:categories_tab")


@method_decorator(login_required, name="dispatch")
class CategoryDelete(DeleteView):
    template_name = "adminpanel/forms/category/category_confirm_delete.html"
    model = Category
    success_url = reverse_lazy("adminpanel:categories_tab")