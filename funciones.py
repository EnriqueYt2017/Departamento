import os
import numpy as np
import msvcrt
from colorama import Fore,Style,Back ,init
init()
init(autoreset=True)

depas=np.empty([2,10,4],object)

def dibujaredificio():
    print(F'{Style.BRIGHT}    A   B   C   D ')
    for x in range(10): #filas
        if 10-x<10:
            print(f'0{10-x}',end='|')
        else:
            print(10-x,end='|')
        for y in range(4): #Columnas
            if depas[0,x,y]==None:
                print(f'🟩',end='|')
            else:
                print(f'🟥',end='|')
        print(' ')

def limpiarpantalla():
    pass

def printr(texto):
    pass

def comprardepa(piso,columna):
    pass

def pagar(costo,pago):
    pass

def buscardueno(nombre):
    pass

