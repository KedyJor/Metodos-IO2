from tkinter import *
import tkinter
import math

primera_va = tkinter.Tk()

# dimesion del cuadro

primera_va.geometry("440x600")
primera_va.title("ESIS")
# expansion de la ventana
primera_va.resizable(0, 0)
# imagen -> primera_va.iconbitmap("descarga.ico") #

# el color #
primera_va.config(background="#213141")

l_titulo = tkinter.Label(primera_va, 
                        text="Modelo de tamaño del lote de producción aconómica",
                        font= "#56CD63",
                        fg="green",
                        width="50",
                        height="2"
                        )


l_titulo.place( y=10)
#-----------------------------------------------------------------------
l_ProduccionAnual = tkinter.Label(primera_va, text="Producción anual")
l_ProduccionAnual.place(x=15,y=70, width=120,height=25)

e_ProduccionAnual=tkinter.Entry(primera_va)
e_ProduccionAnual.place(x=150, y=70, width=120,height=25)
#-----------------------------------------------------------------------
l_DemandaAnual =tkinter.Label(primera_va, text="Demanda anual")
l_DemandaAnual.place(x=15, y=120, width=120,height=25)

e_DemandaAnual =tkinter.Entry(primera_va)
e_DemandaAnual.place(x=150, y=120, width=120,height=25)
#-----------------------------------------------------------------------
l_CostoPreparacion =tkinter.Label(primera_va, text="Costo de preparación")
l_CostoPreparacion.place(x=15, y=170, width=120,height=25)

e_CostoPreparacion =tkinter.Entry(primera_va)
e_CostoPreparacion.place(x=150, y=170, width=120,height=25)
#-----------------------------------------------------------------------
l_CostoRetencion =tkinter.Label(primera_va, text="Costo de retención")
l_CostoRetencion.place(x=15, y=220, width=120,height=25)

e_CostoRetencion =tkinter.Entry(primera_va)
e_CostoRetencion.place(x=150, y=220, width=120,height=25)
#-----------------------------------------------------------------------
#SALIDA
#-----------------------------------------------------------------------
l_CantUnidadesProducir =tkinter.Label(primera_va, text="Cantidad de unidades a producir")
l_CantUnidadesProducir.place(x=15, y=300, width=190,height=25)

l_entrada_CantUniProducir =tkinter.Label(primera_va, text="")
l_entrada_CantUniProducir.place(x=220, y=300, width=130,height=25)
#-----------------------------------------------------------------------
l_FaseAnio =tkinter.Label(primera_va, text="Fase por año")
l_FaseAnio.place(x=15, y=350, width=190,height=25)

l_entrada_FaseAnio =tkinter.Label(primera_va, text="")
l_entrada_FaseAnio.place(x=220, y=350, width=130,height=25)
#-----------------------------------------------------------------------
l_TiempoCiclo =tkinter.Label(primera_va, text="Tiempo de ciclo")
l_TiempoCiclo.place(x=15,y=400, width=190,height=25)

l_entrada_TiempoCiclo =tkinter.Label(primera_va, text="")
l_entrada_TiempoCiclo.place(x=220, y=400, width=130,height=25)
#-----------------------------------------------------------------------
l_CostoTotal =tkinter.Label(primera_va, text="Costo total")
l_CostoTotal.place(x=15,y=450, width=190,height=25)

l_entrada_CostoTotal =tkinter.Label(primera_va, text="")
l_entrada_CostoTotal.place(x=220, y=450, width=130,height=25)

def CostoTotal(Q,Ch,Co):
    D=e_DemandaAnual.get()
    P=e_ProduccionAnual.get()
    Tc=((1/2)*(1-(int(D)/int(P)))*int(Q)*int(Ch))+((int(D)/int(Q))*int(Co))
    l_entrada_CostoTotal.config(text=Tc)

def TiempoCiclo(Fase):
    T=12/int(Fase)
    l_entrada_TiempoCiclo.config(text=T)

def FasesAnio(Q):
    try:
        D=e_DemandaAnual.get()
        Fase=int(D)/int(Q)
        l_entrada_FaseAnio.config(text= Fase)
        TiempoCiclo(Fase)
    except ValueError:
        pass


def TamanioOptimoPedido():
    try:
        P=e_ProduccionAnual.get()
        D=e_DemandaAnual.get()
        Co=e_CostoPreparacion.get()
        Ch=e_CostoRetencion.get()
        Q=math.sqrt((2*float(D)*float(Co))/((1-(float(D)/float(P)))*float(Ch)))
        l_entrada_CantUniProducir.config(text="%.2f" % Q)
        FasesAnio(Q)
        CostoTotal(Q,Ch,Co)
    except ValueError:
        pass


button_calcular=tkinter.Button(primera_va,
    text="Calcular",
    command=TamanioOptimoPedido
    )
button_calcular.place(x=290,y=520,width=100,height=50)

primera_va.mainloop()
