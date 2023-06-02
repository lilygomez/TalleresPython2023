import math

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: división por cero"
    else:
        return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def raiz_cuadrada(num):
    return math.sqrt(num)

def cambiar_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2

print("Bienvenido a la calculadora")

opcion = ""

while opcion != "9":
    print("\n¿Qué operación desea realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz cuadrada")
    print("8. Cambiar números")
    print("9. Salir")
    
    opcion = input("\nIngrese el número correspondiente a la opción: ")
    
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado es:", sumar(num1, num2))
    
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado es:", restar(num1, num2))
       
    
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El resultado es:", multiplicar(num1, num2))
    
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número (distinto de cero): "))
        print("El resultado es:", dividir(num1, num2))
    
    elif opcion == "5":
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
        print("El resultado es:", potencia(num1, num2))
    
    elif opcion == "6":
        num = int(input("Ingrese el número: "))
        print("El factorial es:", factorial(num))
    
    elif opcion == "7":
        num = int(input("Ingrese el número (debe ser entero positivo): "))
        if num < 0:
            print("Error: el número debe ser positivo")
        else:
            print("El resultado es:", raiz_cuadrada(num))
    
    elif opcion == "8":
        num1, num2 = cambiar_numeros()
    
    elif opcion == "9":
        print("¡chao!")
    
    else:
        print("Intente de nuevo.")