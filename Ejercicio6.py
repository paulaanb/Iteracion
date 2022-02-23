#Historial de una cuenta corriente
#El código para resolver lo que te pide el ejercicio (Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente) es el siguiente:

cuenta_corriente = input("¿Desea abrir una cuenta corriente en el banco? (si/no): ")

if cuenta_corriente == "no":
    print("Usted ha elegido no abrir una cuenta corriente en nuestro banco.")
if cuenta_corriente == "si":
    saldo_disponible = 0
    print("Debe abonar dinero en su nueva cuenta corriente.")
    dinero_ingresado= int(input("Pr favor, inserte el dinero deseado a abonar:"))
    saldo = (dinero_ingresado).add(operacion)
