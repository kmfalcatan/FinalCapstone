# models.py

from django.db import models
from django.utils import timezone

class Admin(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
    Name = models.CharField(max_length=255, default='null')
    Rank = models.CharField(max_length=255, default='null')
    Designation = models.CharField(max_length=255, default='null')
    Course = models.CharField(max_length=255, default='null', unique=True)
    Role = models.CharField(max_length=255, default='null')
    Address = models.CharField(max_length=255, default='null')
    College = models.CharField(max_length=255, default='null')
    Number = models.CharField(max_length=255, default='null')

    def __str__(self):
        return self.Email

class Course(models.Model):
    College = models.CharField(max_length=255)
    Course = models.CharField(max_length=255)
    AvgGrade = models.FloatField()  
    AvgCet = models.FloatField()  
    TotalScore = models.FloatField()  
    CourseDescription = models.CharField(max_length=255)
    Logo = models.CharField(max_length=255, default='img/png-clipart-computer-icons-error-information-error-angle-triangle-thumbnail-removebg-preview copy.png')
    reason = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.Course} at {self.College}"
    
class List(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    AvgGrade = models.FloatField()
    AvgCet = models.FloatField()
    Number = models.CharField(max_length=20)
    ApplicationNo = models.CharField(max_length=255, default=0)
    Address = models.TextField()
    Course = models.CharField(max_length=255)
    Status = models.CharField(max_length=20, default='Pending')
    Year = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
    
class Feedback(models.Model):
    Name = models.CharField(max_length=255)
    Feedback = models.CharField(max_length=255)

class Grades(models.Model):
    StudentID = models.FloatField(default=0)
    AvgGrade = models.FloatField(default=0)
    AvgCet = models.FloatField(default=0)
    TotalScore = models.FloatField(default=0)
    PersonalityScore = models.FloatField(default=0)
    courseName = models.CharField(max_length=255, default='General')

class Student(models.Model):
    StudentID = models.FloatField()
    Year = models.IntegerField(default=0)
    
class Question(models.Model):
    text = models.TextField()
    courseName = models.CharField(max_length=255, default='General')
    Percentage = models.FloatField(default=0)

class StudentResponse(models.Model):
    AvgGrade = models.FloatField(default=0)
    AvgCet = models.FloatField(default=0)
    StudentID = models.FloatField()
    question = models.CharField(max_length=255)
    response = models.FloatField()
    courseName = models.CharField(max_length=255, null=True, blank=True)

class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=255)  
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=2)
    
class TotalPercentage(models.Model):
    CetAvgPercentage = models.FloatField(default=0)
    GradeAvgPercentage = models.FloatField(default=0)
    PersonalityPercentage = models.FloatField(default=0)