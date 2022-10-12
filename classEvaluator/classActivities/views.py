import datetime
from django.shortcuts import render, HttpResponse
from .models import Subject, Activity
from .forms import ActivityForm
from django.contrib import messages

# Create your views here.


def activities(request):
    subjects = Subject.objects.filter().order_by("id")
    return render(request, "activities/activities.html", {"subjects": subjects})


def createActivity(request, subject_id, subject_name):
    if request.method == "GET":
        form = ActivityForm()
        form.fields["subject"].initial = subject_id  # Hidden field for the class subjec
        return render(
            request,
            "activities/createActivity.html",
            {"form": form, "subject_id": subject_id, "subject_name": subject_name},
        )
    else:
        form = ActivityForm(request.POST)
        if form.is_valid():
            if request.POST.get("available_from") <= request.POST.get(
                "available_until"
            ):
                activity = Activity(
                    name=request.POST.get("name"),
                    available_from=request.POST.get("available_from"),
                    available_until=request.POST.get("available_until"),
                    grade_scale=request.POST.get("grade_scale"),
                    subject=Subject.objects.get(id=request.POST.get("subject")),
                )
                activity.save()
                return activities(request)
            else:
                messages.error(
                    request,
                    "The 'available from' date and time has to be before the 'available until' date and time",
                )

        return render(
            request,
            "activities/createActivity.html",
            {"form": form, "subject_id": subject_id, "subject_name": subject_name},
        )


def editActivitiesExercises(request, subject_id, subject_name, activity_id):

    if request.method == "GET":
        activity = Activity.objects.get(id=activity_id)
        form = ActivityForm(
            data={
                "name": activity.name,
                "available_from": activity.available_from,
                "available_until": activity.available_until,
                "grade_scale": activity.grade_scale,
                "subject": activity_id,
            }
        )

        return render(
            request,
            "activities/editActivityExercises.html",
            {"form": form, "subject_id": subject_id, "subject_name": subject_name},
        )
    else:
        form = ActivityForm(request.POST)
        if form.is_valid():
            if request.POST.get("available_from") <= request.POST.get(
                "available_until"
            ):
                activity = Activity.objects.get(id=activity_id)
                activity.name = request.POST.get("name")
                activity.available_from = request.POST.get("available_from")
                activity.available_until = request.POST.get("available_until")
                activity.grade_scale = request.POST.get("grade_scale")
                # activity.subject = Subject.objects.get(id=request.POST.get("subject"))

                activity.save()
                return activities(request)
