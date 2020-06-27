
from django.urls import path
from Payment_Application import views

app_name = "Payment_Application"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('purchase/', views.payment, name="payment"),
    path('purchaseform/', views.paymentform, name="paymentform"),
    path('complete/', views.complete, name="complete"),
    path('orders/', views.order_view, name="orders"),
]