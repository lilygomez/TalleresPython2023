# Son mutables 
# Se representa con llaves 
diccionario ={}
Dicc1 ={"clave":"valor","clave":"valor"}
#Las claves deben ser unicas 
datos = {"Nombre1":"Nayroby",
         "Nombre2":"Karina",
         "Apellido":"Valencia",
         "Edad":15}

'''datos1 = dict(Nombre1 = "Nayroby",
            Nombre2="Karina",
            Apellido = "Valencia",
            Edad = 15)
print(datos1)'''

#Acceder a un valor del diccionario : get()
print(datos["Edad"])

print(datos.get("Apellido"))

# Modificar un valor.
datos["Edad"]= 23
datos["fechaNacimiento"]= "07/08/1999"# se agrega al no existir 
print(datos)
#Eliminar elemnetos  del diccionario: del, pop()
'''del datos["Nombre1"]
print(datos)'''
datos.pop("Edad")
print(datos)
#Para eliminar el ultimo elemento : popitems()
datos.popitem()
print(datos)

# Acceder a las claves : keys()
Claves = datos.keys()
print(Claves)
for Clave in datos.keys():
    print(Clave)
# Acceder a los valores: values()

Valores = datos.values()
print(Valores)

for valor in datos.values():
    print(valor)
#Acceder alas claves y valores: items()
elem = datos.items()
print(elem)

for elem in datos.items():
    print(elem)
    
for C, V in datos.items():
    print(C , " ", V)
    
#update(): actualizar el diccionario 

objetos = {
    "objeto1":"carro",
    "objeto2":"avion",
    "objeto3":"camion",
    "objeto4":"bus"
}
datos.update(objetos)
print(datos)
#eliminar todos los datos del diccionario : clear()
datos.clear()
print(datos)

#EJERCICIO
'''Crear 1 dicionario llamado tienda, 
el usuario debe ingresar la cantidad de articulos que desea almacenaren la tienda,
elemnetos (clave),precios(valor). S el elemento ya se encuentra e el atienda debe informarlo
añ usuario, de lo contrario debe ingresarlo Mostrar la info almacenada en tieda (elemn, precio)'''

Tienda = {}
cantidadElementos =int(input("Ingrese la cantidad de elementos de la tienda: "))
for i in range (cantidadElementos):
    Articulo = input("ingrese el nombre del articulo")
    if Articulo in Tienda:
        print(f"El articulo {Articulo} ya se encuentra en la tienda ")
    else:
        Precio = int(input(f"ingrese valor del articulo {Articulo}"))
        Tienda[Articulo]= Precio
print("************* TIENDA ***********")
for Articulo, Precio in Tienda.items():
    print("%s tiene un precio de : %d" %(Articulo,Precio))    