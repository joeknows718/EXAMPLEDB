from django import template

register = template.Library()

@register.filter(name='addcls')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)