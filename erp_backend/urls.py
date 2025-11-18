from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students import views as student_views
from attendance import views as attendance_views 
from courses import views as course_views
# Remove marks import for now

router = routers.DefaultRouter()
router.register(r'students', student_views.StudentViewSet)
router.register(r'attendance', attendance_views.AttendanceViewSet)
router.register(r'courses', course_views.CourseViewSet)
router.register(r'subjects', course_views.SubjectViewSet)
router.register(r'syllabus', course_views.SyllabusViewSet)
# Remove marks line for now

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
]