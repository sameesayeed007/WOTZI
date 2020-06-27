
from django.urls import path
from Shop_Application import views

app_name = 'Shop_Application'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('Accessories', views.Accessories, name='accessories'),
    path('Clothing', views.Clothing, name='clothing'),
    path('EyeWear', views.EyeWear, name='eyewear'),
    path('Electronics', views.Electronics, name='electronics'),
    path('Timepieces', views.Timepieces, name='timepieces'),
]