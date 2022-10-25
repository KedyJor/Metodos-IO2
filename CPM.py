#import numpy as np
from cmath import nan
import pandas as pd
import re


class Tarea():
    def __init__(self,Nombre,Duracion,Predecesor):
        self.Nombre = Nombre
        self.Duracion = Duracion
        self.Predecesor = Predecesor
        self.Sucesores = []
        self.holgura = 0
        self.critica = ''
        self.IC= 0
        self.TC= 0
        self.IL= 0
        self.TL= 0
        self.ESTADO =''
       
    def obtener_holgura(self):
        self.holgura = self.TL - self.TC
        if self.holgura == 0:
            self.critica = 'si'
        else: 
            self.critica = 'no'

        

def ObtenerDatos(file,hoja):
    Datos=pd.read_excel(file,sheet_name= hoja)
    return Datos


def CrearActividades(Datos):
    Tareas = []
    for i in range(len(Datos)):
        Tareas.append(Tarea(Datos['NOMBRE'][i], Datos['DURACION'][i],Datos['PREDECESOR'][i]))

    return Tareas


def HaciaAdelante(Tareas):
    
    aux = []
    for Tarea in Tareas:
        if type(Tarea.Predecesor) is str:
            IC_Lista = []
            for i in Tarea.Predecesor:
                for j in Tareas:
                    if j.Nombre == i:
                        IC_Lista.append(j.TC)
                        aux.append(j.TC)
                Tarea.IC = max(IC_Lista)

            del IC_Lista

        else:
            Tarea.IC = 0

        Tarea.TC = Tarea.IC + Tarea.Duracion


def HaciaAtras(Tareas):
    
    predecer = []
    ef = []

    for Tarea in Tareas:
        if type(Tarea.Predecesor) is str:
            for j in Tarea.Predecesor:
                Patron = re.compile(r'[A-Z]')
                Match = Patron.finditer(j)
                for r in Match:
                    predecer.append(j)

                    for m in Tareas:
                        if m.Nombre == j:
                            m.Sucesores.append(Tarea.Nombre)
        ef.append(Tarea.TC)

    for Tarea in reversed(Tareas):
        if Tarea.Nombre not in predecer:
            Tarea.TL = max(ef)
        else:

            minimos = []
            for x in Tarea.Sucesores:
                for t in (Tareas):
                    if t.Nombre == x:
                        minimos.append(t.IL)
            Tarea.TL = min(minimos)
            del minimos
        Tarea.IL = Tarea.TL - Tarea.Duracion


def Holgura(Tareas):
    for Tarea in Tareas:
        Tarea.obtener_holgura()


def ActualizarDatos(Datos,Tareas):
        Datos1 = pd.DataFrame({
        'NOMBRE' : Datos['NOMBRE'],
        'PREDECESOR' : Datos['PREDECESOR'],
        'DURACION' : Datos['DURACION'],
        'IC' : pd.Series([Tarea.IC for Tarea in Tareas]),
        'TC' : pd.Series([Tarea.TC for Tarea in Tareas]),
        'IL' : pd.Series([Tarea.IL for Tarea in Tareas]),
        'TL' : pd.Series([Tarea.TL for Tarea in Tareas]),
        'HOLGURA' : pd.Series([Tarea.holgura for Tarea in Tareas]),
        'CPM' : pd.Series([Tarea.critica for Tarea in Tareas]),
        })
        return Datos1

def main():

    a = ObtenerDatos("TablaA.xlsx","Hoja1")
    ad = CrearActividades(a)
    HaciaAdelante(ad)
    HaciaAtras(ad)
    Holgura(ad)
    a1=ActualizarDatos(a,ad)
    print(a1)


main()
