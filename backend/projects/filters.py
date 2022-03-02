from django_filters import rest_framework as filters, IsoDateTimeFilter, DateFilter, DateTimeFilter
from django.db import models

from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    # created = filters.IsoDateTimeFromToRangeFilter()    # Интервал с часами и  минутами (DateTime)
    # created = filters.DateRangeFilter()                 # Интервал с временными интервалами (today, yesterday,..., this year)
    created = filters.DateFromToRangeFilter()           # интервал дат (наиболее подходящий

    class Meta:
        model = Todo
        fields = ['project', 'created']
