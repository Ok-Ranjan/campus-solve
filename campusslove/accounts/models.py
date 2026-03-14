from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    collage = models.CharField(max_length=200)
    program = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    semester = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name