#Ejercicio 7: Edición de un número entero
base=int(input("Introduce la base mayor o igual a 2: "))
numero=int(input("Escriba un numero: "))

def edit(numero, base):
    if base > 36:
        print(numero)
    elif base < 2:
        print("Esta base no esta permitida")
    else:
        if numero//base==0:
            print(numero%base)
        else:
            numero = numero//base

edit(numero, base)
