# courses/migrations/0003_faculty_assignment.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0002_enrollment'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('faculty', models.ForeignKey(limit_choices_to={'role': 'FACULTY'}, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'unique_together': {('faculty', 'course')},
            },
        ),
    ]