import django_filters
from django_filters import CharFilter
from django.db.models import Q
from workstation.models.hospital import Hospital

# class for filter the knowledge base and render the list conditionally
class HospitalFilter(django_filters.FilterSet):
    search = CharFilter(method='Hospital_custom_filter' ,field_name='search', label='')

    class Meta:
        model = Hospital
        fields = ['search']

    def Hospital_custom_filter(self, queryset, name, value):
        return Hospital.objects.filter(
            Q(name__icontains=value) | Q(address__icontains=value)).order_by("id")
        
