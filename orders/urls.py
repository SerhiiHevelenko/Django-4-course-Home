from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderViev.as_view(), name='create_order'),
]