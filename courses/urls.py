from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'enrollments', views.EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:student_id>/enrollments/', views.student_enrollments, name='student-enrollments'),
]