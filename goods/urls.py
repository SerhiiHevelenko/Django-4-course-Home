from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.CatalogViwe.as_view(), name='search'),
    path('<slug:category_slug>/', views.CatalogViwe.as_view(), name='index'),
    path('product/<slug:product_slug>/', views.ProductView.as_view(), name='product'),
]


