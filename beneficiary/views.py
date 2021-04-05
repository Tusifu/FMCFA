from django.shortcuts import render
from beneficiary.models import Beneficiary
from beneficiary.forms import BeneficiaryForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView

# Create your views here.

# def beneficiary_list(request):
#     beneficiary = Beneficiary.objects.all().order_by('date')
#     return render(request, 'article_list.html', {'articles': articles})


# def edit_beneficiary(request, slug):
#     beneficiary = Beneficiary.objects.get(slug=slug)
#     return render(request, 'article_detail.html', {'article': article})

class BeneficiaryCreateView(CreateView):
    model = Beneficiary
    class_form = BeneficiaryForm
    fields = '__all__'
    success_url = "list"
    template_name = "beneficiary/register_beneficiary.html"

class BeneficiaryDetailView(DetailView):
    model = Beneficiary
    template_name = "beneficiary/view_beneficiary.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BeneficiaryListView(ListView):
    model = Beneficiary
    context_object_name = 'beneficiaries'
    template_name = "beneficiary/beneficiary_list.html"

class BeneficiaryUpdateView(UpdateView):
    model = Beneficiary
    fields = '__all__'
    success_url = "view"
    template_name = 'beneficiary/update_beneficiary.html'
