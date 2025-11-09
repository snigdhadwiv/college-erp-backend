from django.db import models
from students.models import Student
from courses.models import Subject

class Marks(models.Model):
    EXAM_TYPES = [
        ('MID_SEM', 'Mid Semester'),
        ('END_SEM', 'End Semester'),
        ('ASSIGNMENT', 'Assignment'),
        ('QUIZ', 'Quiz'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)
    exam_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'subject', 'exam_type', 'exam_date']
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.exam_type} - {self.marks_obtained}"
    
    @property
    def percentage(self):
        return (self.marks_obtained / self.max_marks) * 100