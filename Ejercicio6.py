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

operacion = input("¿Desea hacer otra operación más (a elegir entre: consultar saldo,retirar dinero y abonar?")
if operacion == "no":
    print("Gracias por confiar en nuestro banco.")
if operacion == "abonar":
    introducir_dinero= float(input("Introduzca el dinero que desee ingresar en su cuenta: "))
    saldo = (saldo + introducir_dinero).add(operacion)
    print("Su saldo es de " , saldo , "€")
if operacion == "consultar":
    print("El saldo de su cuenta es " , saldo , "€")
if operacion == "retirar":
    retirar_dinero= float(input("Introduzca el dinero que desee retirar de su cuenta: "))
    saldo = (saldo - retirar_dinero).add(operacion)
    if saldo >= 0:
        print("Al retirar la cantidad de " , retirar_dinero , " su saldo ha disminuido a un total de " , saldo , "€")
    if saldo < 0:
        saldo = saldo * (-1)
        print("Al retirar la cantidad de " , retirar_dinero ,". Su saldo ha entrado en numeros rojos, por lo que debe una cantidad de  " , saldo , "€")

suma= 10
if sum(operacion) > suma: 
  print("La media del importe de los movimientos es superior al mínimo solicitado")
else:
  print("La media del importe de los movimientos es inferior al mínimo solicitado")