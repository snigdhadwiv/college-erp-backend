from django.contrib import admin
from .models import Course, Subject, Syllabus
from .models import Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'specialization', 'year', 'semester', 'credits']
    list_filter = ['specialization', 'year', 'semester']
    search_fields = ['course_code', 'course_name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_code', 'subject_name', 'course', 'credits']
    list_filter = ['course']
    search_fields = ['subject_code', 'subject_name']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['course', 'created_at']
    list_filter = ['course']



@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'academic_year', 'enrollment_date')
    list_filter = ('semester', 'academic_year', 'course')
    search_fields = ('student__email', 'course__course_code')
