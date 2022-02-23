#Ejercicio 8: Análisis de una cadena de caracteres

import tabulate
def descomponer():
    separador=str(input("Introduce el separador que desea utilizar: "))
    cadena=str(input("Introduce un texto para analizar: "))
    ca=cadena.split(separador)
    lista=[]

