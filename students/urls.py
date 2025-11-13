from django.urls import path
from . import views

urlpatterns = [
    # Add your student routes here
    path('', views.student_list, name='student-list'),
]