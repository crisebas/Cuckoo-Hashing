import hashlib
from time import time #importamos la función time para capturar tiempos
n = 11
tabla01 = [i*0 for i in range(n)]
tabla02 = [i*0 for i in range(n)]
reiniciar = 0 
acumulador =0

lista = ["Aba", "Abaco", "Abbas", "Abeni", "Abram", "Abundio", "Absalon", "Acilino", "Acindino", "Adela", "Adelfa"]
"""
lista= ["Aba", "Abaco", "Abbas", "Abeni", "Abram", "Abundio",
         "Absalon", "Acilino", "Acindino", "Adela", "Adelfa", "Aranza",
         "Carimi", "Carmen", "Candido", "Candice", "Cancio", "Carauno",
         "Carlos", "Celfa", "Cetmilena", "Chabela", "Cedric", "Celsa"]


lista= ["Aba", "Abaco", "Abbas", "Abeni", "Abram", "Abundio",
         "Absalon", "Acilino", "Acindino", "Adela", "Adelfa", "Aranza",
         "Carimi", "Carmen", "Candido", "Candice", "Cancio", "Carauno",
         "Carlos", "Celfa", "Cetmilena", "Chabela", "Cedric", "Celsa",
         "Dimpa", "Dirck", "Domingo", "Dominica", "Dominique", "Domma",
         "Dionisio", "Eutimio", "Evelin", "Evelina", "Evo", "Flavia",
         "Finola", "Florente", "Fitzpatrick", "Flama", "Florida", "Flann",
         "Francisca", "Fresta", "Jonah", "Jovinas", "Jocabed", "Jorell"]

"""
#clave: funcion hash de la palabra
def fhash(nfuncion, elemento):
    if (nfuncion==1):
        return (int(hash(elemento)))%n 
    if (nfuncion==2):
        return (int(hash(elemento))+5)%n 
    
def insertar(elemento, tabla01, tabla02, n_operaciones):
    global n
    global reiniciar
    reiniciar = 0
    i = 0
    #Cuando la funcion ha ejecutado n veces recursivamente
    # se expande la cada una de las tablas en una unidad
    if(n_operaciones>= n):
        while i<n:
            tabla01[i]=0
            tabla02[i]=0
            i = i+1
        tabla01.append(0)
        tabla02.append(0)
        n = n + 1
        # indica que se debe inicializar la insercion con el nuevo tamaño
        reiniciar = reiniciar +1 
        return
    #Posicion libre
    if(tabla01[fhash(1,elemento)]==0): 
        tabla01[fhash(1,elemento)] = elemento
    else:
        aux = tabla01[fhash(1,elemento)] # copiar el elemento q se va ha mover
        tabla01[fhash(1,elemento)] = elemento
        if (tabla02[fhash(2,elemento)] == 0):
            tabla02[fhash(2,elemento)] = aux
        else:
            nuevo_elemento = tabla02[fhash(2,elemento)]
            tabla02[fhash(2,elemento)] = aux
            insertar( nuevo_elemento, tabla01, tabla02, n_operaciones+1)
    
    
def cuckoo_hash(lista, tabla01, tabla02):
    global reiniciar
    i = 0
    t = len(lista)
    while i<t:
        insertar(lista[i], tabla01, tabla02, 0)
        if(reiniciar==1):
            i = 0 #inicia de nuevo la insercion
            continue
        i = i+1
    
def busqueda(tabla01, tabla02, buscar):
    global acumulador
    tiempo_inicial = time()
    if(tabla01[fhash(1, buscar)]== buscar):
        print("")
    elif(tabla02[fhash(2, buscar)]== buscar):
        print("")
    else:
        print("no existe")
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    acumulador = acumulador + tiempo_ejecucion
    print(tiempo_ejecucion)         

cuckoo_hash(lista, tabla01, tabla02)
for elementos in lista:
    busqueda(tabla01, tabla02, elementos)
print("Promedio: ", acumulador/n)


