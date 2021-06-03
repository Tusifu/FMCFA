from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
import sweetify
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from workstation.models.hospital import Hospital, HospitalForm
from workstation.filters.hospital_filter import HospitalFilter


# Create your views here.
"""
    declaration of some data
"""
hospital_list_template = 'workstation/hospital/hospital_list.html'
create_hospital_template = 'workers/hospital/hospital_form.html'
success = 'Success!'
error = 'Error!'
error_message = 'Something Wrong Happened, please Try Again'


@method_decorator(login_required, name='dispatch')
class HospitalList(ListView):
    model = Hospital
    template_name = hospital_list_template
    paginate_by = 5
    context_object_name = 'hospitals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["find"] = HospitalFilter(
            self.request.GET, queryset=Hospital.objects.all().order_by("id"))
        return context

    def get_queryset(self):
        return HospitalFilter(self.request.GET, queryset=Hospital.objects.all().order_by("id")).qs



# @method_decorator(login_required, name='dispatch')
# class HospitalAgentCreateView(CreateView):
#     model = HospitalAgent
#     template_name = create_hosAgent_template
#     form_class = HospitalAgentForm


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Add"
#         return context

#     def get_success_url(self):
#         sweetify.success(self.request, success, text='You have successfully Added HospitalAgent', icon='success', timerProgressBar='true', timer=3000)
#         return reverse_lazy('hospitalAgent_list')



    
# @method_decorator(login_required, name='dispatch')
# class HospitalAgentUpdate(UpdateView):
#     model = HospitalAgent
#     form_class = HospitalAgentForm
#     template_name = create_hosAgent_template
#     context_object_name = 'hospitalAgent'

#     def get_object(self):
#         return HospitalAgent.objects.get(id=self.kwargs['id'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Edit"
#         return context

#     def get_success_url(self):
#         sweetify.success(self.request, success, text='You have successfully Update HospitalAgent info', icon='success', timerProgressBar='true', timer=3000)
#         return reverse_lazy('hospitalAgent_list')


# @login_required(login_url='/accounts/login')
# def hospitalAgent_detail(request, id):
#     hospitalAgent = get_object_or_404(HospitalAgent, id=id)
#     context = {
#         'hospitalAgent': hospitalAgent,
#     }
#     return render(request, 'workers/hosAgent/hosAgent_detail.html', context)


# @login_required(login_url='/accounts/login')
# def delete_hospitalAgent(request, id):
#     hosAgent = get_object_or_404(HospitalAgent, id=id)
#     hosAgent.delete()
#     sweetify.success(request, success, text='You have successfully deleted Hospital Agent', icon='success', timerProgressBar='true', timer=3000)
#     return redirect('hospitalAgent_list')
