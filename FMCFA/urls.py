from django.contrib import admin
from django.urls import path, include
from accounts.views import render_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', render_dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('pharmacist/', include('workers.urls.pharmacist_urls')),
]
