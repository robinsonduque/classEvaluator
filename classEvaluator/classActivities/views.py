from django.shortcuts import render, HttpResponse

# Create your views here.


def activities(request):
    return render(request, "activities/activities.html")
