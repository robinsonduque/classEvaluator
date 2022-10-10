from django.shortcuts import render, HttpResponse

# Create your views here.
def groups(request):
    return render(request, "groups/groups.html")
