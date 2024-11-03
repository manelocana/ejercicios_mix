                    
                                  ###ejercicios remix aprendeconalf###





# region datossimples
# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

'''
def imprimir():
    print('holamundo')
imprimir()
'''



# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable 
# y luego muestre por pantalla el contenido de la variable.

'''
def variable():
    palabra = 'holamundo variable'
    print(palabra)
variable()
'''



# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla 
# la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

'''
def nombre():
    nombre = input(str('cual es tu nombre: '))
    print(f'hola {nombre}, como estas')
nombre()
'''



# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética XX.


'''
'''



# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

'''
def numerohoras():
    horas = float(input('numero de horas trabajadas?: '))
    coste = float(input('a cuanto la hora en €?: '))
    paga = horas * coste
    print(f'con esas horas y ese precio, te sale el dia a {paga}')
numerohoras()
'''



# Ejercicio 6
# Escribir un programa que lea un entero positivo, "nombre entier"
# , introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
# desde 1 hasta "n". 

'''
numero_entero = int(input('dame un numero entero: '))
suma = numero_entero * (numero_entero + 1) / 2
print('la suma de los numero desde 1 hasta ' + str(numero_entero) + ' es ' + str(suma))
'''



# Ejercicio 7
# Escribir un programa que pida al usuario su peso (kg) y estatura (m), 
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase: "tu indice de masa corporal es "imc", 
# donde "imc" es el índice de masa corporal, calculado redondeado con dos decimales.

'''
peso = float(input('cual es tu peso: '))
altura = float(input('cual es tu altura: '))
imc = peso / (altura*altura)
print(f'tu indice de masa corporal es {imc}')
'''



# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros 
# y muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

'''
n = int(input('dame un numero entero: '))
m = int(input('dame otro numero entero: '))
c = n / m
r = n % m
print(f'{n} entre {m}, da un cociente de {c} y un resto de {r}')
'''



# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

'''
cantidad_invertir = float(input('cantidad a invertir: '))
interes_anual = float(input('interes anual: '))
numero_años = int(input('numero de años: '))
capital_obtenido = (cantidad_invertir + interes_anual) * numero_años
print("Capital final: " + str(round(cantidad_invertir * (interes_anual / 100 + 1) ** numero_años, 2)))
'''



# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán 
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

'''
peso_payaso = 112
peso_muñeca = 75
payasos_vendidos = int(input('payasos vendidos: '))
muñecas_vendidas = int(input('muñecas vendidas: '))
peso_total = peso_payaso * payasos_vendidos + peso_muñeca * muñecas_vendidas
print(f'En el último pedido, se vendieron {payasos_vendidos} payasos y {muñecas_vendidas} muñecas. Con un peso total del pedido de {peso_total} gramos')
'''



# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros 
# que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada 
# en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

'''
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))
'''



# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y el coste final total.

'''
precio = 3.49
descuento = 60
barras = int(input('cuantas barras de ayer se vendieron? '))
precio_barra = precio * descuento / 100
print(f'el precio de la barra normal es de: {precio}€,') 
print(f'con un descuento del 60%, el total es: {precio_barra * barras}€')
'''



# ------------------------------------------------------------------------------
# region cadenas
# cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

'''
nombre = str(input('dame un nombre: '))
num = int(input('dame un num: '))
print((nombre + '\n') * num)
'''



# Ejercicio 2
# Escribir un programa que pregunte el nombre completo 
# del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas 
# las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y 
# minúsculas como quiera.

'''
nombre = input('dame tu nombre completo: ')
print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize())
'''



# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca, muestre por pantalla <NOMBRE> 
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y 
# <n> es el número de letras que tienen el nombre.

'''
def nombre():
    nombre = str(input('dime un nombre: '))
    n = len(nombre)
    print(f'el nombre {nombre.upper()} tiene {n} letras')
nombre()
'''



# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este 
# formato y muestre por pantalla el número de teléfono sin el prefijo y 
# la extensión.

