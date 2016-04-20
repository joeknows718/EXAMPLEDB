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
def filter_date_and_sort_general(queryset, order):
	return queryset.filter(general_election_date__gte=date.today()).order_by(order).distinct('general_election_date')


@register.filter
def filter_date_and_sort_primary(queryset, order):
	return queryset.filter(primary_election_date__gte=date.today()).order_by(order).distinct()



@register.filter
def filter_date_and_sort_filing(queryset, order):
	return queryset.filter(next_filing_date__gte=date.today()).order_by(order).distinct()