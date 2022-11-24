from tkinter import *
import tkinter
import math

quinta_va = tkinter.Tk()

# dimesion del cuadro

quinta_va.geometry("400x620")
quinta_va.title("ESIS")
# expansion de la ventana
quinta_va.resizable(0, 0)
# imagen -> quinta_va.iconbitmap("descarga.ico") #

# el color #
quinta_va.config(background="#213141")

l_titulo = tkinter.Label(quinta_va, 
                        text="Modelo de Punto de Reorden con Demanda P.",
                        font= "#56CD63",
                        fg="green",
                        width="45",
                        height="2"
                        )


l_titulo.place( y=5)

#-----------------------------------------------------------------------
l_DemandaAnual = tkinter.Label(quinta_va, text="Demanda Anual")
l_DemandaAnual.place(x=15,y=70, width=170,height=25)

e_DemandaAnual=tkinter.Entry(quinta_va)
e_DemandaAnual.place(x=200, y=70, width=130,height=25)
#-----------------------------------------------------------------------
l_CostoProducto = tkinter.Label(quinta_va, text="Costo por producto")
l_CostoProducto.place(x=15,y=110, width=170,height=25)

e_CostoProducto=tkinter.Entry(quinta_va)
e_CostoProducto.place(x=200, y=110, width=130,height=25)
#-----------------------------------------------------------------------
l_CostoPedido = tkinter.Label(quinta_va, text="Costo por pedido")
l_CostoPedido.place(x=15,y=150, width=170,height=25)

e_CostoPedido=tkinter.Entry(quinta_va)
e_CostoPedido.place(x=200, y=150, width=130,height=25)
#-----------------------------------------------------------------------
l_TasaRestension = tkinter.Label(quinta_va, text="Tasa de retension")
l_TasaRestension.place(x=15,y=190, width=170,height=25)

e_TasaRestension=tkinter.Entry(quinta_va)
e_TasaRestension.place(x=200, y=190, width=130,height=25)
#-----------------------------------------------------------------------
l_TiempoEspera = tkinter.Label(quinta_va, text="Tiempo de espera")
l_TiempoEspera.place(x=15,y=230, width=170,height=25)

e_TiempoEspera=tkinter.Entry(quinta_va)
e_TiempoEspera.place(x=200, y=230, width=130,height=25)
#-----------------------------------------------------------------------
l_Media = tkinter.Label(quinta_va, text="Media")
l_Media.place(x=15,y=270, width=170,height=25)

e_Media=tkinter.Entry(quinta_va)
e_Media.place(x=200, y=270, width=130,height=25)
#-----------------------------------------------------------------------
l_Desviacion = tkinter.Label(quinta_va, text="Desviación estandar")
l_Desviacion.place(x=15,y=310, width=170,height=25)

e_Desviacion=tkinter.Entry(quinta_va)
e_Desviacion.place(x=200, y=310, width=130,height=25)
#-----------------------------------------------------------------------
l_DisZ =tkinter.Label(quinta_va, text="Z")
l_DisZ.place(x=15, y=350, width=170,height=25)

e_DisZ=tkinter.Entry(quinta_va)
e_DisZ.place(x=200, y=350, width=130,height=25)
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CantidadOptimaPedido =tkinter.Label(quinta_va, text="Cantidad Op. Pedido")
l_CantidadOptimaPedido.place(x=15, y=410, width=170,height=25)

l_entrada_CantidadOptimaPedido =tkinter.Label(quinta_va, text="")
l_entrada_CantidadOptimaPedido.place(x=200, y=410, width=130,height=25)
#-----------------------------------------------------------------------
l_CantidadPedidosAnual =tkinter.Label(quinta_va, text="Cantidad de pedidos anual")
l_CantidadPedidosAnual.place(x=15, y=450, width=170,height=25)

l_entrada_CantidadPedidosAnual =tkinter.Label(quinta_va, text="")
l_entrada_CantidadPedidosAnual.place(x=200, y=450, width=130,height=25)
#-----------------------------------------------------------------------
l_TiempoCiclo =tkinter.Label(quinta_va, text="Tiempo de ciclo")
l_TiempoCiclo.place(x=15, y=490, width=170,height=25)

l_entrada_TiempoCiclo =tkinter.Label(quinta_va, text="")
l_entrada_TiempoCiclo.place(x=200, y=490, width=130,height=25)
#-----------------------------------------------------------------------
l_PuntoReorden =tkinter.Label(quinta_va, text="Punto de reorden")
l_PuntoReorden.place(x=15, y=530, width=170,height=25)

l_entrada_PuntoReorden =tkinter.Label(quinta_va, text="")
l_entrada_PuntoReorden.place(x=200, y=530, width=130,height=25)


def PuntoReorden(u,o):
    z=e_DisZ.get()
    r= float(u)+(float(z)*float(o))
    r=int(r)
    l_entrada_PuntoReorden.config(text=r)

def TiempoCiclo(N):
    T=250/(float(N))
    l_entrada_TiempoCiclo.config(text="%.1f" % T)

def PedidoAnual(Q,D):
    N=float(D)/float(Q)
    N=int(N)
    l_entrada_CantidadPedidosAnual.config(text=N)
    TiempoCiclo(N)

def CantEconomicaPedido():
    D=e_DemandaAnual.get()
    C=e_CostoProducto.get()
    Co=e_CostoPedido.get()
    I=e_TasaRestension.get()
    m=e_TiempoEspera.get()
    u=e_Media.get()
    o=e_Desviacion.get()
    Q=math.sqrt((2*float(D)*float(Co))/(float(I)*float(C)))
    Q=int(Q)
    l_entrada_CantidadOptimaPedido.config(text=Q)
    PedidoAnual(Q,D)
    PuntoReorden(u,o)

button_calcular=tkinter.Button(quinta_va,
    text="Calcular",
    command=CantEconomicaPedido,
    )
button_calcular.place(x=270,y=570,width=100,height=30)

quinta_va.mainloop()