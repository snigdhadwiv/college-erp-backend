from django.urls import path
from . import views

urlpatterns = [
    # Add your course routes here
    path('', views.course_list, name='course-list'),
]