from django.shortcuts import redirect, render
import random
from datetime import  datetime
# Create your views here.

def start(request):
    
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["gold"] = 0
        request.session["logs"] = []
        request.session["win"] = False
        request.session["lose"] = False
        request.session["modo"] = "Facil"
        request.session["movimientos"] = 10
        request.session["obj_oro"] = 150
        print("Se ha creado la sesion:" + request.session["name"])
        return redirect("/")

def logout(request):
    if request.method == "POST":
        del request.session["name"]
        del request.session["gold"]
        del request.session["logs"]
        del request.session["modo"] 
        del request.session["movimientos"]
        del request.session["obj_oro"]
        return redirect("/")


# COnfiguraciones del juego, modo con reglas

def config(request):
    if request.method == "POST":
        request.session["modo"] = request.POST["modo"]
        print(request.session["modo"])
        if request.session["modo"] == "Facil":
            request.session["gold"] = 0
            return redirect("/")
        else:    
            movs = request.POST["movimientos"]
            objoro = request.POST["obj_oro"]
            request.session["movimientos"] = int(movs)
            request.session["obj_oro"] = int(objoro)
            request.session["win"] = False
            request.session["lose"] = False
            request.session["gold"] = 0
            return redirect("/")


def reset(request):
    if request.method == "POST":
        request.session["gold"] = 0
        request.session["modo"] = "Facil"
        request.session["movimientos"] = ""
        request.session["obj_oro"] = ""
        request.session["win"] = False
        request.session["lose"] = False
        return redirect("/")



# Aca empieza el process_money y funciones del juego

def matraca(request):
    if request.method == "POST":
        time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        # <!---FARMEO ORO---!>
        if request.POST["tipo"] == "farm":
            oro_farm = random.randrange(10, 21 , 1)
            request.session["gold"] += oro_farm
            request.session["logs"].append({
            "tipo" : "farm",
            "descripcion" : f"Has ganado {str(oro_farm)} de oro en Farm!",
            "css" : "text-success",
            "time": time
            })
            request.session.save()


        elif request.POST["tipo"] == "cave":
            oro_cave = random.randrange(5, 11 , 1)
            request.session["gold"] += oro_cave
            request.session["logs"].append({
            "tipo" : "cave",
            "descripcion" : f"Has ganado {oro_cave} de oro en Farm!",
            "css" : "text-success",
            "time": time
            })
            request.session.save()


        elif request.POST["tipo"] =="house":
            oro_house = random.randrange(2, 6 , 1)
            request.session["gold"] += oro_house
            request.session["logs"].append({
            "tipo" : "house",
            "descripcion" : f"Has ganado {oro_house} de oro en Farm!",
            "css" : "text-success",
            "time": time
            })
            request.session.save()


        elif request.POST["tipo"] =="casino":
            oro_casino = random.randrange(-50, 51 , 1)
            request.session["gold"] += oro_casino
            
            if oro_casino < 0:
                descripcion = f"Has perdido {oro_casino *-1} de oro en Casino! "
                css = "text-danger"
            else:
                descripcion = f"Has ganado {oro_casino} de oro en Casino!"
                css= "text-success"

            request.session["logs"].append({
            "tipo" : "casino",
            "descripcion" : descripcion,   
            "css" : css,
            "time": time
            })
            request.session.save()


        # <!---COMO GANAR---!>

        if request.session["modo"] == "Dificil":
            victoria = {
                "tipo" : "Estado del Juego",
                "descripcion" : "Has Ganado el Juego",
                "css" : "text-success",
                "time" : time
            }
            derrota = {
                "tipo" : "Estado del Juego",
                "descripcion" : "Has Perdido el Juego",
                "css" : "text-danger",
                "time" : time
                    }

            request.session["movimientos"] -= 1
            if request.session["movimientos"] > 0:

                if request.session["gold"] >= request.session["obj_oro"]:
                    request.session["win"] = True
                    request.session["logs"].append(victoria)
                    request.session.save()

            elif request.session["movimientos"] == 0:
                if request.session["gold"] >= request.session["obj_oro"]:
                    request.session["win"] = True
                    request.session["logs"].append(victoria)
                    request.session.save()
                elif request.session["gold"] < request.session["obj_oro"]:
                    request.session["lose"] = True
                    request.session["logs"].append(derrota)
                    request.session.save()
            else:
                request.session["lose"] = True
                request.session["logs"].append(derrota)
                request.session.save()
                
                



    return redirect("/")