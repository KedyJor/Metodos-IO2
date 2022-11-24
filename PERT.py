import numpy as np
from cmath import nan
import pandas as pd
import re


class Tarea():
    def __init__(self,Nombre,Duracion,Predecesor,TP,TM,TO):
        self.Nombre = Nombre
        self.Duracion = Duracion
        self.Predecesor = Predecesor
        self.TP = TP
        self.TM = TM
        self.TO = TO
        self.Varianza = 0
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

    def obtener_varianza(self):
        self.Varianza = ((self.TP - self.TO)**2)/36       


def HaciaAdelante(Tareas):
    
    
    for Tarea in Tareas:
        if type(Tarea.Predecesor) is str:
            IC_Lista = []
            for i in Tarea.Predecesor:
                for j in Tareas:
                    if j.Nombre == i:
                        IC_Lista.append(j.TC)
                        
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

def Varianza(Tareas):
    for Tarea in Tareas:
        Tarea.obtener_varianza()

def Desviacion(Tareas):
    Desviacion = 0
    for Tarea in Tareas:
        if Tarea.holgura == 0:
            Desviacion = Desviacion + Tarea.Varianza
    Desviacion = Desviacion**(0.5)

    return Desviacion

def RTC(Tareas):
    rtc = []
    for Tarea in Tareas:
        if Tarea.holgura == 0:
            rtc.append(Tarea.Nombre)

    return rtc