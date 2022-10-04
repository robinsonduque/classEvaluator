from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control


# Create your views here.




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.user.is_authenticated:
        return render(request, "base/index.html")
    return  redirect("log_in")