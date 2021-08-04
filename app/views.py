from django.shortcuts import redirect, render
import random
from datetime import date, datetime
# Create your views here.

def start(request):
    
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["gold"] = 0
        request.session["logs"] = []
        print("Se ha creado la sesion:" + request.session["name"])
        return redirect("/")

def logout(request):
    if request.method == "POST":
        del request.session["name"]
        del request.session["gold"]
        del request.session["logs"]
        return redirect("/")


def matraca(request):
    if request.method == "POST":

        if request.POST["tipo"] == "farm":
            oro_farm = random.randrange(10, 21 , 1)
            request.session["gold"] += oro_farm
            logs = request.session["logs"]
            logs.append({
            "tipo" : "farm",
            "descripcion" : f"Has ganado {str(oro_farm)} de oro en Farm!",
            "css" : "text-success",
            "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            })
            request.session["logs"] = logs


        elif request.POST["tipo"] == "cave":
            oro_cave = random.randrange(5, 11 , 1)
            request.session["gold"] += oro_cave
            logs = request.session["logs"]
            logs.append({
            "tipo" : "cave",
            "descripcion" : f"Has ganado {oro_cave} de oro en Farm!",
            "css" : "text-success",
            "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            })
            request.session["logs"] = logs


        elif request.POST["tipo"] =="house":
            oro_house = random.randrange(2, 6 , 1)
            request.session["gold"] += oro_house
            logs = request.session["logs"]
            logs.append({
            "tipo" : "house",
            "descripcion" : f"Has ganado {oro_house} de oro en Farm!",
            "css" : "text-success",
            "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            })
            request.session["logs"] = logs


        elif request.POST["tipo"] =="casino":
            oro_casino = random.randrange(-50, 51 , 1)
            request.session["gold"] += oro_casino
            logs = request.session["logs"]
            if oro_casino < 0:
                descripcion = f"Has perdido {oro_casino *-1} de oro en Casino! "
                css = "text-danger"
            else:
                descripcion = f"Has ganado {oro_casino} de oro en Casino!"
                css= "text-success"
            logs.append({
            "tipo" : "casino",
            "descripcion" : descripcion,   
            "css" : css,
            "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            })
            request.session["logs"] = logs
    

    return redirect("/")