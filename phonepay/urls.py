from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment-initiate', views.initiate_payment, name='initiate_payment'),
    path('callback', views.payment_callback, name='callback'),
]