'''
numero_telefono = input('dame un numero de telefono completo, prefijo-numero-extension: ')
print('el numero de telf es', numero_telefono[4:-3])
'''



# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en 
# la consola y muestre por pantalla la frase invertida.

'''
def frase_invertida():
    frase = str(input('dime una frase: '))
    print(frase[::-1])
frase_invertida()
'''



# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase 
# en la consola y una vocal, y después muestre por pantalla la misma 
# frase pero con la vocal introducida en mayúscula.

'''
def frase_vocal():
    frase = str(input('dime una frase: '))
    vocal = str(input('dime una vocal: '))
    print(frase.replace(vocal, vocal.upper()))
frase_vocal()
'''



# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario 
# en la consola y muestre por pantalla otro correo electrónico con el 
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.    

'''
correo = input('dame un correo electronico: ')
print(correo[:correo.find('@')] + '@ceu.es')
'''



# Ejercicio 8
# Escribir un programa que pregunte por consola el precio 
# de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.

'''
precio = input("Introduce el precio del producto con dos decimales (separado por punto . ):  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
'''



# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento 
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día 
# o el mes se introduzcan con un solo carácter.

'''
fecha = input('dame tu fecha de naciemiento en formato dd/mm/aaaa : ')
print('dia', fecha[:2])
print('mes', fecha[3:5])
print('año', fecha[6:])
'''

'''
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
'''



# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos 
# de una cesta de la compra, separados por comas, y muestre por 
# pantalla cada uno de los productos en una línea distinta.

'''
lista = input('dame una lista de la compra, separando cada elemento con , :')
print(lista.replace(',', '\n'))
'''



# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, 
# su precio y un número de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido de su precio unitario con 6 dígitos 
# enteros y 2 decimales, el número de unidades con tres dígitos 
# y el coste total con 8 dígitos enteros y 2 decimales.

'''
producto = input('dime un producto: ')
precio = float(input('dime su precio: '))
unidades = int(input('unidades de ese producto: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
'''



# --------------------------------------------------------------------------------------------
# region condicionales
# condicionales
# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla si es mayor de edad o no.

'''
def mayor_de_edad():
    edad = int(input('dime tu edad: '))
    if edad > 18:
        print('eres mayor')
    else:
        print('eres menor de edad')
mayor_de_edad()
'''



# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña 
# en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

'''
def contraseña():
    contraseña = 'hola'.upper()
    caracteres = str(input('dime una contraseña: ')).upper()
    if caracteres == contraseña:
        print('muy bien')
    else:
        print('contraseña incorrecta')
contraseña()
'''



# Ejercicio 3
# Escribir un programa que pida al usuario dos números y 
# muestre por pantalla su división. Si el divisor es cero el 
# programa debe mostrar un error.

'''
def numeros():
    n1 = float(input('dime un numero: '))
    n2 = float(input('dime otro: '))
    if n2 == 0:
        print('no se puede dividir por 0')
    else:
        print(n1/n2)
numeros()
'''



# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar.

'''
def paroimpar():
    num = int(input('dame un numero entero: '))
    if num %2==0:
        print('es par')
    else:
        print('no es par')
paroimpar()
'''



# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y 
# sus ingresos mensuales y muestre por pantalla si el usuario 
# tiene que tributar o no.

'''
edad = int(input('dime tu edad: '))
ingresos = int(input('que ingresos mensuales tienes: '))
if edad < 16 or ingresos < 1000:
    print('no tienes que tributar')
else:
    print('pagas impuestos')
'''



# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. El grupo A esta formado por 
# las mujeres con un nombre anterior a la M y los hombres con 
# un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

'''
nombre = input('dime tu nombre: ')
genero = input('dime tu genero (H o M): ')
if (genero == 'M' and nombre.lower() < 'm') or (genero == 'H' and nombre.lower() > 'n'):
    grupo = 'A'
else:
    grupo = 'B'
print('tu grupo es', grupo)
'''



# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un 
# determinado país son los siguientes:
# Renta 	                Tipo impositivo
# Menos de 10000€ 	            5%
# Entre 10000€ y 20000€ 	    15%
# Entre 20000€ y 35000€ 	    20%
# Entre 35000€ y 60000€ 	    30%
# Más de 60000€ 	            45%
# Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impositivo que le corresponde.

'''
renta = int(input('dime tu renta anual: '))
if renta < 10000:
    impuestos = 5
elif renta > 10000 and renta < 20000:
    impuestos = 15
elif renta > 20000 and renta < 35000:
    impuestos = 20
elif renta > 35000 and renta < 60000:
    impuestos = 30
else:
    renta > 60000
    impuestos = 45
print(f'con una renta de {renta} tienes que pagar el {impuestos} de impuestos')
'''



# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final 
# de cada año. Los puntos que pueden obtener en la evaluación 
# comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores 
# beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre 
# las cifras mencionadas. A continuación se muestra una tabla con los 
# niveles correspondientes a cada puntuación. La cantidad de dinero 
# conseguida en cada nivel es de 2.400€ multiplicada por la puntuación 
# del nivel.
# Nivel 	Puntuación
# Inaceptable 	0.0
# Aceptable 	0.4
# Meritorio 	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel 
# de rendimiento, así como la cantidad de dinero que recibirá el usuario.

'''
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntuacion = float(input('que puntuacion tienes? '))

if puntuacion == inaceptable:
    nivel = 'inaceptable'
elif puntuacion == aceptable:
    nivel = 'aceptable'
elif puntuacion == meritorio:
    nivel = 'meritorio'
else:
    nivel = ''

if nivel == '':
    print('la puntuacion no es valida')
else:
    print('tu nivel de rendimiento es %s' % nivel)
    print('te corresponde cobrar %.2f€' % (puntuacion * bonificacion))
'''



# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos 
# para todas las edades y quiere calcular de forma automática el 
# precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y 
# mostrar el precio de la entrada. Si el cliente es menor de 4 años 
# puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.

'''
edad = int(input('que edad tienes: '))
if edad < 4:
    precio = 0
elif edad > 4 and edad < 18:
    precio = 5
else:
    edad > 18
    precio = 10
print('el precio de la entrada es', precio, '€')
'''



# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no 
# vegetarianas a sus clientes. Los ingredientes para cada 
# tipo de pizza aparecen a continuación.
    # Ingredientes vegetarianos: Pimiento y tofu.
    # Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza 
# vegetariana o no, y en función de su respuesta le muestre un 
# menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe 
# mostrar por pantalla si la pizza elegida es vegetariana o no 
# y todos los ingredientes que lleva.

'''
# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
'''



#-------------------------------------------------------------------------------
# region bucles
# bucles
# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y 
# la muestre por pantalla 10 veces.

'''
def palabra():
    palab = str(input('dime una palabra: '))
    for i in range(10):
        print(palab)
palabra()
'''



# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

'''
def edad():
    edad = int(input('dime una edad: '))
    for i in range(edad):
        print(i+1)
edad()
'''



# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese 
# número separados por comas.

'''
num = int(input('dame un numero entero positivo: '))
for i in range(num):
    if i %2 != 0:
        print(i , end=',')
'''



# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta 
# cero separados por comas.

'''
numero = int(input('dame un numero: '))
    # desde numero hasta 0 (-1), reduciendo 2 en dos
for i in range(numero, -1, -2):
    print(i, end=',')
'''



# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

'''
inversion = float(input('cantidad a invertir: '))
interes = float(input('que interes? '))
años = int(input('durante cuantos años: '))
for i in range(años):
    inversion *= 1 + interes / 100
    print('capital tras', str(i+1), 'años: ', str(round(inversion, 2)))
'''



# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

'''
num = int(input('dame un numero entero: '))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")
'''



# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end='\t')
    print('')
'''



# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

'''
numero = int(input('dame un numero entero: '))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end='')
    print('')
'''



# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres 
# contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.

'''
contraseña = '1234'
dimeelpass = input('dime el pass: ')
while dimeelpass != contraseña:
    dimeelpass = input('escribe la contraseña: ')
    print('no es la contraseña correcta ')
