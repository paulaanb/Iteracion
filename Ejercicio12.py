#Para hacer este ejercicio debemos primero importar las librerias
from math import sqrt
#Definimos la funcion para calcular los cuadrados perfectos
def calcular_cuadrados(n):
    l = [](#lado del cuadrado)
    s =[]
#Creamos un bucle para generar los numeros enteros desde 0 hasta n lados y otro para os cuadrados perfectos
for i in range (n+1):
    s.append(i)
for m in s:
    if sqrt(m) in s:
        l.append(m)
print("Los cuadrados perfectos resultantes son:".format(n))
#Ultimo bucle dibujar los cuadrados
for x in r:
    print(x)