
from tkinter import *
import random
 

root = Tk()
 

root.geometry("300x300")
 

root.title("Piedra Papel o Tijera")
 

computer_value = {
    "0":"Piedra",
    "1":"Papel",
    "2":"Tijera"
}
 

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "jugador              ")
    l3.config(text = "Computadora")
    l4.config(text = "")
 

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 

def esPiedra():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Piedra":
        match_result = "Empate"
    elif c_v=="Tijera":
        match_result = "Jugador Gana"
    else:
        match_result = "Computadora gana"
    l4.config(text = match_result)
    l1.config(text = "Piedra            ")
    l3.config(text = c_v)
    button_disable()
 

def esPapel():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Papel":
        match_result = "Empate"
    elif c_v=="Tijera":
        match_result = "Computadora "
    else:
        match_result = "Jugadora gana"
    l4.config(text = match_result)
    l1.config(text = "Papel           ")
    l3.config(text = c_v)
    button_disable()
 

def esTijera():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Piedra":
        match_result = "Computadora Gana"
    elif c_v == "Tijera":
        match_result = "Empate"
    else:
        match_result = "Jugadora"
    l4.config(text = match_result)
    l1.config(text = "Tijera         ")
    l3.config(text = c_v)
    button_disable()
 

Label(root,
      text = "Piedra Papel Tijera",
      font = "normal 20 bold",
      fg = "blue").pack(pady = 20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "Jugador              ",
           font = 10)
 
l2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
 
l3 = Label(frame, text = "Computadora", font = 10)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text = "Piedra",
            font = 10, width = 7,
            command = isrock)
 
b2 = Button(frame1, text = "Papel ",
            font = 10, width = 7,
            command = ispaper)
 
b3 = Button(frame1, text = "Tijera",
            font = 10, width = 7,
            command = isscissor)
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
 
Button(root, text = "reiniciar_jueguo",
       font = 10, fg = "red",
       bg = "black", command = reiniciar_juego).pack(pady = 20)
 

root.mainloop()