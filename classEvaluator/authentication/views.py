from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def log_in(request):
    if request.user.is_authenticated:
        return redirect("index")
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
                messages.error(request, "User not valid")
        else:
            messages.error(request, "Incorrect information")

        return render(request, "login/iniciar_sesion.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("log_in")


@login_required(login_url="login/")
def update_user(request):
    if request.method == "GET":
        form = PasswordChangeForm(None)
        return render(request, "updateUser/update_password.html", {"form": form})
    elif request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid() and form.clean_old_password() and form.clean_new_password2():
            form.save()
            # update_session_auth_hash(request, form.user)
            return redirect("/")
        else:
            messages.error(request, "Incorrect information")

    return render(request, "updateUser/update_password.html", {"form": form})
