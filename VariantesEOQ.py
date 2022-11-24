import tkinter as tk
from tkinter import *
import tkinter
# ------------------------------------"
# dimesion del cuadro
vari_eoq = tkinter.Tk()
vari_eoq.geometry("550x600")
vari_eoq.title("ESIS")
vari_eoq.resizable(0, 0)
vari_eoq.config(background="#213141")

l_titulo = tkinter.Label(vari_eoq, 
                        text="MODELO DE EOQ(CANTIDAD ECONOMICA DE PEDIDO)",
                        font= "#56CD63",
                        fg="green",
                        width="60",
                        height="2"
                        )
l_titulo.place( y=10)

def cerrar_ventana():
    vari_eoq.destroy()

def ventanaEOQ():
    vari_eoq.withdraw() 
    import EOQ
    win=EOQ   

def ventanaPrime_va():
    vari_eoq.withdraw()
    import prime_va
    win=prime_va

def ventanaSegun_va():
    vari_eoq.withdraw()
    import segun_va
    win=segun_va

def ventanaTerce_va():
    vari_eoq.withdraw()
    import terce_variante
    win=terce_variante

def ventanaCuarta_va():
    vari_eoq.withdraw()
    import cuarta_vari
    win=cuarta_vari

def ventanaQuinta_va():
    vari_eoq.withdraw()
    import quinta_va
    win=quinta_va

def ventanaSexta_va():
    vari_eoq.withdraw()
    import sexta_va
    win=sexta_va

def atras():
    vari_eoq.destroy()
    import Menu
    win=Menu
#-----------------------------------------------------------
button_EOQ =tkinter.Button(vari_eoq,
    text= "Modelo de cantidad economica de pedido",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaEOQ
)
button_EOQ.place(x=25, y=80, width=500, height= 40)

#-------PRIMERA VARIANTE------------------------------------
button_priVariente =tkinter.Button(vari_eoq,
    text= "Modelo de tamaño del lote de producción económica",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaPrime_va
)
button_priVariente.place(x=25, y=140, width=500, height= 40)

#-------SEGUNDA VARIANTE------------------------------------
button_segVariante =tkinter.Button(vari_eoq,
    text= "Modelo de inventario con faltantes planeados",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaSegun_va
)
button_segVariante.place(x=25, y=200, width=500, height= 40) #centramos y separamos con el pady

#-------TERCERA VARIANTE------------------------------------
button_terVariante =tkinter.Button(vari_eoq,
    text= "Descuentos por cantidad en el modelo EOQ",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaTerce_va
)
button_terVariante.place(x=25, y=260, width=500, height= 40)

#-------CUARTA VARIANTE------------------------------------
button_cuarVariante =tkinter.Button(vari_eoq,
    text= "Inventario de periodo unico con demanda probabilística",

    font=("Arial", 13), 
    bg='light grey',
    command=ventanaCuarta_va
)
button_cuarVariante.place(x=25, y=320, width=500, height= 40)

#-------QUINTA VARIANTE------------------------------------
button_quinVariante =tkinter.Button(vari_eoq,
    text= "Modelo de Punto de Reorden con Demanda Probabilística",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaQuinta_va
)
button_quinVariante.place(x=25, y=380, width=500, height= 40)

#-------SEXTA VARIANTE------------------------------------
button_sexVariante =tkinter.Button(vari_eoq,
    text= "Modelo con revisión periódica con demanda probabilística",
    font=("Arial", 13), 
    bg='light grey',
    command=ventanaSexta_va
)
button_sexVariante.place(x=25, y=440, width=500, height= 40)


button_salir=tkinter.Button(vari_eoq,
    text= "Salir",
    font=("Arial", 11), 
    bg='light grey',
    command=cerrar_ventana
)
button_salir.place(x=200, y=500, width=150, height= 30)

button_atras=tkinter.Button(vari_eoq,
    text="Atras",
    font=("Arial", 11), 
    bg='light grey',
    command=atras
)
button_atras.place(x=25, y=550, width=70, height= 25)

vari_eoq.mainloop()