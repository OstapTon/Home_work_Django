"""
URL configuration for home_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/create/', views.create_client_view, name='create_client'),
    path('clients/', views.all_clients_view, name='all_clients'),
    path('clients/<int:client_id>/update/', views.update_client_view, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client_view, name='delete_client'),
    path('clients/<int:client_id>/ordered_products/<int:days>/', views.client_ordered_products, name='client_ordered_products'),
    path('product/create/', views.create_product, name='create_product'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/update/', views.update_product_view, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product_view, name='delete_product'),

]
