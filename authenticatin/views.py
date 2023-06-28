from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request,"authenticatin/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
      

        messages.success(request, "Your account was successfully created")
        return redirect("signin")

    return render(request, "authenticatin/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        pass1 = request.POST.get('pass1', '')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("signin")

    return render(request, "authenticatin/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")