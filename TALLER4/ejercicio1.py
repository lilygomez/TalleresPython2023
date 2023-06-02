# 1: Crea una funcion que reciba un numero como parametro y devuelva true si es primo y false si no lo es

def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True
    
num = 67
if es_primo(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")
    
    
    
    
# 2: utilizando la funcion del punto1, realizar otra funcion que reciba del parametro una lista de numeros  y devuelva en una lista solo aquellos que son primos
def listaPrimo(lista):
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = listaPrimo(numeros)
print("Números primos en la lista:", primos)




