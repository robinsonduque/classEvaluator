from django.shortcuts import HttpResponse, render

# Create your views here.
def reports(request):
    return render(request, "reports/reports.html")
