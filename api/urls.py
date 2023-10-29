from django.urls import path
from .views import article_list,product_list,home,select_product_list


urlpatterns = [
    path('articles/',article_list),
    path('products/',product_list),
    path('products/<int:pk>/',select_product_list),
    path('',home)
]