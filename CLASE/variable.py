Num = 23
num1 =1.25
valor = "hola"
v1 = True
#print(type(v1))
#operaciones basicas
dato1 = 4
dato2 = 2
division = dato1 // dato2
#prse puede usar tambienint("el resultado de la operacion es:",potenciacion)
"""Se puede usar tambien asi:"""
#print("El resultado es {0}".format (division))
"""tambien se puede llamar usando %d para entero y %F para decial ejemplo:"""
#print("el resultado es %f" % (division))
#todo dato que ingresa como un imput es tipo string
#dato1 = int(input("ingrese un numero:"))
#dato2 = int(input("ingrese un numero:"))
#division = dato1 // dato2
#print ("el resultado es %d" % (division))

#metodos lower(), upper(),title
texto = "hola grupo!!!"
#print (texto.upper())
#print (texto.title())
#print (texto.lower())

"""calcular el precio de las horas de parqueo teniendo en cuenta la hora de llegada, la hora de salida, 
el precio por hora, precio a pagar,
* definir variables de forma correcta
*Mostrar en pantalla el valor a pagar"""

"""precio_hora: 1000
horaS: int(input("ingrese la hora de salida:"))
horaIn: int(input("ingrese la hora de llegada:"))
tiempo_total: (horaS - horaIn)* precio_hora
print ("el total a pagar: ", tiempo_total)"""

"""ejercicio2:
realizar un programa donde el usuario ingrese dos numeros para dividir y  
muestre en pantalla un mensaje que indique cual es el dividendo, el divisor, conciente y el residuo """

#dividendo = int(input("ingrese un numero:"))
#divisor = int(input("ingrese un numero:"))
#cociente = dividendo // divisor
#print ("el dividendo es: ", dividendo ,"\n" "el divisor es:", divisor,"\n" "el cociente es:", cociente ,"\n"
       #"el residuo es: ",dividendo%divisor)
#print(f"\tcociente {dividendo//divisor}\n\tdivisor: {divisor}\n\tdividendo: {dividendo}\n\treiduo: {dividendo%divisor}")

"""CONDICIONAL IF
nota: la condicion que se da es de tipo booleano """
#ingresar edad del usuario, muestre si es mayor de edad.

"""nombre = (input ("ingresar nombre: "))
edad = int(input ("ingresar edad: "))

if edad >= 18:
    print(nombre, "Eres mayor de edad ")
    
else:
    print(nombre, "Eres menor de edad ")"""
    
#elif (es el si no si , la condicion:
#                        intruccion)

"""num1 = (input ("ingresar numero: "))
num2 = (input ("ingresar numero: "))

if num1>num2:
    print(num1, "es mayor")
elif num1<num2:
    print(num2, "es mayor")
else:
    print(f"{num1} y {num2} son iguales")"""
     
#CONDICIONAL Y OPERADORES lOGICOS: AND , OR
#PEDIR A USUARIO LA EDAD Y A QUE GRUPO QUIERE PERTENECER(ADULTO O INFANTIL), 
# SI EL USAURIO TIENEN 18 AÑOS O MAS Y ESCOGE ADULTO MUESTRE "PUEDE INGRESAR AL GRUPO",
# DE LO CONTRARIO "EXCEDE LA EDAD PARA INGRESAR AL GRUPO ",SI TIENE MENOS DE 18 Y ESCOGE INFANTE MUESTRE 
# "PUEDE INGRESAR AL GRUPO", DE LO CONTRATIO "NO PUEDE INGRESAR". SI ESCOGE UNA OPCION DIFERENTE
# DEBE SALIR OPCION NO VALIDA

"""edad = (input ("Dime tu edad: "))
ingreseGrupo = (input ("A que grupo quieres pertenecer ADULTO 1 o NIÑO"), grupo1 )
grupo1 = "adulto"
grupo2 = "infantil"

if edad >= 18 and grupo1 :
    print ("debes pagar impuesto")

Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no."""


edad = (input ("ingresa tu edad: "))
ingresos = (input ("ingresa tu ingresos mensuales: "))

if edad >= 18 and ingresos >= 2500000 :
    print ("debes pagar impuesto")
else:
    print ("no pagas impuesto")

