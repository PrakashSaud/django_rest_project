from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class User(User):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)


class Student(models.Model):
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    roll_no = models.IntegerField(blank=False)
    student_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Students')

    class Meta:
        ordering = ['roll_no']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='teachers')
    teacher_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Teachers')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name