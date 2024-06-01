"""
URL configuration for test_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from backend_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/', MaterialView.as_view(), name='material'),
    path('materials/<int:pk>', MaterialDetailView.as_view(), name='material_detail'),
    path('categories/', CategoryView.as_view(), name='category'),
    path('categories-full-flat/', CategoryWithMaterialsFlatView.as_view(), name='category_full_flat'),
    path('categories-full/', CategoryWithMaterialsView.as_view(), name='category_full')
]
