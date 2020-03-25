from django.urls import path, re_path
from api.views import product_list, product_detail, category_list, category_detail, cat_products

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>', product_detail),
    path('categories/', category_list),
    path('categories/<int:id>', category_detail),
    path('categories/<int:cat_id>/products', cat_products)
]
