from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    credits = models.IntegerField()
    description = models.TextField(blank=True)
    specialization = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField()
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class Enrollment(models.Model):
    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'), 
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
    ]
    
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'})
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    academic_year = models.CharField(max_length=9)
    
    class Meta:
        unique_together = ['student', 'course', 'semester', 'academic_year']
    
    def __str__(self):
        return f"{self.student.email} - {self.course.course_code} (Sem {self.semester})"

# ADD THIS AS SEPARATE CLASS (NOT INSIDE ENROLLMENT)
class FacultyAssignment(models.Model):
    faculty = models.ForeignKey('users.User', on_delete=models.CASCADE, limit_choices_to={'role': 'FACULTY'})
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['faculty', 'course']
    
    def __str__(self):
        return f"{self.faculty.email} - {self.course.course_code}"

# Your other models (Syllabus, Subject, Assignment)...
class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # ... rest of Syllabus fields

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # ... rest of Subject fields

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # ... rest of Assignment fields