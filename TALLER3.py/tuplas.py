#ejercicio 1

"""numeros = (3, 8, 11, 14, 17, 20)
par = []
impar = []
for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print("números pares:", tuple(par))
print("números impares:", tuple(impar))

#ejercicio 2

numeros = (13, 4, 20, 10, 30, 1, 18, 84)
maximo = max(numeros)
minimo = min(numeros)
print("El número mayor es:", maximo)
print("El número menor es:", minimo)

#ejercicio 3

numeros = ()
cantidad = int(input("Ingresa la cantidad de números que deseas agregar a la tupla: "))

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    numeros += (numero,)

print("La tupla generada es:", numeros)

numero = int(input("Ingresa un número para buscar en la tupla: "))

if numero in numeros:
    cuenta = numeros.count(numero)
    print("El número", numero, "se encuentra", cuenta, "veces en la tupla.")
else:
    print("El número", numero, "no se encuentra en la tupla.")
    
    
#ejercicio 4 

contactos = {}

while True:
    print("\n--- contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")
    
    opcion = input("Ingrese una opción (1-3): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in contactos:
            print("El nombre ya existe en la agenda")
        else:
            telefono = input("Ingrese el teléfono del contacto: ")
            contactos[nombre] = telefono
            print("Contacto agregado con éxito")
    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos en la agenda")
        else:
            print("--- CONTACTOS ---")
            for nombre, telefono in contactos.items():
                print(nombre, ":", telefono)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida")
        
#ejercicio 5

#se agrega otro menu en la opcion 3 para que solicite el usuario y pida la clave

contactos = {}

while True:
    print("\n--- contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar teléfono")
    print("4. Salir")
    
    opcion = input("Ingrese una opción (1-4): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in contactos:
            print("El nombre ya existe en la agenda")
        else:
            telefono = input("Ingrese el teléfono del contacto: ")
            contactos[nombre] = telefono
            print("Contacto agregado con éxito")
    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos en la agenda")
        else:
            print("--- CONTACTOS ---")
            for nombre, telefono in contactos.items():
                print(nombre, ":", telefono)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in contactos:
            telefono = contactos[nombre]
            print("El teléfono de", nombre, "es:", telefono)
        else:
            print("El contacto no está en los contactos")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida")
        
#ejercicio 6

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Ingrese un índice (1-10): ")) - 1

if indice >= 0 and indice < 10:
    valor = tupla[indice]
    print("El valor en el índice", indice+1, "es:", valor)
else:
    print("El índice ingresado no es válido")
    
    
    
#validacion con otros numeros

tupla = (10, 20 , 30 ,40)

indice = int(input("Ingrese un índice (1-4): ")) - 1

if indice >= 0 and indice < 4:
    valor = tupla[indice]
    print("El valor en el índice", indice+1, "es:", valor)
else:
    print("El índice ingresado no es válido")
    
    
#LISTAS

#Ejercicion 1  encuentra el error

#A

#lista_colores ["rojo", "azul", "verde","amarillo"]
#print ("la lista de colores es: ", lista_colores (0))

#en este caso no tiene el = que es necesario para asignar los valores a la lista,  después del nombre de la 
# variable lista_colores



lista_colores = ["rojo", "azul", "verde","amarillo"]


#B
# En este caso es redundate usar el -0 ya que es lo mismo que 0 o posicion 1 
# En la posicion -4 tambien hay error ya que está fuera de los límites de la lista (la lista solo tiene tres elementos)
#los valores deben estar entre corchetes [ ]. Además, falta el signo =
#en el print para buscar la posicion de un objeto en la lista se una son los [] y no el () 
# en la posicion 0

#lista_colores ["rojo", "azul", "verde",}
#print ( "el color es: ", lista_colores [0])

lista_colores= ["rojo", "azul", "verde",]
print (lista_colores [-0])
print (lista_colores [-4])


#corregido seria asi:

lista_colores= ["rojo", "azul", "verde",]
print (lista_colores [0])
print (lista_colores [-1])

#ejercicio 2 de listas"""

departamentos_colombia = []
cantidad_departamentos = int(input("Ingrese la cantidad de departamentos a ingresar: "))

for i in range(cantidad_departamentos):
    departamento = input("Ingrese el nombre del departamento de Colombia que desee: ")
    departamentos_colombia.append(departamento)

departamentos_colombia.sort(reverse=True)

print("Lista de departamentos en orden descendente:", departamentos_colombia)
print("Los dos últimos departamentos ingresados son: {} y {}".format(departamentos_colombia[-0], departamentos_colombia[-2]))

#ejercicio 3 de listas

"""numeros = []

cantidad_numeros = int(input("Ingrese la cantidad de números enteros a ingresar: "))

for i in range(cantidad_numeros):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

numeros_ascendente = sorted(numeros)
numeros_descendente = sorted(numeros, reverse=True)

print("Lista de números en orden ascendente: ", numeros_ascendente)
print("Lista de números en orden descendente: ", numeros_descendente)"""