print('hola bienvenido')
'''



# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es un número primo o no

'''
def entero():
    n = int(input('dame un numero mayor a 2: '))
    i = 2
    while n % i != 0:
        i += 1
    if i == n:
        print(str(n) + ' es primo')
    else:
        print(str(n) + ' NO es primo')
entero()
'''



# Ejercicio 11
# escribe un programa que pida al usuario una palabra y luego muesre por panatalla
# una a una de las letras de la palabra introducida empezando por la última.

'''
def unauna():
    palabra = str(input('dame una palabra: '))
    for i in range(len(palabra) -1, -1, -1):
        print(palabra[i])
unauna()
'''



#-----------------------------------------------------------------------------------------------------
# region listas y tuplas
# LISTAS Y TUPLAS
# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica
# quimica, historia y lengua) en una lista y la muestre por pantalla

'''
asignaturas = ['mates', 'fisica', 'quimica', 'historia', 'lengua']
print(asignaturas)
'''



# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
#  Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

'''
asignaturas = ['mates', 'fisica', 'quimica', 'historia', 'lengua']
#print(f'yo estudio {asignaturas[0]}, tambien estudio {asignaturas[1]}, tambien {asignaturas[2]}')
for i in asignaturas:
    print(f'yo estudio {i}')
'''



# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario

'''
asignaturas = ['mates', 'fisica', 'quimica', 'historia', 'lengua']
notas = []
for i in asignaturas:
    nota = input(f'¿que nota has sacado en {i} ?')
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f'en {asignaturas[i]} has sacado {notas[i]}')
'''
    


# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

'''
numeros = []
for i in range(6):
    n = int(input('dame un numero ganador: '))
    numeros.append(n)
numeros.sort()
print(f'los numeros ganadores son {str(numeros)}')
'''



# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[::-1])
'''



# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en 
# cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
#  por pantalla las asignaturas que el usuario tiene que repetir.

'''
asignaturas = ['mates', 'fisica', 'quimica', 'historia', 'lengua']
notas = []
for i in asignaturas:
    nota = int(input(f'la nota de {i} '))
    if nota >= 5:
        notas.append(i)
for i in notas:
    asignaturas.remove(i)
print(f'tienes que repetir {asignaturas}')
'''



# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

'''
import string
abecedario_minusculas = list(string.ascii_lowercase)
print(abecedario_minusculas)
for i in range(len(abecedario_minusculas),1,-1):
    if i %3 == 0:
        abecedario_minusculas.pop(i-1)
print(abecedario_minusculas)
'''



# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

'''
    # aqui convertimos en lista, para usar el metodo reverse(), solo funciona en listas
word = input(str('dame una palabra: '))
reverse_word = word
word = list(word)
reverse_word = list(reverse_word)
reverse_word.reverse()
if word == reverse_word:
    print('es palindromo')
else:
    print('NO es palindromo')
'''

'''
    # aqui hacemos la reversa directamente con [::-1], que funciona con strings
word = input(str('dame una palabra: '))
if word == word[::-1]:
    print('es palindromo')
else: 
    print('NO es palindromo')
'''



# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

'''
palabra = str(input('dame una palabra: '))
vocales = ['a', 'e', 'i', 'o', 'u']
for i in vocales:
    contador = 0
    for letra in palabra:
        if letra == i:
            contador += 1
    print(f'la vocal {i} aparace {contador} veces en la palabra {palabra}')
'''



# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.

'''
    # 
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))
'''

'''
    # usando funciones integradas de python
prices = [50, 75, 46, 22, 80, 65, 8]

min_price = min(prices)
max_price = max(prices)

print("El mínimo es " + str(min_price))
print("El máximo es " + str(max_price))
'''



# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

'''
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
'''



# Ejercicio 12
# Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

'''
    # esto no lo entiendo, copia/pega
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])
'''



# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista 
# y muestre por pantalla su media y desviación típica.

'''
    # esto tampoco lo entiendo, hago copia/pega
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
'''



