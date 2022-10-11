from django.contrib import admin
from .models import Category, Exercise, Subject, Test, Activity, ActivityExercise

# Register your models here.
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(Test)
admin.site.register(Activity)
admin.site.register(ActivityExercise)
admin.site.register(Subject)
