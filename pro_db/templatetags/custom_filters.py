from django import template
from datetime import date

register = template.Library()

@register.filter(name='addcls')
def addcss(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)

@register.filter
def filter_date_and_sort(queryset, order):
	return queryset.filter(general_election_date__gt=date.today()).order_by(order)

