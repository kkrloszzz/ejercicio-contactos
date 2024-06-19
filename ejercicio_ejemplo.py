import os
import time
from funciones import *

while True:
    os.system('cls')
    print("MENU CONTACTOS")
    print("1. AGREGAR CONTENIDO\n2.VER CONTACTOS\n3.EXPORTAR ARCHIVO CSV\n4.Salir")
    opc = int(input("Ingrese opción: "))
    if opc==1:
        opcion_1()

    elif opc==2:
        opcion_2()

    elif opc==3:
        opcion_3()

    else:
        opcion_4()
        
