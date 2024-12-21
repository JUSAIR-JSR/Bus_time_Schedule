from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_buses, name='view_all_buses'),
]
