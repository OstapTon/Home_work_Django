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
from .views import (
    create_client, client_list, client_detail, update_client, delete_client,
    create_product, product_list, product_detail, update_product, delete_product,
    create_order, order_list, order_detail, update_order, delete_order
)

urlpatterns = [
    # Client URLs
    path('clients/', client_list, name='client_list'),
    path('client/new/', create_client, name='create_client'),
    path('client/<int:pk>/', client_detail, name='client_detail'),
    path('client/<int:pk>/edit/', update_client, name='update_client'),
    path('client/<int:pk>/delete/', delete_client, name='delete_client'),

    # Product URLs
    path('products/', product_list, name='product_list'),
    path('product/new/', create_product, name='create_product'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', update_product, name='update_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),

    # Order URLs
    path('orders/', order_list, name='order_list'),
    path('order/new/', create_order, name='create_order'),
    path('order/<int:pk>/', order_detail, name='order_detail'),
    path('order/<int:pk>/edit/', update_order, name='update_order'),
    path('order/<int:pk>/delete/', delete_order, name='delete_order'),
]

