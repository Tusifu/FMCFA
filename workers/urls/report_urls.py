from django.urls import path
from workers.views.FMCFA_reports import generate_pdf, DownloadPDF

app_name = 'reports'

urlpatterns = [
    path('', generate_pdf, name='generate_report'),
    path('download',DownloadPDF.as_view(), name='download_pdf')

]