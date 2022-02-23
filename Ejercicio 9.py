#Ejercicio 9: Búsqueda de palabras en un diccionario
import tabulate

def tabla(diccionario):
    table=[]
    for i in range(0, len(diccionario)):
        table.append(list(diccionario[i:i+1]))
    headders=["i", "diccionario", "anterior", "siguiente"]
    print(tabulate.tabulate(table, tablefmt="fancy_gird", showindex=True))

def palabra():
    diccionario=["avion", "tren", "auto", "camion"]
    tabla(diccionario)
    print("\n")
    diccionario.sort()
    print("Ordenadas alfabéticamente: ")
    tabla(diccionario)
palabra()