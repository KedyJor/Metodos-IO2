from tkinter import *
import tkinter
import math

tercera_va = tkinter.Tk()

# dimesion del cuadro

tercera_va.geometry("420x570")
tercera_va.title("ESIS")
# expansion de la ventana
tercera_va.resizable(0, 0)
# imagen -> tercera_va.iconbitmap("descarga.ico") #

# el color #
tercera_va.config(background="#213141")

l_titulo = tkinter.Label(tercera_va, 
                        text="Descuentos por cantidad en el modelo EOQ",
                        font= "#56CD63",
                        fg="green",
                        width="50",
                        height="2"
                        )


l_titulo.place( y=10)
#-----------------------------------------------------------------------
l_Demanda = tkinter.Label(tercera_va, text="Demanda anual")
l_Demanda.place(x=15,y=70, width=175,height=25)

e_Demanda=tkinter.Entry(tercera_va)
e_Demanda.place(x=200, y=70, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoInventario = tkinter.Label(tercera_va, text="Costo de mantener el inventario")
l_CostoInventario.place(x=15,y=120, width=175,height=25)

e_CostoInventario=tkinter.Entry(tercera_va)
e_CostoInventario.place(x=200, y=120, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoPedido = tkinter.Label(tercera_va, text="Costo de pedido")
l_CostoPedido.place(x=15,y=170, width=175,height=25)

e_CostoPedido=tkinter.Entry(tercera_va)
e_CostoPedido.place(x=200, y=170, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoAdquisicion = tkinter.Label(tercera_va, text="Costo de Adquisición")
l_CostoAdquisicion.place(x=15,y=220, width=175,height=25)

e_CostoAdquisicion=tkinter.Entry(tercera_va)
e_CostoAdquisicion.place(x=200, y=220, width=175,height=25)

#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CantidadOptima =tkinter.Label(tercera_va, text="Tamaño óptimo de pedido")
l_CantidadOptima.place(x=15, y=340, width=175,height=25)

l_entrada_CantidadOptima =tkinter.Label(tercera_va, text="")
l_entrada_CantidadOptima.place(x=220, y=340, width=130,height=25)
#-----------------------------------------------------------------------
l_CostoTotal =tkinter.Label(tercera_va, text="Costo total")
l_CostoTotal.place(x=15, y=390, width=175,height=25)

l_entrada_CostoTotal =tkinter.Label(tercera_va, text="")
l_entrada_CostoTotal.place(x=220, y=390, width=130,height=25)
#-----------------------------------------------------------------------

def CostoTotal(D,S,I,Ca,Q):
    Cq=(float(D)*float(Ca))+((float(S)*float(D))/float(Q))+((float(Q)*float(I)*float(Ca))/2)
    l_entrada_CostoTotal.config(text=Cq)


def CantidadOptima():
    D=e_Demanda.get()
    S=e_CostoPedido.get()
    I=e_CostoInventario.get()
    Ca=e_CostoAdquisicion.get()
    Q = math.sqrt((2*float(D)*float(S))/(float(I)*float(Ca)))
    l_entrada_CantidadOptima.config(text=Q)
    CostoTotal(D,S,I,Ca,Q)

button_calcular=tkinter.Button(tercera_va,
    text="Calcular",
    command=CantidadOptima,
    )
button_calcular.place(x=270,y=480,width=100,height=50)

tercera_va.mainloop()
