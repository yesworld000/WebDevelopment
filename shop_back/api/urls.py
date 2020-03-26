from django.urls import path
from api.views import product_list, product_detail, category_list, category_detail
from api import views

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>', product_detail),
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    # path('categories/<int:pk>/products/', views.category_product)
]