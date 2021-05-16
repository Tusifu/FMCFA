from django.contrib import admin
from django.urls import path, include
from accounts.views import render_dashboard

urlpatterns = [
    path('', admin.site.urls),
    path('dashboard/', render_dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('beneficiary/', include('beneficiary.urls')),
    path('drug/', include('drugs.urls')),
    path('pharmacist/', include('workers.urls.pharmacist_urls')),
    path('hospitalAgent/', include('workers.urls.hosAgent_urls')),
    path('report/', include('workers.urls.report_urls')),
]
 