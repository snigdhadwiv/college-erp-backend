from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students import views as student_views

router = routers.DefaultRouter()
router.register(r'students', student_views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]