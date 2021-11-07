from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail_prod'),
    path('category/<slug:cat_slug>/', views.ProductFilter.as_view(), name='filter_prod')
]
