from django.contrib import admin
from django.urls import path, include
from accounts.views import render_dashboard

urlpatterns = [
    path('', admin.site.urls),
    path('dashboard/', render_dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('beneficiary/', include('beneficiary.urls')),
]
 