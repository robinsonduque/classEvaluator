from django.shortcuts import HttpResponse, render

# Create your views here.


def repositories(request):
    return render(request, "repositories/repositories.html")
