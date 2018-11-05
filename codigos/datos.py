#Manejo de archivos csv para la base de datos

import csv
import pandas as pd

def crear_archivo(base_de_datos):
    archivo = open(base_de_datos, "w")
    archivo.write("Usuario,Contraseña\n")
    archivo.close()

def guardar_datos(base_de_datos, datos):	#base_de_datos es un archivo con los datos, datos es una lista
    archivo = open(base_de_datos, "a")		#abrimos el archivo para escritura al final
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)			#llenamos la fila del archivo
    archivo.close()							#cerramos el archivo

def existencia_usuario(base_de_datos, usuario):
    ok = 0
    archivo = open(base_de_datos, "r")
    archivo_csv = csv.reader(archivo)
    for row in archivo_csv:				#vemos linea por linea
        if row[0] == usuario:			#si existe el usuario
            ok = 1
            break
    archivo.close()
    if ok == 0:
        return False
    elif ok == 1:
        return True
    
def validar_datos(base_de_datos, datos):
    ok = 0
    archivo = open(base_de_datos, "r")
    archivo_csv = csv.reader(archivo)
    for row in archivo_csv:								#vemos linea por linea
        if row[0] == datos[0] and row[1] == datos[1]:	#si coincide el usuario y contraseña
            ok = 1
            break
    archivo.close()
    if ok == 0:
        return False
    elif ok == 1:
        return True

def mostrar_tabla(base_de_datos):						#para mostrar la tabla
    tabla = pd.read_csv("base_de_datos.csv")
    print(tabla)