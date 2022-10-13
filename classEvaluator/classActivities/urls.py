"""classEvaluator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (
    activities,
    createActivity,
    editActivity,
    createSubject,
    deleteSubject,
    editSubject,
    deleteActivity,
)

urlpatterns = [
    path("activities", activities, name="activities"),
    path(
        "createActivity/<int:subject_id>/<str:subject_name>/",
        createActivity,
        name="createActivity",
    ),
    path(
        "editActivity/<int:subject_id>/<str:subject_name>/<int:activity_id>/",
        editActivity,
        name="editActivity",
    ),
    path("deleteActivity/<int:activity_id>", deleteActivity, name="deleteActivity"),
    path("createSubject/", createSubject, name="createSubject"),
    path("deleteSubject/<int:subject_id>", deleteSubject, name="deleteSubject"),
    path(
        "editSubject/<int:subject_id>/<str:subject_name>/",
        editSubject,
        name="editSubject",
    ),
]
