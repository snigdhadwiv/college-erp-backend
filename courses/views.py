from rest_framework import viewsets
from .models import Course, Syllabus, Subject
from .serializers import CourseSerializer, SyllabusSerializer, SubjectSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

from rest_framework import viewsets
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Add this view for student's enrolled courses
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def student_enrollments(request, student_id):
    enrollments = Enrollment.objects.filter(student_id=student_id)
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)