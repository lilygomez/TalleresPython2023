import math
 

print("hola")


def menu():
    print("CALCULADORA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potenciacion")
    print("6. Factorial")
    print("7. Raiz Cuadrada")
    print("8. Cambiar Numeros")
    print("9. Salir")
    return int(input("Ingrese una opcion: "))

def obtener_numeros():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    return a, b

def suma():
    a, b = obtener_numeros()
    return a + b

def resta():
    a, b = obtener_numeros()
    return a - b

def multiplicacion():
    a, b = obtener_numeros()
    return a * b

def division():
    a, b = obtener_numeros()
    while b == 0:
        print("No se puede dividir entre 0.")
        b = float(input("Ingrese el segundo numero: "))
    return a / b

def potenciacion():
    a, b = obtener_numeros()
    return a ** b

def factorial():
    a = int(input("Ingrese un numero entero: "))
    return math.factorial(a)

def raiz_cuadrada():
    a = int(input("Ingrese un numero entero positivo: "))
    while a < 0:
        print("El numero debe ser positivo.")
        a = int(input("Ingrese un numero entero positivo: "))
    return math.sqrt(a)

def cambiar_numeros():
    return obtener_numeros()

opcion = 0
while opcion != 9:
    opcion = menu()
    if opcion == 1:
        print("Resultado: ", suma())
    elif opcion == 2:
        print("Resultado: ", resta())
    elif opcion == 3:
        print("Resultado: ", multiplicacion())
    elif opcion == 4:
        print("Resultado: ", division())
    elif opcion == 5:
        print("Resultado: ", potenciacion())
    elif opcion == 6:
        print("Resultado: ", factorial())
    elif opcion == 7:
        print("Resultado: ", raiz_cuadrada())
    elif opcion == 8:
        print("Numeros cambiados.")
    elif opcion == 9:
        print("Adios!")
    else:
        print("Opcion invalida.")