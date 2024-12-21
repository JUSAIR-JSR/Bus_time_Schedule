from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('show/', views.show, name='show'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
