from django.urls import path
from . import views

urlpatterns = [
    # Add your faculty routes here
    path('', views.faculty_list, name='faculty-list'),
]