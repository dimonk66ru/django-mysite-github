from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    ProductsDataExportView,
    OrdersDataExportView,
    ProductViewSet,
    OrderViewSet,
    UserOrdersListView,
    UserOrdersExportView,
    create_product,
    create_order,
)

app_name = "shopapp"

routers = DefaultRouter()
routers.register("products", ProductViewSet)
routers.register("orders", OrderViewSet)

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("api/", include(routers.urls)),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/export/", ProductsDataExportView.as_view(), name="products-export"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/export/", OrdersDataExportView.as_view(), name="orders-export"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("products/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("users/<int:user_id>/orders/", UserOrdersListView.as_view(), name="user_orders"),
    path("users/<int:user_id>/orders/export/", UserOrdersExportView.as_view(), name="user_orders_export"),
]
