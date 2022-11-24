from tkinter import *
import tkinter
import math
# ------------------------------------"
raiz = tkinter.Tk()

raiz.geometry("400x570")
raiz.title("ESIS")
raiz.resizable(0, 0)
raiz.config(background="#213141")

l_titulo = tkinter.Label(raiz, 
                        text="MODELO DE CANTIDAD ECONOMICA DE PEDIDO",
                        font= "#56CD63",
                        fg="green",
                        width="45",
                        height="2"
                        )


l_titulo.place( y=10)


# ------------------------------------ #
#  nombre de las etiquetas #
l_demanda = tkinter.Label(raiz, text="Tasa de demanda (D)")
l_pedido = tkinter.Label(raiz, text="Costo de pedido (S)")
l_cost_transporte = tkinter.Label(raiz, text="Costo de transporte (H)")
l_cost_uni = tkinter.Label(raiz, text="Costo unitario")
l_dias_anio = tkinter.Label(raiz, text="Dias por anio")
l_tiempo_espera = tkinter.Label(raiz, text="Tiempo de espera")


#   etiquetas de salida #
# ---------------------------------------------------------- #
l_tam_pedido = tkinter.Label(raiz, text="Tamaño de pedido")
l_num_pedido = tkinter.Label(raiz, text="Numero de pedido")
l_tiempo_ciclo = tkinter.Label(raiz, text="Tiempo de ciclo")
l_tiempo_Reorden = tkinter.Label(raiz, text="Tiempo de reorden")

label_Q = tkinter.Label(raiz, text="")
label_Ped = tkinter.Label(raiz, text="")
label_Ciclo = tkinter.Label(raiz, text="")
label_Reorden = tkinter.Label(raiz, text="")

# ---------------------------------------------------------- #
#  Entrada de datos #
e_demanda = tkinter.Entry(raiz)
e_cost_pedido = tkinter.Entry(raiz)
e_cost_transporte = tkinter.Entry(raiz)
e_cost_unitario = tkinter.Entry(raiz)
e_dias_anio = tkinter.Entry(raiz)
e_tiempo_espera = tkinter.Entry(raiz)


# inciando el tiempo de espera en 0  #

e_tiempo_espera.insert(0, "0")


# colocanado las etiquetas en la pantalla #
l_demanda.place(x=10, y=70, width=150)
l_pedido.place(x=10, y=100, width=150)
l_cost_transporte.place(x=10, y=130, width=150)
l_cost_uni.place(x=10, y=160, width=150)
l_dias_anio.place(x=10, y=190, width=150)
l_tiempo_espera.place(x=10, y=220, width=150)

l_tam_pedido.place(x=10, y=330, width=150)
l_num_pedido.place(x=10, y=360, width=150)
l_tiempo_ciclo.place(x=10, y=390, width=150)
l_tiempo_Reorden.place(x=10, y=420, width=150)

# colocando la entrada de datos en la pantalla#
e_demanda.place(x=170, y=70)
e_cost_pedido.place(x=170, y=100)
e_cost_transporte.place(x=170, y=130)
e_cost_unitario.place(x=170, y=160)
e_dias_anio.place(x=170, y=190)
e_tiempo_espera.place(x=170, y=220)

# colocando la salida de datos en la pantalla#

label_Q.place(x=170, y=330, width=130, height=20)
label_Ped.place(x=170, y=360, width=130, height=20)
label_Ciclo.place(x=170, y=390, width=130, height=20)
label_Reorden.place(x=170, y=420, width=130, height=20)


# ------------------------------------ #
# funciones #
def punto_reorden():
    """punto de reorden"""
    m = e_tiempo_espera.get()
    dias = e_dias_anio.get()
    D = e_demanda.get()
    r = float(D)*float(m)/float(dias)
    label_Reorden.config(text="%.2f" % r)


def tiempo_ciclo(z):
    """tiempo de ciclo"""
    dias = e_dias_anio.get()
    t = float(dias)/float(z)
    label_Ciclo.config(text="%.2f" % t)


def numero_pedido(x):
    """numero de pedidos"""
    D = e_demanda.get()
    N = float(D)/float(x)
    if (abs(N) - abs(int(N)) != 0):
        N = N-(abs(N) - abs(int(N)))+1
    label_Ped.config(text=N)
    tiempo_ciclo(N)


def cantidad_optima_pedido():
    """cantidad optima de pedido"""
    try:
        costo_pedido = e_cost_pedido.get()
        cant_anual = e_demanda.get()
        costo_mantenimiento = e_cost_transporte.get()
        q = math.sqrt(2*float(costo_pedido)*float(cant_anual) /
                      float(costo_mantenimiento))
        if (abs(q) - abs(int(q)) != 0):
            q = q-(abs(q) - abs(int(q)))+1
        label_Q.config(text=q)
        numero_pedido(q)
        punto_reorden()
    except ValueError:
        pass

def cerrar_ventana():
    raiz.destroy()

button_calcular = tkinter.Button(raiz,
    text="Calcular",
    command=cantidad_optima_pedido
    )
button_calcular.place(x=200, y=480, width=100,height=50)

button_salir=tkinter.Button(
    raiz,
    text="Salir",
    command=cerrar_ventana
)
button_salir.place(x=10,y=500, width=70,height=25)


raiz.mainloop()
