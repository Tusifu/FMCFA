from django.urls import path
from workstation.views import hospitalViews
urlpatterns = [
    # path('create', hospitalViews.HospitalAgentCreateView.as_view(), name='create_hospitalAgent'),
    path('list', hospitalViews.HospitalList.as_view(), name='hospital_list'),
    # path('<str:id>/edit',hosAgentsViews.HospitalAgentUpdate.as_view(),name="hospitalAgent_edit"),
    # path('<str:id>/delete',hosAgentsViews.delete_hospitalAgent,name="hospitalAgent_delete"),
    # path('<str:id>/detail',hosAgentsViews.hospitalAgent_detail,name="hospitalAgent_detail"),

]

