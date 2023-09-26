import tkinter as tk
import random

def jugar(opcion_usuario):
    opciones = ["piedra","papel","tijera"]
    opcion_computadora = random.choice(opciones)
    resultado = ""
    if opcion_usuario == opcion_computadora:
        resultado = "empate"
    elif(opcion_usuario == "piedra" and opcion_computadora == "tijera")or\
        (opcion_usuario == "papel" and
          opcion_computadora == "piedra") or\
          (opcion_usuario == "tijera" and
            opcion_computadora == "papel"):
        resultado = "ganaste"
        else:
            resultado = "perdiste"
            