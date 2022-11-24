from tkinter import *
import tkinter
import math

cuarta_va = tkinter.Tk()

# dimesion del cuadro

cuarta_va.geometry("435x600")
cuarta_va.title("ESIS")
# expansion de la ventana
cuarta_va.resizable(0, 0)
# imagen -> cuarta_va.iconbitmap("descarga.ico") #

# el color #
cuarta_va.config(background="#213141")

l_titulo = tkinter.Label(cuarta_va, 
                        text="Inventario de periodo unico con demanda probabilística",
                        font= "#56CD63",
                        fg="green",
                        width="50",
                        height="2"
                        )


l_titulo.place( y=10)
#-----------------------------------------------------------------------
l_CostoCompra = tkinter.Label(cuarta_va, text="CostoCompra")
l_CostoCompra.place(x=15,y=70, width=170,height=25)

e_CostoCompra=tkinter.Entry(cuarta_va)
e_CostoCompra.place(x=200, y=70, width=170,height=25)
#-----------------------------------------------------------------------
l_PrecioLiquidacion = tkinter.Label(cuarta_va, text="Costo de liquidación")
l_PrecioLiquidacion.place(x=15,y=120, width=170,height=25)

e_PrecioLiquidacion=tkinter.Entry(cuarta_va)
e_PrecioLiquidacion.place(x=200, y=120, width=170,height=25)
#-----------------------------------------------------------------------
l_CostoRegular = tkinter.Label(cuarta_va, text="Costo regular")
l_CostoRegular.place(x=15,y=170, width=170,height=25)

e_CostoRegular=tkinter.Entry(cuarta_va)
e_CostoRegular.place(x=200, y=170, width=170,height=25)
#-----------------------------------------------------------------------
l_Min = tkinter.Label(cuarta_va, text="Ventas minimas")
l_Min.place(x=15,y=230, width=170,height=25)

e_Min=tkinter.Entry(cuarta_va)
e_Min.place(x=200, y=230, width=170,height=25)
#-----------------------------------------------------------------------
l_Max = tkinter.Label(cuarta_va, text="Ventas maximas")
l_Max.place(x=15,y=280, width=170,height=25)

e_Max=tkinter.Entry(cuarta_va)
e_Max.place(x=200, y=280, width=170,height=25)

#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CostoSobreEstimarD =tkinter.Label(cuarta_va, text="Costo de sobrestimar demanda")
l_CostoSobreEstimarD.place(x=15, y=340, width=180,height=25)

l_entrada_CostoSobreEstimarD =tkinter.Label(cuarta_va, text="")
l_entrada_CostoSobreEstimarD.place(x=220, y=340, width=180,height=25)
#-----------------------------------------------------------------------
l_CostoSubestimaD =tkinter.Label(cuarta_va, text="Costo de subestimar la demanda")
l_CostoSubestimaD.place(x=15, y=390, width=180,height=25)

l_entrada_CostoSubestimaD =tkinter.Label(cuarta_va, text="")
l_entrada_CostoSubestimaD.place(x=220, y=390, width=180,height=25)
#-----------------------------------------------------------------------
l_CantidadPedido =tkinter.Label(cuarta_va, text="Cantidad de pedido")
l_CantidadPedido.place(x=15, y=440, width=180,height=25)

l_entrada_CantidadPedido =tkinter.Label(cuarta_va, text="")
l_entrada_CantidadPedido.place(x=220, y=440, width=180,height=25)
#-----------------------------------------------------------------------

def CantidaOptimaP(PDmQ):
    min=e_Min.get()
    max=e_Max.get()
    pedido= (float(max)-float(min))*PDmQ
    Q=float(min)+float(pedido)
    Q=int(Q)
    l_entrada_CantidadPedido.config(text=Q)
    

def ProbDemanda(Cu,Co):
    PDmQ= (float(Cu))/(float(Cu)+float(Co))
    CantidaOptimaP(PDmQ)

def CostoSubestimarD(Pr,Cc,Co):
    Cu=float(Pr)-float(Cc)
    l_entrada_CostoSubestimaD.config(text=Cu)
    ProbDemanda(Cu,Co)


def CostoSobreEstimarD():
    Cc=e_CostoCompra.get()
    Pvl=e_PrecioLiquidacion.get()
    Pr= e_CostoRegular.get()
    Co=float(Cc)-float(Pvl)
    l_entrada_CostoSobreEstimarD.config(text=Co)
    CostoSubestimarD(Pr,Cc,Co)

button_calcular=tkinter.Button(cuarta_va,
    text="Calcular",
    command=CostoSobreEstimarD,
    )
button_calcular.place(x=290,y=520,width=100,height=50)

cuarta_va.mainloop()
