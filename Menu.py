import tkinter as tk
import tkinter
from tkinter import *

v_menu = tkinter.Tk()

v_menu.geometry("460x450")
v_menu.title("ESIS - VI")
v_menu.resizable(0, 0)
v_menu.config(background="light steel blue")
main_title = Label(v_menu,
                   text="METODOS",
                   font=("Yu Mincho", 17), 
                   bg="royal blue",
                   fg="white",
                   width="550",
                   height="2"
                   )
main_title.pack()


def cerrar():
    v_menu.destroy()


def ventanaVariantes():
    v_menu.withdraw()          
    import VariantesEOQ      
    win=VariantesEOQ   

def ventanaPERT():
    v_menu.withdraw()          
    import PERTinterface      
    win=PERTinterface        

def ventanaCPM():
    v_menu.withdraw()
    import CPMinterface      
    win=CPMinterface

button_cpm =tkinter.Button(v_menu,
    text= "CPM",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaCPM
)
button_cpm.pack(pady=20,ipadx=70,ipady=15)


button_pert =tkinter.Button(v_menu,
    text= "PERT",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaPERT
)
button_pert.pack(ipadx=70,ipady=15)

button_eopq =tkinter.Button(v_menu,
    text= "EOQ",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaVariantes
)
button_eopq.pack(pady=20,ipadx=74,ipady=15) 

button_salir=tkinter.Button(v_menu,
    text= "Salir",
    font=("Arial", 11), 
    bg='light grey',
    command=cerrar
)
button_salir.pack(pady=20,ipadx=34,ipady=3)

v_menu.mainloop()