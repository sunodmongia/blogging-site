from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# creating the login page to register users
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("wireium-home")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form, "title": "Register"})


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
