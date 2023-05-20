from django.shortcuts import render
from .forms import Roomforms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import discussion_room


# Create your views here.

# def room(request) :
#     get_form = Roomforms
#     return render(request, "chat/room.html", {
#         "form" : get_form
#     })

def index(request) :
    return render(request, "chat/index.html")

def login_view(request) :
    if not request.user.is_authenticated:
        if request.method == "POST" :
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return HttpResponseRedirect(reverse(index))
            else :
                return render(request, "rec/index.html", {
                    "message" : "Invalid username and/or password."
                })
            
        else :
            return render(request, "rec/index.html")
    else :
        return HttpResponseRedirect(reverse(index))
    
def register(request) :
    if not request.user.is_authenticated:
        if request.method == "POST" :
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            if password != confirm_password :
                return render(request, "chat/register.html", {
                    "message" : "Password does not match"
                })
            
            try : 
                user = User.objects.create_user(username, email, password)
                user.save()

            except IntegrityError:
                return render(request, "chat/register.html", {
                    "message" : "A user with that username already exist"
                })
            
            login(request, user)
            return HttpResponseRedirect(reverse(index))

        else:
            return render(request, "chat/register.html")
    else:
        return HttpResponseRedirect(reverse(index))

def logout_view(request) :
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse(index))
    
def dis_room(request) :
    get_rooms = discussion_room.objects.get(id = 2)
    return render(request, "chat/discussion_room.html", {
        "room" : get_rooms
    })

def home(request) :
    get_rooms = discussion_room.objects.all()
    return render(request, "chat/home.html", {
        "rooms" : get_rooms
    })
    
def add_room(request) :
    if request.user.is_authenticated :
        if request.method == "POST" :
            form = Roomforms(request.POST , request.FILES)
            if form.is_valid :
                form.save()
                return HttpResponseRedirect(reverse(home))
        else :
            get_form = Roomforms
            return render(request, "chat/room.html", {
                "form" : get_form
            })


