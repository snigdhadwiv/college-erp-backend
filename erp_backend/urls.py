from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students import views as student_views
from attendance import views as attendance_views 
from courses import views as course_views

router = routers.DefaultRouter()
router.register(r'students', student_views.StudentViewSet)
router.register(r'attendance', attendance_views.AttendanceViewSet)
router.register(r'courses', course_views.CourseViewSet)
router.register(r'subjects', course_views.SubjectViewSet)
router.register(r'syllabus', course_views.SyllabusViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]