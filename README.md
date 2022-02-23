# Iteracion
El repositorio del trabajo realizado por Paula Naranjo y Carlota Sanchez es [https://github.com/paulaanb/Iteracion]
Los códigos son:

```EJERCICIO 6
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
  print("La media del importe de los movimientos es inferior al mínimo solicitado")'''
  
EJERCICIO 7
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


EJERCICIO 8
#Ejercicio 8: Análisis de una cadena de carácteres

import tabulate
def descomponer():
    separador=str(input("Introduce el separador que desea utilizar: "))
    cadena=str(input("Introduce un texto para analizar: "))
    ca=cadena.split(separador)
    lista=[]

    for i in range(0, len(ca)):
        lista.append(list(ca[i:i+1]))

    table=lista
    headers=["Numero", "Cadena"]
    print(tabulate.tabulate(table, headers, tablefmt = "fancy_grid", showindex = True))
   
 EJERCICIO 9
 #Ejercicio 9: Búsqueda de palabras en un diccionario
import tabulate

def tabla(diccionario):
    table=[]
    for i in range(0, len(diccionario)):
        table.append(list(diccionario[i:i+1]))
    headers=["i", "diccionario", "anterior", "siguiente"]
    print(tabulate.tabulate(table, header, tablefmt="fancy_gird", showindex=True))

def palabra():
    diccionario=["avion", "tren", "auto", "camion"]
    tabla(diccionario)
    print("\n")
    diccionario.sort()
    print("Ordenadas alfabéticamente: ")
    tabla(diccionario)
palabra()

EJERCICIO 10
#Cálculo de los identificadores de las personas de 20 a 30 años
# Selección de los identificadores de las personas por franja de edades.

Entrada
	familias : TABLA[PERSONA]	# El objetivo de la selección
	 edad_min : ENTERO	# El límite de base de la selección
	 edad_max : ENTERO	# El límite superior

Resultado : TABLA[ENTERO][1, 500]

precondición
	familias ≠ NULO
	 edad_min ≠ NULO ; edad_max ≠ NULO

constante
	MIN : ENTERO ← índice_min(familias)
	MAX : ENTERO ← índice_max(familias)

	MIN_EDADES : ENTERO ← índice_min(Resultado)
	MAX_EDADES : ENTERO ← índice_max(Resultado)

	  INFINITO : ENTERO ← ENTERO_MIN
		# El número entero más pequeño utilizable
	HUERFANO : ENTERO ← INFINITO
	  BORRADO : ENTERO ← HUERFANO + 1
	    VACIO : ENTERO ← HUERFANO + 2

variable
	i : ENTERO	
		# Índice de la siguiente celda a observar
	j : ENTERO	
		# Índice siguiente celda de Resultado a inicializar

inicialización
	i ← MIN ; j ← MIN_EDADES
	Resultado[MIN_EDADES] ← VACIO

	afirmación
		i > MIN y j > MIN_EDADES =>
	
realización
	hasta que
		familias[i].identificador = VACIO
		o si no i > MAX

		invariante
			???
		variante de control
			MAX -i + 1

	repetir
		si
			familias[i].identificador ≠ BORRADO
		    y entonces
			edad_min ≤ familias[i].edad ≤ edad_max
		entonces
			Resultado[j] ← familias[i].identificador
			j ← j + 1
		fin si

		i ← i + 1
	fin repetir

postcondición
	# Resultado está VACIO cuando los límites de edades no están en orden
	edad_min > edad_max => Resultado[1] = VACIO

	(∀k ∈ ℤ)(
		índice_min(Resultado) ≤ k ≤ índice_max(Resultado)
		=>
		Resultado[k] es el identificador de una persona de edad
		entre `edad_min' y `edad_max' años
		)
fin edades

#Algoritmo 2: Envejecer un año a las personas registradas

algoritmo envejecer
	# Envejece la población un año.

Entrada
	familias : TABLA[PERSONA]

precondición
	familias ≠ NULO


constante
	MIN : ENTERO ← índice_min(familias)
	MAX : ENTERO ← índice_max(familias)

	  INFINITO : ENTERO ← ENTERO_MIN
		# El número entero más pequeño utilizable
	HUERFANO : ENTERO ← INFINITO
	  BORRADO : ENTERO ← HUERFANO + 1
	    VACIO : ENTERO ← HUERFANO + 2

variable
	i : ENTERO	# Índice de la siguiente celda a tratar

inicialización
	i ← MIN

realización
	hasta que 
		familias[i].identificador = VACIO 
	    o si no
		i > MAX

		invariante
			???
		variante de control
			MAX – i + 1
	repetir
		si
		    familias[i].identificador ≠ BORRADO
		entonces
		    familias[i].edad ← familias[i].edad + 1
		fin si

		i ← i + 1
	fin repetir

