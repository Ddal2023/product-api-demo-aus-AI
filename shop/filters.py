import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):

    # name = django_filters.CharFilter(lookup_expr='icontains')
    # price = django_filters.RangeFilter()

    # диапазон для цены
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    # диапазон для даты создания
    created_after = django_filters.DateFilter(field_name="created", lookup_expr="gte")
    created_before = django_filters.DateFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
