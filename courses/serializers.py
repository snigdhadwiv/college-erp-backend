from rest_framework import serializers
from .models import Course, Syllabus, Subject

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'

from rest_framework import serializers
from .models import Course, Subject, Syllabus, Assignment, Enrollment
from users.serializers import UserSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'course_name', 'course_code', 'semester', 'academic_year', 'enrollment_date']