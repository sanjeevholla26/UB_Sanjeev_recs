from django.urls import path

from . import views

urlpatterns = [
    # path("", views.room, name="index"),
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name = "register"),
    path("logout/", views.logout_view, name="logout"),
    path("dis_room/", views.dis_room, name = "dis_room"),
    path("home/", views.home, name = "home"),
    path("addroom/", views.add_room, name="addroom"),
]