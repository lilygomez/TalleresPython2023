# 3: crea una funcion que , al recibir una lista de numeros, devuelva el que mas se repite y cuantas veces lo hace. si hay mas de una repetida q devuelva cualquiera

def numero_mas_repetido(lista):
    frecuencias = {}
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    numero_mas_repetido = None
    frecuencia_maxima = 0
    for numero, frecuencia in frecuencias.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            numero_mas_repetido = numero
    return numero_mas_repetido, frecuencia_maxima

numeros = [1, 2, 3, 2, 4, 1, 5, 1, 6, 6, 6]
numero_mas_comun, frecuencia = numero_mas_repetido(numeros)
print(f"El número más común es {numero_mas_comun} y se repite {frecuencia} veces.")