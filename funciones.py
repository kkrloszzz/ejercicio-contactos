import os
import time
import csv

contactos = []




def opcion_1():
    os.system('cls') 
    print("AGREGAR CONTACTO")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
    contacto = {"nombre":nombre,"telefono":telefono,"correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO!")
    time.sleep(2)


def opcion_2():
    if not contactos:
        os.system('cls')
        print("NO EXISTEN CONTACTOS REGISTRADOS")
        time.sleep(2)
        os.system('cls')
        
    else:
        print("\tLISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELÉFONO: {c['telefono']}")
            print(f"CORREO: {c['correo']}")
            time.sleep(4)
        

def opcion_3():
    if not contactos:
        os.system('cls')
        print("NO EXISTEN CONTACTOS REGISTRADOS")
        time.sleep(2)
        os.system('cls')
    else:
        nombre_archivo = input("Ingrese Nombre del archivo:")+".csv"
        with open(nombre_archivo,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, contactos[0].keys())
            escritor.writerows(contactos)                
            

def opcion_4():
    os.system('cls')
    print("GRACIAS POR PREFERIRNOS!")
    time.sleep(3)
    exit()

def validar_nombre():
    while True:
        nom = input("Ingrese Nombre: ")
        if len(nom.strip()) >=3 and nom.isalpha():
            return nom
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 CARACTERES Y SOLO LETRAS!")



def validar_telefono():
    while True:
        try:
            tel = int(input("Ingrese Número del Teléfono: "))
            if len(str(tel))==9 and str(tel)[0]=='9':
                return tel
            else:
                print("ERROR! EL TELÉFONO DEBE COMENZAR CON 9 Y TENER 9 DÍGITOS!")
                time.sleep(2)
                os.system('cls')
        except:
            os.system('cls')
            print("ERROR! INGRESE NÚMERO ENTERO")
            time.sleep(2)
            os.system('cls')

def validar_correo():
    while True:
        #patterns
        cor = input("Ingrese correo GMAIL: ")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip())>=13:
            return cor
        else:
            print("ERROR! CORREO INCORRECTO, SOLO GMAIL!")