# ------------------------------------------------------------------------------------------------------------------------
# region diccionarios
# DICCIONARIOS
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

'''
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
'''

'''
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")
'''



# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

'''
nombre = input('dame un nombre: ')
edad = input('dame una edad: ')
direccion= input('dame una direccion: ')
diccionario = {'nombre':nombre, 'edad':edad, 'direccion':direccion}
print(f'el nombre {nombre}, tiene {edad} edad, y vive en la direccion {direccion}')
'''

'''
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
'''



# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número 
# de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Fruta 	Precio
# Plátano 	1.35
# Manzana 	0.80
# Pera 	0.85
# Naranja 	0.70

'''
def fruteria():
    precios_frutas = {'platano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}
    fruta = input('que fruta quiere?: ').lower()
    kg = int(input('cuantos quilos?: '))
    if fruta in precios_frutas:
        print(f'{kg} quilos de {fruta}, valen {precios_frutas[fruta]*kg} €')
    else:
        print('la fruta no se encuentra en la lista')
fruteria()
'''



# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

'''
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 
         7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('dame una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(f'{fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}')
'''



# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
# asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
# asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

'''
creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos_totales = 0
for asignatura, creditos in creditos_asignaturas.items():
    print(f'{asignatura} tiene {creditos} creditos')
    creditos_totales +=  creditos
print('numero total de creditos del curso', creditos_totales)
'''



# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez 
# que se añada un nuevo dato debe imprimirse el contenido del diccionario.

'''
def diccionario():
    persona = {}
    continuar = True
    while continuar:
        clave = input('que dato introduces? ')
        valor = input(clave + ': ')
        persona[clave] = valor
        print(persona)
        continuar = input('quieres añadir mas datos (si/no)? ') == 'si'
diccionario()
'''



# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
# Lista de la compra 	
# Artículo 1 	Precio
# Artículo 2 	Precio
# Artículo 3 	Precio
# … 	…
# Total 	Coste

'''
def lista_compra():
    lista_compra = {}                                                  
    continuar = True
    total = 0
    while continuar:
        clave = input('que articulo quieres comprar? ')
        valor = input(clave + ' precio (€) ? : ')
        lista_compra[clave] = valor
        continuar = input('quieres seguir comprando [si/no] ?  ') == 'si'
        total = total + float(valor)
    for clave, valor in lista_compra.items():
        print(clave, '\t', valor)
    print(f'el precio total de la lista de compra es {total} €')
lista_compra()
'''



#Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
# cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con 
# las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla 
# palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

'''
def traductor_palabras():
    diccionario = {}
    palabras = input('escribe una lista de palabras en formato json: ')
    for i in palabras.split(','):
'''








# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el 
# coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o 
# terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
# el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.










# Ejercicio 10
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un 
# diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente 
# (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, 
# (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la 
# opción elegida el programa tendrá que hacer lo siguiente:

    # Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    # Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    # Preguntar por el NIF del cliente y mostrar sus datos.
    # Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    # Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    # Terminar el programa.









# Ejercicio 11
# El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, 
# donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
# Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos 
# con la información contenida en el directorio.

# "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;
# Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;
# Carmen Sánchez;carmen@mail.com;667677855;15.7"

# Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un 
# cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. 
# Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores 
# la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5},
# '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0},
# '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, 
# '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}











# -----------------------------------------------------------------------------------------------------
#region funciones
# FUNCIONES
# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

'''
def holaamigo():
    print('hola amigo')
holaamigo()
holaamigo()
'''





# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

'''
def nombres():
    nombre = str(input('dime un nombre: '))
    print(f'hola {nombre}')
nombres()
'''




# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''
def factorial(num):
    uno = 1
    for i in range(num):
        uno *= i+1
    return uno
print(factorial(4))
print(factorial(20))
'''


    




# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total 
# de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

'''
def calcular_iva():
    cantidad = int(input('dame una cantidad: '))
    iva = 21
    calculo_iva= (cantidad * iva)/100
    cantidad_total = cantidad + calculo_iva
    print(cantidad_total)
