from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('templatetags/categories.html')
def categories():
    category = Category.objects.all()
    return {'category':category}