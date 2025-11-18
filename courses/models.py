from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    credits = models.IntegerField()
    description = models.TextField(blank=True)
    specialization = models.CharField(max_length=100)  # CS, IT, etc.
    year = models.IntegerField()  # 1, 2, 3, 4
    semester = models.IntegerField()  # 1, 2
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tlp_file = models.FileField(upload_to='syllabus/', blank=True, null=True)
    objectives = models.TextField()
    outcomes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Syllabus - {self.course.course_code}"

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=200)
    credits = models.IntegerField()
    
    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    max_marks = models.IntegerField()
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.subject.subject_code}"

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
    academic_year = models.CharField(max_length=9)  # 2024-2025
    
    class Meta:
        unique_together = ['student', 'course', 'semester', 'academic_year']
    
    def __str__(self):
        return f"{self.student.email} - {self.course.course_code} (Sem {self.semester})"