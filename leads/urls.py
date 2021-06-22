from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_list, name="lead-list"),
    path('create', lead_create, name="lead-create"),
    path('<pk>', lead_detail, name="lead-detail"),
    path('update/<pk>', lead_update_view, name="lead-update"),
    path('delete/<pk>', lead_del, name="lead-delete")
]
