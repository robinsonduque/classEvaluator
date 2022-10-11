from django.shortcuts import render, HttpResponse
from .models import Subject

# Create your views here.


def activities(request):
    subjects = Subject.objects.all()
    return render(request, "activities/activities.html", {"subjects": subjects})
