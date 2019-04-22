"""schoolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, ContactView, LessonTableView
from .views import view_404, view_403, view_401

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="homepage"),
    path("accounts/", include("accounts.urls")),
    path("wiadomosci/", include("articles.urls")),
    path("kategorie/", include("categories.urls")),
    path("panel/", include("adminpanel.urls")),
    path("plan_lekcji/", LessonTableView.as_view(), name="lesson_table"),
    path("kontakt/", ContactView.as_view(), name="contact"),
    path("", include("pwa.urls")),
    path("404/", view_404),
    path("403/", view_403),
    path("401/", view_401),
]

handler404 = view_404
handler403 = view_403
handler401 = view_401

# Development settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Production settings
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
