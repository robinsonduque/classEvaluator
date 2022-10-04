
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.


def log_in(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "login/iniciar_sesion.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("index")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

        return render(request, "login/iniciar_sesion.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("log_in")