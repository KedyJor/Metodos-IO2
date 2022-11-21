from tkinter import *
from tkinter.ttk import Notebook,Entry
from CPM import *

ventana1=Tk()

def Aventana2():
    aux = []
    ac = int(Ntareas.get())
    Trs = []

    ventana1.withdraw()
    ventana2 =Toplevel()
    #ventana3 = Frame(ventana3,width=1200,height=800)
    #ventana3.pack()

    label7=Label(ventana2,text="ACTIVIDAD")
    label7.grid(row=0, column=0)
    label8=Label(ventana2,text="DURACION")
    label8.grid(row=0, column=1)
    label9=Label(ventana2,text="PREDECESORES")
    label9.grid(row=0, column=2)

    
    for row in range(ac):
        for column in range(3):
            lav=Entry(ventana2)
            lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            aux.append(lav)
                        
    Gen1=Button(ventana2,text="CALCULAR",command=lambda :apendear(aux,ac))
    Gen1.grid(row=ac+1, column=1,pady=20)
    
    ventana2.mainloop()
 
def apendear(lis,cant):
    Laux= []
    Act = []
    for v in range(cant):
        v = []
        Act.append(v)
    

    for i in lis:
        Laux.append(i.get())
   
    Laux = list(Laux)   
    a = 0
    b = 3
    for fil in Act:
        for j in Laux[a:b]:
            fil.append(j)
            
        a = a+3
        b = b+3

    Tareas = []
   
    for j in range(len(Act)):
        Tareas.append(Tarea(Act[j][0],int(Act[j][1]),Act[j][2]))
    HaciaAdelante(Tareas)
    HaciaAtras(Tareas)
    Holgura(Tareas)
    Aventana3(cant,Tareas)
    
def Aventana3(c,Tareas):
    
    ventana3 =Toplevel()
    ventana3.mainloop

    label17=Label(ventana3,text="ACTIVIDAD")
    label17.grid(row=0, column=0)
    label18=Label(ventana3,text="DURACION")
    label18.grid(row=0, column=1)
    label19=Label(ventana3,text="PREDECESORES")
    label19.grid(row=0, column=2)
    label20=Label(ventana3,text="IC")
    label20.grid(row=0, column=3)
    label21=Label(ventana3,text="TC")
    label21.grid(row=0, column=4)
    label22=Label(ventana3,text="IL")
    label22.grid(row=0, column=5)
    label23=Label(ventana3,text="TL")
    label23.grid(row=0, column=6)
    label24=Label(ventana3,text="HOLGURA")
    label24.grid(row=0, column=7)
    
    
    for row in range(c):
        for column in range(8):
            if column == 0:
                lav=Label(ventana3,text = Tareas[row].Nombre)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 1:
                lav=Label(ventana3,text = Tareas[row].Duracion)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column ==2:
                lav=Label(ventana3,text = Tareas[row].Predecesor)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 3:
                lav=Label(ventana3,text = Tareas[row].IC)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 4:
                lav=Label(ventana3,text = Tareas[row].TC)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 5:
                lav=Label(ventana3,text = Tareas[row].IL)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 6:
                lav=Label(ventana3,text = Tareas[row].TL)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            elif column == 7:
                lav=Label(ventana3,text = Tareas[row].holgura)
                lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            else:
                g =1


ventana1.title("Metodo De la Ruta Critica")
ventana1.geometry('380x300')

label1=Label(ventana1,text="CPM").pack(padx=5,pady=5,anchor=W)
label2=Label(ventana1,text="Numero de Tareas").pack(padx=15,pady=5,anchor=W)
Ntareas = IntVar()
Entrada1=Entry(ventana1,textvariable=Ntareas).pack(padx=15,pady=5,anchor=W)

Gen=Button(ventana1,text="Generar",command=Aventana2).pack(padx=15,pady=5,anchor=W)

#command=sumbmitForm3
ventana1.mainloop()
