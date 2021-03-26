"""Proyecto URL Configuration

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
from django.contrib import admin
from django.urls import path
from Proyecto.views import firtsView, index, index2
from Tienda.views import articulo, createArticulo, editArticulo, deleteArticulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firtsView),
    path('index/<int:agno>/<int:actual>/', index),
    path('index2/', index2),
    path('articulos/', articulo, name = 'articulo'),
    path('createArticulo/', createArticulo, name = 'create_articulo'),
    path('editArticulo/<int:id>/', editArticulo, name = 'edit_articulo'),
    path('deleteArticulo/<int:id>/', deleteArticulo, name = 'delete_articulo'),
]