calcular_iva()
'''

'''
def calculo_iva(amount, vat=21):
    return amount + amount*vat/100
print(calculo_iva(123))
'''





# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

'''
def area_circulo():
    import math
    radio = 234
    area_circulo = math.pi * (radio*radio)
    print(area_circulo)
    alturaH = 33
    volumen_cilindro = area_circulo * alturaH
    print(volumen_cilindro)
area_circulo()
'''


'''
def area_circulo(radio):
    import math
    return math.pi * radio**2
def volumen_cilindro(radio, altura):
    return area_circulo(radio)*altura
print(volumen_cilindro(3,5))
'''







# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

'''
def numeros():
    numeros = [12,33,44,23,34,45]
    suma = sum(numeros)
    media = suma / len(numeros)
    print(suma)
    print(media)
numeros()
'''

'''
def numeros(numeros):
        print(sum(numeros) / len(numeros))
numeros(numeros = [12,33,44,23,34,45])
'''






# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.


'''
def cuadrados():
    numeros = [12,33,44,23,34,45]
    lista_numeros = []
    for i in numeros:
        suma =i **2 
        lista_numeros.append(suma)
    print(lista_numeros)
cuadrados()
'''

'''
def cuadrados(numeros):
    lista_numeros = []
    for i in numeros:
        lista_numeros.append(i**2)
    return lista_numeros
print(cuadrados([12,33,44,23,34,45]))
'''







# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
# varianza y desviación típica.


'''
def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
'''









# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

'''
def maximo_comun_divisor(num1, num2):
    rest = 0
    while (num1 > 0):
        rest = num1
        num1 = num2 % num1
        num2 = rest
    return num2
print(maximo_comun_divisor(24,36))

def minimo_comun_multiplo(num1, num2):
    if num1 > num2:
        combi = num1
    else:
        combi = num2 
    while (combi % num1 !=0) or (combi % num2 !=0):
        combi += 1
    return combi
print(minimo_comun_multiplo(24,36))
'''
        
    








# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.









# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que 
# contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y 
# devuelva una tupla con la palabra más repetida y su frecuencia.














#----------------------------------------------------------------------------------------
#region programacion funcional
# Ejercicios de Programación Funcional
# PROGRAMACION FUNCIONAL 
# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta 
# de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los 
# descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.








# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, 
# tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a 
# aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de 
# aplicar la función a esos enteros.








# Ejercicio 3
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de 
# aplicar la función dada a cada uno de los elementos de la lista.









# Ejercicio 4
# Escribir una función que reciba otra función booleana y una lista, y devuelva otra 
# lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.










# Ejercicio 5
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.









# Ejercicio 6
# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.









# Ejercicio 7
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro 
# diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.









# Ejercicio 8
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva 
# otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.










# Ejercicio 9
# Escribir una función que calcule el módulo de un vector.










# Ejercicio 10
# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los 
# inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben 
# incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble 
# se calcula con las siguiente fórmula en función de la zona:
    # Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
    # Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5








# Ejercicio 11
# Escribir una función que reciba una muestra de números y devuelva los valores atípicos, 
# es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación 
# típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.









#------------------------------------------------------------------------------
#region ejercicios ficheros
# EJERCICIOS DE FICHEROS
# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre 
# tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.











# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar 
# de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un 
# mensaje por pantalla informando de ello.











# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar 
# de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla 
# informando de ello.














# Ejercicio 4
# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla 
# el número de palabras que contiene.










# Ejercicio 5
# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea 
# (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.







# Ejercicio 6
# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. 
# El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, 
# añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero 
# de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.









# Ejercicio 7
# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
# Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
# Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
# Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

    # Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
    # Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato 
    # csv con el mínimo, el máximo y la media de dada columna.










# Ejercicio 8
# El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes 
# parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron 
# repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

    # Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
    # donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
    # La lista tiene que estar ordenada por apellidos.

    # Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada 
    # diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de 
    # un 30% mientras que el peso del examen de prácticas es de un 40%.

    # Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, 
    # una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser 
    # mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor 
    # o igual que 5.
