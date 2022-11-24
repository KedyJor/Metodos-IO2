from tkinter import *
import tkinter
import math

sexta_va = tkinter.Tk()

# dimesion del cuadro

sexta_va.geometry("400x580")
sexta_va.title("ESIS")
# expansion de la ventana
sexta_va.resizable(0, 0)
# imagen -> sexta_va.iconbitmap("descarga.ico") #

# el color #
sexta_va.config(background="#213141")

l_titulo = tkinter.Label(sexta_va, 
                        text="Modelo con revisión periódica con demanda p.",
                        font= "#56CD63",
                        fg="green",
                        width="45",
                        height="2"
                        )


l_titulo.place( y=10)

#-----------------------------------------------------------------------
l_PeriodoRevision = tkinter.Label(sexta_va, text="Periodo de revisión")
l_PeriodoRevision.place(x=15,y=70, width=170,height=25)

e_PeriodoRevision=tkinter.Entry(sexta_va)
e_PeriodoRevision.place(x=200, y=70, width=130,height=25)
#-----------------------------------------------------------------------
l_DemandaPromedio = tkinter.Label(sexta_va, text="Demanda promedio")
l_DemandaPromedio.place(x=15,y=110, width=170,height=25)

e_DemandaPromedio=tkinter.Entry(sexta_va)
e_DemandaPromedio.place(x=200, y=110, width=130,height=25)
#-----------------------------------------------------------------------
l_PeriodoEspera = tkinter.Label(sexta_va, text="Periodo de espera")
l_PeriodoEspera.place(x=15,y=150, width=170,height=25)

e_PeriodoEspera=tkinter.Entry(sexta_va)
e_PeriodoEspera.place(x=200, y=150, width=130,height=25)
#-----------------------------------------------------------------------
l_ValorDisNormal = tkinter.Label(sexta_va, text="Distribución normal")
l_ValorDisNormal.place(x=15,y=190, width=170,height=25)

e_ValorDisNormal=tkinter.Entry(sexta_va)
e_ValorDisNormal.place(x=200, y=190, width=130,height=25)
#-----------------------------------------------------------------------
l_DesviacionEstandar = tkinter.Label(sexta_va, text="Desviación estandar")
l_DesviacionEstandar.place(x=15,y=230, width=170,height=25)

e_DesviacionEstandar=tkinter.Entry(sexta_va)
e_DesviacionEstandar.place(x=200, y=230, width=130,height=25)
#-----------------------------------------------------------------------
l_InventarioInicial = tkinter.Label(sexta_va, text="Inventario inicial")
l_InventarioInicial.place(x=15,y=270, width=170,height=25)

e_InventarioInicial=tkinter.Entry(sexta_va)
e_InventarioInicial.place(x=200, y=270, width=130,height=25)
#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CantidadOptimaPedido =tkinter.Label(sexta_va, text="Cantidad Op. Pedido")
l_CantidadOptimaPedido.place(x=15, y=350, width=170,height=25)

l_entrada_CantidadOptimaPedido =tkinter.Label(sexta_va, text="")
l_entrada_CantidadOptimaPedido.place(x=200, y=350, width=130,height=25)
#-----------------------------------------------------------------------
l_VarianzaTL =tkinter.Label(sexta_va, text="Varianza de T. Espera y P.")
l_VarianzaTL.place(x=15, y=390, width=170,height=25)

l_entrada_VarianzaTL =tkinter.Label(sexta_va, text="")
l_entrada_VarianzaTL.place(x=200, y=390, width=130,height=25)
#-----------------------------------------------------------------------
l_InventarioSeguridad =tkinter.Label(sexta_va, text="Inventario de seguridad")
l_InventarioSeguridad.place(x=15, y=430, width=170,height=25)

l_entrada_InventarioSeguridad =tkinter.Label(sexta_va, text="")
l_entrada_InventarioSeguridad.place(x=200, y=430, width=130,height=25)

def InventarioSeguridad(OTmL):
    z=e_ValorDisNormal.get()
    SS=float(z)*float(OTmL)
    if (abs(SS) - abs(int(SS)) != 0):
        SS = SS-(abs(SS) - abs(int(SS)))+1
    SS=int(SS)
    l_entrada_InventarioSeguridad.config(text=SS)

def CantidadPedirPeriodo(OTmL):
    d=e_DemandaPromedio.get()
    T=e_PeriodoRevision.get()
    L=e_PeriodoEspera.get()
    z=e_ValorDisNormal.get()
    o=e_DesviacionEstandar.get()
    Io=e_InventarioInicial.get()
    Q=(float(d)*(float(T)+float(L)))+(float(z)*float(OTmL))-(float(Io))
    if (abs(Q) - abs(int(Q)) != 0):
        Q = Q-(abs(Q) - abs(int(Q)))+1
    Q=int(Q)
    l_entrada_CantidadOptimaPedido.config(text=Q)

def VarianzaTmL():
    T=e_PeriodoRevision.get()
    L=e_PeriodoEspera.get()
    o=e_DesviacionEstandar.get()
    OTmL = math.sqrt((float(T)+float(L))*math.pow(float(o),2))
    l_entrada_VarianzaTL.config(text="%.1f" % OTmL)
    CantidadPedirPeriodo(OTmL)
    InventarioSeguridad(OTmL)

button_calcular=tkinter.Button(sexta_va,
    text="Calcular",
    command=VarianzaTmL,
    )
button_calcular.place(x=270,y=498,width=100,height=50)

sexta_va.mainloop()