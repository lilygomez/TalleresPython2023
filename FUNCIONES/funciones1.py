# FUNCIONES: Ahorra lineas de codigo, reutiliza codigo, divide el programa en pequeñas tareas
# para declarar una funcion en py se utiliza la palabra recervada y para llamar la funcion se invoca y se pasa los argumentos 
"""def NombreFuncion(parametro!, parametro2...):
conjunto de instrucciones
NomreFuncion(Argumento1, Argumento2.....)
"""


#ejemplo funcion sin parametros:

"""def DerechosHumanos():
 print("Derecho a la vida \nDerecho a la libre exprecion\nDerecho a la liberta\nDerecho a la libre exprecion \nDerecho de la personalidad ")
DerechosHumanos()
def MayoresdeEdad():
    print("Derecho a morir dignamente\nDerecho al trabajo\nDerecho a tener una vejez digna\nDerecho a votar")
    
#FUNCION CON PARAMETROS

#ejemplo: declarar una funcion que muestre los derechos humanos y los derechos de los mayores de edad, si la edad es mayor o igual de 18,
# de lo contratio solo muestre lo derechos humanos 

Nota: son parametros cuando se llaman y argumentos cuando se les da valor

def Derechos(Nombre, edad):
    print(f"{Nombre} tus derechos son:"),
    if edad >= 18:
        DerechosHumanos()
        MayoresdeEdad()
    else:
        DerechosHumanos()
#edad = int(input("ingrese su edad: "))
Derechos("Karina", edad)
    
#nota: simpre va primero los argumentos obligatorios y luego los parametros que se les da un valor"""

#Segundo ejemplo:
#funcion de division: divisor es 0 debe arrojar un mensaje de error, de lo contratio muestre el resultado 

"""def Division(Dividendo, Divisor):
    if Divisor ==0:
        print("no existe la division por cero")
    else:
        print (f" El cociente es: { Dividendo // Divisor} ")
Division(20, 5)


#otra forma:

Divisor = 3
def Division(Dividendo, Divisor):
    if Divisor ==0:
        print("no existe la division por cero")
    else:
        print (f" El cociente es: { Dividendo // Divisor} ")
Division(20, Divisor)
print(Divisor)"""


# Funcion que compare dos números y muestre cual de ellos es el mayor, ademas debe verificar que los datos sean enteros decimales:

        
"""def Numeros(num1, num2):
    if (type(num1)== int) or (type(num1)==float) and (type(num2)== int) or (type(num2)==float):
        if  num1 > num2:
            print(f"el numero {num1}, es mayor que {num2} ")
    else:
        print(f"el numero {num2}, es mayor que {num1}")
        
Numeros(5, 4.9)"""


#Ejercicios

# 1: Crea una funcion que reciba un numero como parametro y devuelva true si es primo y false si no lo es
# 2: utilizando la funcion del punto1, realizar otra funcion que reciba del parametro una lista de numeros  y devuelva en una lista solo aquellos que son primos
# 3: crea una funcion que , al recibir una lista de numeros, devuelva el que mas se repite y cuantas veces lo hace. si hay mas de una repetida q devuelva cualquiera


# Ejercicio 1:

def numPrimo (num):
    if num == 1 or num == 0:
        print("false", "el numero ingresado no es primo")
    elif num == 2:
        print("true" , "el numero ingresado es primo")
    elif num >2:
        for divisor in range (2, num):
            if num % divisor == 0:
                return False
            elif num % divisor != 0 and divisor == -1:
                return True
            
numPrimo (1)
       
    
