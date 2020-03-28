from django.urls import path
from api.views import product_list, product_detail,\
    category_list, category_detail, category_products
# from api import views

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>', product_detail),
    path('categories/', category_list),
    path('categories/<int:pk>/', category_detail),
    path('categories/<int:pk>/products/', category_products)
]