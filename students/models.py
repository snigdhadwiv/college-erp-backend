
from django.db import models

class Student(models.Model):
    student_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Student ID"
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Last Name"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone Number"
    )
    date_of_birth = models.DateField(
        verbose_name="Date of Birth"
    )
    address = models.TextField(
        verbose_name="Residential Address"
    )
    enrollment_date = models.DateField(
        auto_now_add=True,
        verbose_name="Enrollment Date"
    )

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
