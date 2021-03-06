from django.shortcuts import render, redirect, get_object_or_404
import sweetify
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from beneficiary.models import Beneficiary,BeneficiaryForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from beneficiary.filters.beneficiary_filter import BeneficiaryFilter

# Create your views here.
"""
    declaration of some data
"""
success = 'Success!'
error = 'Error!'
error_message = 'Something Wrong Happened, please Try Again'

@method_decorator(login_required, name='dispatch')
class BeneficiaryCreateView(CreateView):
    model = Beneficiary
    class_form = BeneficiaryForm
    fields = '__all__'
    success_url = "list"
    template_name = "beneficiary/register_beneficiary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add"
        return context

    def get_success_url(self):
        sweetify.success(self.request, success, text='You have successfully Added Benificiary', icon='success', timerProgressBar='true', timer=3000)
        return reverse_lazy('list_beneficiary')

@method_decorator(login_required, name='dispatch')
class BeneficiaryDetailView(DetailView):
    model = Beneficiary
    template_name = "beneficiary/view_beneficiary.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class BeneficiaryListView(ListView):
    model = Beneficiary
    paginate_by = 5
    context_object_name = 'beneficiaries'
    template_name = "beneficiary/beneficiary_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["find"] = BeneficiaryFilter(
            self.request.GET, queryset=Beneficiary.objects.all().order_by("id"))
        return context

    def get_queryset(self):
        return BeneficiaryFilter(self.request.GET, queryset=Beneficiary.objects.all().order_by("id")).qs

@method_decorator(login_required, name='dispatch')
class BeneficiaryUpdateView(UpdateView):
    model = Beneficiary
    fields = '__all__'
    success_url = "view"
    template_name = 'beneficiary/update_beneficiary.html'
    context_object_name = 'beneficiary'

    def get_object(self):
        return Beneficiary.objects.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit"
        return context

    def get_success_url(self):
        sweetify.success(self.request, success, text='You have successfully Update Beneficiary info', icon='success', timerProgressBar='true', timer=3000)
        return reverse_lazy('list_beneficiary')

@login_required(login_url='/accounts/login')
def delete_beneficiary(request, id):
    beneficiary = get_object_or_404(Beneficiary, id=id)
    beneficiary.delete()
    sweetify.success(request, success, text='You have successfully deleted pharmacist', icon='success', timerProgressBar='true', timer=3000)
    return redirect('list_beneficiary')