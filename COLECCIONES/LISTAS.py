listas = [] #listas vacias
listas =[2, 1.30, "hola", True, False]
#mutables: modificar
#indexadas: que tiene el mismo indice y el ultimo elemento de la lista es -1
# se pueden ingresar varios metodos y poder modificarlos:
#len(): muestra la longitud de las listas(la cantidad de elementos que tiene la lista)
"""print(len(listas))
#ACCEDER A LA LISTA
print(listas[2])
print(listas[-2])

#MODIFICAR ELEMENTO en este se cambia el hola de la posicion 2 a colecciones
listas[2]="colecciones"
print(listas)

#RECORRER UNA LISTA nos muestra las lista de arriba a bajo
for elemento in listas:
    print(elemento)
    
#indice (posicion) recorre dem 0 a la cantidad de elementos de la lista en este caso de 0 a
#se usa la F
for elem in range(len(listas)):
    print(f"{listas[elem]} esta en la posicion {elem}") """
    
    #INSERTAR ELEMENTOS: insert (posicion, dato o elemento a ingresar), 
    # append (dato o elemento a ingresar) ingresa el elemento en la ultima posicion
    
"""Marcas_Autos =["Renault", "Chevrolet","Suzuki","Audi", "Kia"]
Marcas_Autos. insert(3, "Mazda")
Marcas_Autos. append("toyota")
print(Marcas_Autos)

#eliminar elementos: pop(posicion), remover(elemento)

Marcas_Autos.pop(5)
Marcas_Autos.remove("Chevrolet")
print(Marcas_Autos)

#RECONOCER LA POSICION DEL ELEMENTO: index(elementos)
posicion = Marcas_Autos.index("Suzuki")
print(posicion)

#Organizar lista: ascendente sort (), descendente sort(reverse=True)
Marcas_Autos.sort()
print(Marcas_Autos)
Marcas_Autos.sort(reverse=True)
print(Marcas_Autos)

#Extender la lista: extend(lista)
otras_marcas = ["Bmw","Ferrari","Telsa","Mercedez Benz"]
Marcas_Autos.extend(otras_marcas)
print(Marcas_Autos)

#Recorrer 2 o más listas al mismo tiempo 
animales = ["Gato","Leon","Ballena","Pajaro","Serpiente"]
tipo_a = ["Terrestre","Salvaje","Mamifero","Aereo","Reptil"]
for animal, tipo in zip(animales, tipo_a):
    print(f"{animal} es un animal tipo {tipo}")
    
#CONTAR ELEMENTOS REPETIDOS: conmunt(elemento)
numeros = [1,2,3,4,5,1,345,1,45,2,1,1,1,456]
contar = numeros.count(1)
print(contar)"""


#EJERCICIO:
#CREAR 2 LISTAs VACIAS UNA LLAMaDA TIENDA, OTRA LLAMADA PRECIO, 
# EL USUARIO DEBE INGRESAR EL NUMERO DE ARTICULOS DE LA TIENDA ELEMENTOS DE CADA lista, 
# estos elementos deben ser agregados a la lista correspondiente. debe mostrar los elementos 
# de la tienda con su respectivo precio (for, while)

print("Bienvenido a tienda Shophis")

tienda = []
precio = []
def sumar(articulo + cantidad):
valor_total = sumar

opcion = ""

while opcion != "5":
  print("\n agregar articulos al carrito?")
  print("1. arroz valor $1000")
  print("2. yuca valor $2000 ")
  print("3. maiz valor $3000")
  print("4. papa valor $4000")
  print("5. chontaduro valor $5000")
  
articulo = int(input("Escoja el articulo (1-5): "))
cantidad = int(input ("ingresar cauntos articulos va a comprar: "))

if opcion == "1":
    tienda. append("arroz")
    precio. append("$1000")
    valor_total. 




