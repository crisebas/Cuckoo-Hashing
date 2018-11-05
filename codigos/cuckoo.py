#Implementación del código del Hash del cuco

n = 7			#tamaño de las tablas hash
ver = 2			#numero de tablas y funciones hash
hashTable = [[i*0 for i in range(n)], [i*0 for i in range(n)]]	#inicializamos las tablas en 0
pos = [0, 0]	#guardara las salidas de la funcion hash
aux = []		#guardara los elementos que no pueda posicionar por encontrar un ciclo.

def funcion_hash(funcion, clave):
    suma = 0
    for i in clave:
        suma+=ord(i)			#suma de ascii de cada letra
    if(funcion == 1):
        return suma%n
    elif(funcion == 2):
        return n-(suma%n)-1
        

def colocar(clave, tabla, cont, n): 
    if (cont == n):								#detecta el bucle al intentar posicionar
        aux.append(clave)						#guardamos el elemento en una lista auxiliar
        return
    for i in range(ver):
        pos[i] = funcion_hash(i+1, clave)		#hallamos los indices para posicionarlo en cada tabla
    if (hashTable[tabla][pos[tabla]] != 0):		#si encuentra un elemento en la posicion que quiero
        save = hashTable[tabla][pos[tabla]]		#guardamos ese elemento
        hashTable[tabla][pos[tabla]] = clave	#y posicionamos la clave en el lugar que queremos
        colocar(save, (tabla+1)%ver, cont+1, n)	#colocando el que estaba ahi, en la otra tabla
    else:
        hashTable[tabla][pos[tabla]] = clave;	#si no hay un elemento, simplemente lo coloca ahi

def actualizar_tabla():
    global hashTable
    hashTable = [[i*0 for i in range(n)], [i*0 for i in range(n)]]    
        
def cuckoo(valores, n):
    for i in valores:
        cont = 0
        colocar(i, 0, cont, n)				#colocar todos los valores
    contraseña = [l for l in hashTable[0] if l != 0] + [l for l in hashTable[1] if l != 0] + aux #concatenamos sin los ceros
    cadena = "".join(contraseña)			#lo convertimos a cadena
    actualizar_tabla()						#actualizamos la tabla en ceros al final para la siguiente cadena
    return cadena
