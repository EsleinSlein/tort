from django import template
from La_TORTE.models import Category, ProductDetail, Product

register = template.Library()


@register.inclusion_tag('La_TORTE/categories.html')
def get_category():
    cat = Category.objects.all
    return {'category': cat}

