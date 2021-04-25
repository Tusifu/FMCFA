from django.contrib import admin
from django.urls import path
from beneficiary import views

urlpatterns = [
    path('create', views.BeneficiaryCreateView.as_view(), name='create_beneficiary'),
    path('list', views.BeneficiaryListView.as_view(), name='list_beneficiary'),
    path('<int:pk>/view', views.BeneficiaryDetailView.as_view(), name='detail_beneficiary'),
    path('<int:pk>/update', views.BeneficiaryUpdateView.as_view(), name='update_beneficiary'),
    path('<str:id>/delete',views.delete_beneficiary,name="beneficiary_delete"),
]
 