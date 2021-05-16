from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.shortcuts import render, redirect
from django.views.generic import  ListView, View
from django.contrib.auth.decorators import login_required
from beneficiary.models import Beneficiary
from workers.filter import BeneficiaryFilter

from xhtml2pdf import pisa

"""
    Declaration os constants
"""
content_type = 'application/pdf'

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type=content_type)
    return None

@login_required(login_url='/accounts/login/')
def generate_pdf(request, *args, **kwargs):
    all_beneficiaries = Beneficiary.objects.all()
    my_filter = BeneficiaryFilter(request.POST, queryset= all_beneficiaries)
    filtered_beneficiaries = my_filter.qs
    if request.method == 'GET':
        return render(request, 'workers/make_report.html',{'my_filter':my_filter}) 
    else:

        data = {
            'filtered_beneficiaries' : filtered_beneficiaries,
            # 'title': report_title(request.POST['date_range']),
            'today': datetime.date.today(),
            'reporter':request.user.username,
            'number_of_data':len(filtered_beneficiaries)
        }
    pdf = render_to_pdf('workers/report_page.html', data)
    return HttpResponse(pdf, content_type=content_type)

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        all_beneficiaries = Beneficiary.objects.all()
        my_filter = BeneficiaryFilter(request.POST, queryset= all_beneficiaries)
        filtered_beneficiary = my_filter.qs

        data = {
            'filtered_beneficiary' : filtered_beneficiary,
            # 'title': report_title(request.POST['date_range']),
            'today': datetime.date.today(),
            'reporter':request.user.username,
            'number_of_data':len(filtered_beneficiary)
        }
        pdf = render_to_pdf('Document/report_page.html', data)
        response = HttpResponse(pdf, content_type=content_type)
        filename = "DLF_report_of %s"%(datetime.date.today())
        content = "attachment; filename='%s'"%(filename)
        response['content-Disposition'] = content
        return response
        




def report_title(date_range):
    if date_range == 'today':
        return  "Today's"
    elif date_range == 'month':
        return "Monthly"
    elif date_range == 'week':
        return 'weekly'
    elif date_range == 'yesterday':
        return 'Yesterday'
    elif date_range == 'year':
        return  'Annual'
    else:
        return 'Date Range'