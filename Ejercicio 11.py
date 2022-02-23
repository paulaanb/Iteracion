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

def iniciar():
    num1=5
    num2=10
    print("Por el algoritmo de Euclides: ".format(mcd_euclides(num1, num2)))
    print("Por sumas y restas: ", mcd_sumas_restas(num1, num2))