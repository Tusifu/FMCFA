import django_filters
from django_filters import CharFilter
from django.db.models import Q
from workstation.models.pharmacy import Pharmacy

# class for filter the knowledge base and render the list conditionally
class PharmacyFilter(django_filters.FilterSet):
    search = CharFilter(method='Pharmacy_custom_filter' ,field_name='search', label='')

    class Meta:
        model = Pharmacy
        fields = ['search']

    def Pharmacy_custom_filter(self, queryset, name, value):
        return Pharmacy.objects.filter(
            Q(name__icontains=value) | Q(address__icontains=value) | Q(phone__icontains=value) | Q(email__icontains=value)).order_by("id")
        
