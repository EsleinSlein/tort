from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from La_TORTE.models import Product, Category


class ProductListView(ListView):
    """Список товара"""
    model = Product
    queryset = Product.objects.filter(draft=False)
    context_object_name = 'product'
    paginate_by = 10


class ProductDetailView(DetailView):
    """Полное описание товара """
    model = Product
    queryset = Product.objects.filter(draft=False)
    slug_field = "url"


class ProductFilter(ListView):
    model = Product
    context_object_name = 'product'

    def get_queryset(self):
        if self.kwargs['cat_slug'] == 'popular':
            return Product.objects.filter(popular=True, draft=False)
        return Product.objects.filter(category__url=self.kwargs['cat_slug'], draft=False)
