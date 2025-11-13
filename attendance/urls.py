from django.urls import path
from . import views

urlpatterns = [
    # Add your attendance routes here
    path('', views.attendance_list, name='attendance-list'),
]