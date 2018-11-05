#Manejo de los datos al recibirlos

import datos
import cuckoo

datos.crear_archivo("base_de_datos.csv")		#creamos el archivo para la base de datos


def recibir_para_guardar():
    ex = True
    while ex:
        usuario = input("\nIngrese usuario: ")
        ex = datos.existencia_usuario("base_de_datos.csv", usuario)	#vemos si existe ese nombre de usuario en la base de datos
        if ex:
            print("El nombre de usuario ya existe.")
    print("Nombre de usuario valido.")
    contraseña = input("Ingrese contraseña: ")
    return usuario, contraseña

def recibir_para_validar():
    usuario = input("\nIngrese usuario: ")
    contraseña1 = input("Ingrese contraseña: ")
    contraseña2 = transformar_entrada(contraseña1)
    return usuario, contraseña2

def transformar_entrada(entrada):
    cadena_aux = (",").join(entrada)		#añadimos comas entre cada letra del string	
    cadena = cadena_aux.split(",")			#y lo convertimos a lista de letras
    return cadena


def guardando_datos():
    usuario, contraseña = recibir_para_guardar()
    cadena = cuckoo.cuckoo(contraseña, len(contraseña))		#aplicamos el hash del cuco a la contraseña
    entrada = [(usuario, cadena)]
    datos.guardar_datos("base_de_datos.csv", entrada)		#y lo guardamos(encriptado) en la base de datos
    print("Bienvenido {}, te registraste con exito.".format(usuario))
    
def validando_datos():
    usuario, contraseña = recibir_para_validar()
    cadena = cuckoo.cuckoo(contraseña, len(contraseña))		#aplicamos el hash del cuco a la contraseña
    entrada = (usuario, cadena)
    ex = datos.validar_datos("base_de_datos.csv", entrada)	#y verificamos si esta en la base de datos
    if ex:
        print("El usuario esta registrado.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        