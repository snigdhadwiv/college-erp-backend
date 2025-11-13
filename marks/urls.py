from django.urls import path
from . import views

urlpatterns = [
    # Add your marks routes here
    path('', views.marks_list, name='marks-list'),
]