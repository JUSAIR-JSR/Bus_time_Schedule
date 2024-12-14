from django.urls import path
from . import views

urlpatterns = [
    path('buses/', views.view_all_buses, name='view_all_buses'),
]
