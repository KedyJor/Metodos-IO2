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
    ventana2.configure(bg="orange")
    #ventana3 = Frame(ventana3,width=1200,height=800)
    #ventana3.pack()

    label7=Label(ventana2,text="ACTIVIDAD",bg="orange",fg="#2F4F4F",font="consolas 11 bold")
    label7.grid(row=0, column=0)
    label8=Label(ventana2,text="DURACION",bg="orange",fg="#2F4F4F",font="consolas 11 bold")
    label8.grid(row=0, column=1)
    label9=Label(ventana2,text="PREDECESORES",bg="orange",fg="#2F4F4F",font="consolas 11 bold")
    label9.grid(row=0, column=2)

    
    for row in range(ac):
        for column in range(3):
            lav=Entry(ventana2)
            lav.grid(row=row+1, column=column, sticky="nsew", padx=5, pady=5)
            aux.append(lav)
                        
    Gen1=Button(ventana2,text="Calcular",command=lambda :apendear(aux,ac),font="arial 10 bold")
    Gen1.grid(row=ac+1, column=1,pady=10)
    
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
    ventana3.configure(bg="orange")

    label17=Label(ventana3,text="ACTIVIDAD",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label17.grid(row=0, column=0)
    label18=Label(ventana3,text="DURACION",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label18.grid(row=0, column=1)
    label19=Label(ventana3,text="PREDECESORES",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label19.grid(row=0, column=2)
    label20=Label(ventana3,text="IC",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label20.grid(row=0, column=3)
    label21=Label(ventana3,text="TC",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label21.grid(row=0, column=4)
    label22=Label(ventana3,text="IL",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label22.grid(row=0, column=5)
    label23=Label(ventana3,text="TL",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
    label23.grid(row=0, column=6)
    label24=Label(ventana3,text="HOLGURA",bg="orange",fg="#2F4F4F",font="consolas 10 bold")
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

    labelRT=Label(ventana3,text="Ruta Critica",bg="orange",fg="black",font="Arial 10 bold")        
    labelRT.grid(row=c+2, column=0)
    labelRT1=Label(ventana3,text=RTC(Tareas),bg="orange",fg="#2F4F4F",font="consolas 10 bold")        
    labelRT1.grid(row=c+3, column=0)
    labelRT2=Label(ventana3,text="Ocurrencia Temprana",bg="orange",fg="black",font="Arial 10 bold")        
    labelRT2.grid(row=c+2, column=1)
    labelRT3=Label(ventana3,text=Tareas[c-1].TC,bg="orange",fg="#2F4F4F",font="consolas 10 bold")        
    labelRT3.grid(row=c+3, column=1)
    labelRT2=Label(ventana3,text="Ocurrencia Tardia",bg="orange",fg="black",font="Arial 10 bold")        
    labelRT2.grid(row=c+2, column=2)
    labelRT3=Label(ventana3,text=Tareas[0].TL,bg="orange",fg="#2F4F4F",font="consolas 10 bold")        
    labelRT3.grid(row=c+3, column=2)

ventana1.title("CPM")
ventana1.geometry('300x200')
ventana1.configure(bg="orange")
label1=Label(ventana1,text="CPM",bg="#D2691E",fg="white",font="consolas 40 bold",width=40).pack(padx=5,pady=5)
label2=Label(ventana1,text="Numero de Tareas",bg="orange",font="arial 10 bold").pack(padx=15,pady=5,anchor=CENTER)
Ntareas = IntVar()
Entrada1=Entry(ventana1,textvariable=Ntareas).pack(padx=15,pady=5,anchor=CENTER)
Gen=Button(ventana1,text="Generar",font="arial 10 bold",command=Aventana2).pack(padx=15,pady=5,anchor=CENTER)

#command=sumbmitForm3
ventana1.mainloop()
