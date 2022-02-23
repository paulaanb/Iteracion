#Ejercicio 11: mcd de dos números enteros

def mcd_euclides(a, b):
    while b != 0:
        #Utilizo propiedad: mcd(a, b)=mcd(a-b, b)
        aux=b
        b=a%b
        a=aux
    return a

def mcd_sumas_restas(a, b):
    while b!=0:
        aux=b-a
        b=aux
        a=aux
    return a