from time import timezone
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    question_text = models.TextField(null=True, blank=True)
    question_image = models.ImageField(upload_to="exercises/", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    description = models.CharField(max_length=100)
    input = models.TextField(null=False, blank=False)
    output = models.TextField(null=False, blank=False)
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.description


class Subject(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    available_from = models.DateTimeField(null=False)
    available_until = models.DateTimeField(null=False)
    grade_scale = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, through="ActivityExercise")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=False, blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ActivityExercise(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    exercie = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    grade = models.IntegerField()
