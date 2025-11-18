from django.contrib import admin
from .models import Course, Subject, Syllabus, Enrollment, FacultyAssignment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_name', 'specialization', 'year', 'semester', 'credits']

# TEMPORARILY COMMENT OUT EVERYTHING ELSE
# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['id', 'course', 'subject_code', 'subject_name', 'credits']

# @admin.register(Syllabus)
# class SyllabusAdmin(admin.ModelAdmin):
#     list_display = ['id', 'course', 'created_at']

# @admin.register(Enrollment)
# class EnrollmentAdmin(admin.ModelAdmin):
#     list_display = ('student', 'course', 'semester', 'academic_year', 'enrollment_date')

@admin.register(FacultyAssignment)
class FacultyAssignmentAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'course', 'assigned_date')