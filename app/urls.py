from django.urls import path
from . import views

urlpatterns = [

    path("",views.start),
    path("login",views.login),
    path("logout",views.logout),
    path("process_money",views.matraca)
]

