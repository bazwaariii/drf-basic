from django.contrib import admin
from django.urls import path
from core.views import ProductListCreateAPIView, ProductDetailAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    
    # PASTIKAN ADA SLASH DI BELAKANG pk/
    path('products/<uuid:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]