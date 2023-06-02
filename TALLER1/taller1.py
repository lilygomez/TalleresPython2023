#punto 1
"""edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingresos >= 2500000:
    print("Debe tributar impuestos.")
else:
    print("No está obligado a tributar impuestos.")"""
    
    #punto 2

"""desarrolloSf = float(input("Ingrese la nota de Desarrollo de Software: "))
matematicas = float(input("Ingrese la nota de Matemáticas: "))
logicaP = float(input("Ingrese la nota de Lógica de Programación: "))

# Calculamos el promedio
promedio = (desarrolloSf  + matematicas + logicaP) / 3

# promedio es mayor o igual que 3.0
if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")"""
    
    #punto 1 condicional elif
    
# Pedimos al usuario que ingrese los 4 números
"""num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

# Comprobamos si algún número se repite
if num1 == num2 or num1 == num3 or num1 == num4:
    print("El número", num1, "se repite")
elif num2 == num3 or num2 == num4:
    print("El número", num2, "se repite")
elif num3 == num4:
    print("El número", num3, "se repite")

# Comprobamos si todos los números son iguales
elif num1 == num2 == num3 == num4:
    print("Todos los números son iguales")

# Comprobamos si todos los números son diferentes
else:
    print("Todos los números son diferentes")"""
    
    #punto 2 condicional elif

# Mostramos el menú de colores primarios
print("1. Amarillo")
print("2. Azul")
print("3. Rojo")
print("4. Blanco")
print("5. Negro")

# escoja 2 colores
color1 = int(input("Escoja el primer color (1-5): "))
color2 = int(input("Escoja el segundo color (1-5): "))

#combinaciones de colores
if color1 == 1 and color2 == 2 or color1 == 2 and color2 == 1:
    print("Combinación: Verde")
elif color1 == 1 and color2 == 3 or color1 == 3 and color2 == 1:
    print("Combinación: Naranja")
elif color1 == 2 and color2 == 3 or color1 == 3 and color2 == 2:
    print("Combinación: Morado")
elif color1 == 1 and color2 == 4 or color1 == 4 and color2 == 1:
    print("Combinación: Amarillo claro")
elif color1 == 2 and color2 == 4 or color1 == 4 and color2 == 2:
    print("Combinación: Celeste")
elif color1 == 3 and color2 == 4 or color1 == 4 and color2 == 3:
    print("Combinación: Rosado")
elif color1 == 1 and color2 == 5 or color1 == 5 and color2 == 1:
    print("Combinación: Gris claro")
elif color1 == 2 and color2 == 5 or color1 == 5 and color2 == 2:
    print("Combinación: Gris azulado")