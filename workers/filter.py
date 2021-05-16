import django_filters
from django_filters import CharFilter
from beneficiary.models import Beneficiary
from django_filters import DateRangeFilter, DateFilter, DateTimeFilter
from django.db.models import Q
from django.forms import Select, TextInput, SelectMultiple

class BeneficiaryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Beneficiary 
        fields = ['id']