postcondición
	Se han incrementado todos los atributos `edad' de las celdas
	ni VACIO ni BORRADO

fin envejecer


#Algoritmo 3: Lista de los identificadores de los huérfanos de padre o de madre.


Entrada
	familias : TABLA[PERSONA]

# Tablas de los identificadores de los huérfanos
Resultado : TABLA[ENTERO][1, 500]

precondición
	familias ≠ NULO

constante
	MIN : ENTERO ← índice_min(familias)
	MAX : ENTERO ← índice_max(familias)
	MIN_HUERFANO : ENTERO ← índice_min(Resultado)
	MAX_HUERFANO : ENTERO ← índice_max(Resultado)

	  INFINITO : ENTERO ← ENTERO_MIN
		# El número entero más pequeño utilizable
	HUERFANO : ENTERO ← INFINITO
	  BORRADO : ENTERO ← HUERFANO + 1
	    VACIO : ENTERO ← HUERFANO + 2

variable
	i : ENTERO	
		# Índice de la siguiente celda a tratar
	j : ENTERO
		# Índice de la siguiente celda de Resultado a
		# inicializar

inicialización
	i ← MIN
	j ← MIN_HUERFANO
	Resultado[j] ← VACIO	# Todavía ningún HUERFANO encontrado

realización
	hasta que 
		familias[i].identificador = VACIO 
	    o si no
		i > MAX

		invariante
			???
		variante de control
			MAX – i + 1
	repetir
		si
		    familias[i].identificador ≠ BORRADO
		  y entonces
		    (
		 	  familias[i].padre = HUERFANO
			o
			  familias[i].madre = HUERFANO
		    )
		entonces
		    Resultado[j] ← familias[i].identificador
		    j ← j + 1
		fin si

		i ← i + 1
	fin repetir

postcondición
	Se han registrado en Resultado los identificadores de todos los
	HUERFANOS de las celdas ni VACIO ni BORRADO 

fin huérfanos

#Algoritmo 4: ¿Cuál es el padre de una persona dada?
# El identificador del padre de `identidad'.

...
hasta que
	familias[i].identificador = VACIO
    o si no
	i > MAX
repetir
	si
		familia[i].identificador ≠ BORRADO
	    y entonces
		(
		  familia[i].identidad.nombre = identidad.nombre
		y
		  familia[i].identidad.apellido = identidad.apellido
		)
	entonces
		Resultado[j, 1] ← familia[i].identificador
		Resultado[j, 2] ← familia[i].padre
		j ← j + 1
	fin si

	i ← i + 1
fin repetir
...
variable
	identidad : IDENTIDAD
	    # La identidad para la que se busca el `padre'
	los_padres : MATRIZ[ENTERO][1, MAX_HOMONIMOS][1,2]
	    # Los identificadores del `padre' de las personas de
	    # identidad 'Jaime MARTIN'. Supone como máximo MAX_HOMONIMOS
	    # en la base para `identidad'.

realización
	identidad.nombre ← 'Jaime'
	identidad.apellido ← 'MARTIN'
	los_padres ← padre(familias, identidad)

	{Hacer algo con `los_padres'}

#Algoritmo unos_hermanos
# Calcula los hermanos de padre `padre' de los hermanos de `identificador'

Entrada
	familias : TABLA[PERSONA]
	identificador : ENTERO # Persona para la que queremos hermanos
	       padre : ENTERO # Identificador del padre de los hermanos

Resultado : TABLA[ENTERO] # Identificadores miembros de los hermanos

constante
	MAX : ENTERO ← índice_max(familias)

variable
	persona : ENTERO	 # Un identificador de persona
	i : ENTERO	# siguiente hermano/a a registrar

inicialización
	Resultado[1] ← identificador
	i ← 1		# Índice del último hermano identificado
	j ← índice_min(familias)

realización
	persona ← familias[j].identificador
		# siguiente persona a observar en `familias'

	hasta que persona = VACIO o si no j > MAX repetir
		invariante
			???
		variante de control
			MAX – i + 1

		si
			persona ≠ BORRADO
		    y
			familias[j].padre = padre
		entonces
			i ← i + 1
			Resultado[i] ← persona
		fin si
	
		j ← j + 1
	fin repetir

	Resultado[i + 1] ← VACIO	# Marca el final de los hermanos

postcondición
	

fin unos_hermanos

EJERCICIO 11
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
  
  
EJERCICIO 12
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
print("Los cuadrados perfectos resultantes hasta {} son:".format(n))
#Ultimo bucle dibujar los cuadrados
for x in r:
    print(x)

if __name__ == "__main__":

  n = int(input("Por favor, introduzca un numero entero: "))
  calcular_cuadrados(n)
