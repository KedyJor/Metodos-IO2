from tkinter import *
import tkinter
import math

segunda_va = tkinter.Tk()

# dimesion del cuadro

segunda_va.geometry("450x600")
segunda_va.title("ESIS")
# expansion de la ventana
segunda_va.resizable(0, 0)
# imagen -> segunda_va.iconbitmap("descarga.ico") #

# el color #
segunda_va.config(background="#213141")

l_titulo = tkinter.Label(segunda_va, 
                        text="Modelo de inventario con faltantes planeados",
                        font= "#56CD63",
                        fg="green",
                        width="50",
                        height="2"
                        )


l_titulo.place( y=10)

#-----------------------------------------------------------------------
l_Demanda = tkinter.Label(segunda_va, text="Demanda anual")
l_Demanda.place(x=15,y=70, width=175,height=25)

e_Demanda=tkinter.Entry(segunda_va)
e_Demanda.place(x=200, y=70, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoInventario = tkinter.Label(segunda_va, text="Costo de mantener el inventario")
l_CostoInventario.place(x=15,y=120, width=175,height=25)

e_CostoInventario=tkinter.Entry(segunda_va)
e_CostoInventario.place(x=200, y=120, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoPedido = tkinter.Label(segunda_va, text="Costo de pedido")
l_CostoPedido.place(x=15,y=170, width=175,height=25)

e_CostoPedido=tkinter.Entry(segunda_va)
e_CostoPedido.place(x=200, y=170, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoFaltante = tkinter.Label(segunda_va, text="Costo de faltante")
l_CostoFaltante.place(x=15,y=220, width=175,height=25)

e_CostoFaltante=tkinter.Entry(segunda_va)
e_CostoFaltante.place(x=200, y=220, width=175,height=25)
#-----------------------------------------------------------------------
l_CostoUnitario = tkinter.Label(segunda_va, text="Costo unitario")
l_CostoUnitario.place(x=15,y=270, width=175,height=25)

e_CostoUnitario=tkinter.Entry(segunda_va)
e_CostoUnitario.place(x=200, y=270, width=175,height=25)
#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CantidadOptima =tkinter.Label(segunda_va, text="Cantidad óptima para comprar")
l_CantidadOptima.place(x=15, y=340, width=175,height=25)

l_entrada_CantidadOptima =tkinter.Label(segunda_va, text="")
l_entrada_CantidadOptima.place(x=220, y=340, width=130,height=25)
#-----------------------------------------------------------------------
l_UnidadesAgotadas =tkinter.Label(segunda_va, text="Número de unidades agotadas")
l_UnidadesAgotadas.place(x=15, y=390, width=175,height=25)

l_entrada_UnidadesAgotadas =tkinter.Label(segunda_va, text="")
l_entrada_UnidadesAgotadas.place(x=220, y=390, width=130,height=25)
#-----------------------------------------------------------------------
l_CostoTotalAnual =tkinter.Label(segunda_va, text="Costo total anual")
l_CostoTotalAnual.place(x=15, y=440, width=175,height=25)

l_entrada_CostoTotalAnual =tkinter.Label(segunda_va, text="")
l_entrada_CostoTotalAnual.place(x=220, y=440, width=130,height=25)

def CostoAnual(Q,S):
    D=e_Demanda.get()
    Cp=e_CostoPedido.get()
    Cmi=e_CostoInventario.get()
    Cf=e_CostoFaltante.get()
    Cu=e_CostoUnitario.get()   
    Cta = (float(Cu)*float(D))+((float(D)/float(Q))*float(Cp))+(((math.pow((float(Q)-float(S)),2))/(2*float(D)))*float(Cmi))+(((math.pow(float(S),2))/(2*float(Q)))*float(Cf))
    Cta=int(Cta)
    l_entrada_CostoTotalAnual.config(text=Cta)

def UnidadesAgotdas(Q):
    D=e_Demanda.get()
    Cp=e_CostoPedido.get()
    Cmi=e_CostoInventario.get()
    Cf=e_CostoFaltante.get()
    S = math.sqrt((2*float(Cp)*float(D)*float(Cmi))/(float(Cf)*(float(Cmi)+float(Cf))))  
    if (abs(S) - abs(int(S)) != 0):
        S = S-(abs(S) - abs(int(S)))+1 
    S=int(S)
    l_entrada_UnidadesAgotadas.config(text=S)  
    CostoAnual(Q,S)

def CantidadOptima():
    D=e_Demanda.get()
    Cp=e_CostoPedido.get()
    Cmi=e_CostoInventario.get()
    Cf=e_CostoFaltante.get()
    Q=math.sqrt((2*float(Cp)*float(D)*(float(Cmi)+float(Cf)))/(float(Cf)*float(Cmi)))
    Q=int(Q)
    l_entrada_CantidadOptima.config(text=Q)
    UnidadesAgotdas(Q)

button_calcular=tkinter.Button(segunda_va,
    text="Calcular",
    command=CantidadOptima,
    )
button_calcular.place(x=290,y=520,width=100,height=50)
segunda_va.mainloop()