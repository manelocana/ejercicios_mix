                    
                                  ###ejercicios remix aprendeconalf###





# region datossimples
#Ejercicio 1
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

'''
def hola():
    print('hola mundo')
hola()
'''


#Ejercicio 2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable 
#y luego muestre por pantalla el contenido de la variable.

'''
def hola():
    hola = 'hola mundo'
    print(hola)
hola()
'''


#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola 
#y después de que el usuario lo introduzca muestre por pantalla 
#la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

'''
def hola_nombre():
    nombre = input('dime tu nombre: ')
    print(f'hola {nombre}')
hola_nombre()
'''


#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética XX.

'''
'''


#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

'''
def precio():
    horas = float(input('horas trabajadas: '))
    coste = float(input('coste por hora: '))
    paga = horas * coste
    print(f'le corresponde {paga} €')
    return paga
precio()
'''


#Ejercicio 6
#Escribir un programa que lea un entero positivo, "nombre entier"
#, introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
#desde 1 hasta "n". 

'''
def entero_positivo():
    numero = int(input('dame un numero entero: '))
    cuenta = 0
    for i in range(numero):
        cuenta += i
    print(f'la suma de numeros desde 1 hasta {numero} es {cuenta}')
entero_positivo()
'''


#Ejercicio 7
#Escribir un programa que pida al usuario su peso (kg) y estatura (m), 
#calcule el índice de masa corporal y lo almacene en una variable,
#y muestre por pantalla la frase: "tu indice de masa corporal es "imc", 
#donde "imc" es el índice de masa corporal, calculado redondeado con dos decimales.

'''
# imc = kg/m2
def calcular_imc():
    peso = float(input('cual es tu peso?: '))
    altura = float(input('cual es tu altura?: '))
    imc = peso / (altura*altura)
    print(f'tu indice de masa corporal es {imc:.2f}')
calcular_imc()
'''

'''
def calcular_imc(peso, altura):
    return peso/(altura **2)
peso = float(input('peso en kg: '))
altura = float(input('que altura en m: '))
imc = calcular_imc(peso, altura)
print(f'tu imc es {imc:.2f}')
'''


#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros 
#y muestre por pantalla la <n> entre <m> da un cociente <c> 
#y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
#y <c> y <r> son el cociente y el resto de la división entera respectivamente.

'''
def cociente():
    n = int(input('numero 1: '))
    m = int(input('numero 2: '))
    c = n / m
    r = n % m
    print(f'{n} entre {m}, da un cociente de {c:.2f} y un resto de {r}')
cociente()
'''


#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

'''
def inversiones():
    inversion = float(input('cuanto quieres invertir: '))
    interes = float(input('a que interes anual: '))
    años = int(input('numero de años de la inversion?: '))
    calculo = ((inversion * interes)/100)*años
    #print(f'el capital obtenido es: {((inversion * interes)/100)*años}')
    print(f'el capital obtenido es {calculo} €')
inversiones()
'''


#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán 
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

'''
def juguetes():
    payaso = 112
    muñeca = 75
    cuantos_payasos = int(input('cuantos payasos? '))
    cuantas_muñecas = int(input('cuantas muñecas? '))
    peso = payaso * cuantos_payasos + muñeca * cuantas_muñecas
    print(f'el peso total del paquete sera: {peso} g.')
juguetes()
'''


#Ejercicio 11
#Imagina que acabas de abrir una nueva cuenta de ahorros 
# que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada 
# en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

'''
def interes_compuesto(inversion, interes, años):
    interes /= 100
    invertido = inversion
    for i in range(1, años+1):
        invertido *= 1+interes
        print(f'tras el año {i} tienes: {round(invertido, 2)} €')
interes_compuesto(100, 4, 20) 
'''


# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y el coste final total.

'''
def panaderia(precio, descuento, pan_vendido):
    precio_pan = precio 
    descuento /= 100
    venta = pan_vendido * precio_pan
    calculo = venta * (1 - descuento)
    return f'el precio total del pan con descuento es: {calculo:.2f} €'
print(panaderia(3.49, 60, 20))
'''


#region cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

'''
def repeticion():
    nombre = input('dame un nombre: ')
    numero = int(input('ahora dame un numero: '))
    print((nombre + '\n') * numero)
repeticion()
'''


#Ejercicio 2
#Escribir un programa que pregunte el nombre completo 
# del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas 
# las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y 
# minúsculas como quiera.

'''
def nombre_completo():
    nombre = input('dame un nombre completo: ')
    print(nombre.lower())
    print(nombre.capitalize())
    print(nombre.upper())
nombre_completo()
'''
    

#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca, muestre por pantalla <NOMBRE> 
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y 
# <n> es el número de letras que tienen el nombre.

'''
def nombre_usuario():
    nombre = input('dame un nombre: ')
    print(f'el nombre {nombre.upper()} tiene {len(nombre)} letras')
nombre_usuario()
'''


#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este 
# formato y muestre por pantalla el número de teléfono sin el prefijo y 
# la extensión.

'''
def prefijos():
    numero = input('dame un numero de telf con este formato: xx-xxxxxxxxx-xx ')
    print(numero[3:-3])
prefijos()
'''


#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en 
# la consola y muestre por pantalla la frase invertida.

'''
def frase_invertida():
    frase  = input('dime una frase, que te la invierto: ')
    print(frase[::-1])
frase_invertida()
'''


#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase 
# en la consola y una vocal, y después muestre por pantalla la misma 
# frase pero con la vocal introducida en mayúscula.

'''
def vocal_mayus():
    frase = input('dame una frase: ')
    vocal = input('ahora una vocal: ')
    print(frase.replace(vocal, vocal.upper()))
vocal_mayus()
'''


#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario 
# en la consola y muestre por pantalla otro correo electrónico con el 
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.    

'''
def correo():
    correo = input('dame un correo electronico: ')
    print(correo[:correo.find('@')] + '@ceu.es')
correo()
'''


#Ejercicio 8
#Escribir un programa que pregunte por consola el precio 
# de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.

'''
def precio():
    precio = input('dame un precio con dos decimales (separado por punto): ')
    print(precio[:precio.find('.')], 'euros y', precio[precio.find('.') +1 :], 'centimos')
precio()
'''


#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento 
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día 
# o el mes se introduzcan con un solo carácter.

'''
def nacimiento():
    fecha = input('fecha de nacimiento (dd/mm/aaaa): ')
    print('dia:', fecha[:2], 'mes:', fecha[3:5], 'año:', fecha[6:])
nacimiento()
'''


#Ejercicio 10
#Escribir un programa que pregunte por consola por los productos 
# de una cesta de la compra, separados por comas, y muestre por 
# pantalla cada uno de los productos en una línea distinta.

'''
def cesta_compra():
    compra = input('dime la lista de la compra: ')
    print(compra.replace(',', '\n'))
cesta_compra()
'''


#Ejercicio 11
#Escribir un programa que pregunte el nombre del un producto, 
# su precio y un número de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido de su precio unitario con 6 dígitos 
# enteros y 2 decimales, el número de unidades con tres dígitos 
# y el coste total con 8 dígitos enteros y 2 decimales.

""" 
def productos():
    producto = input('producto: ')
    precio = float(input('precio: '))
    unidades = int(input('unidades: '))
    coste = precio * unidades
    print(f'el producto', producto, 'tiene un precio de', precio, 'numero de unidades:', unidades)
    print(f'el precio total del pedido es', coste, '€')
productos()
 """


#region condicionales
#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y 
#muestre por pantalla si es mayor de edad o no.

'''
def edad():
    edad = int(input('dime tu edad: '))
    if edad < 18:
        print('eres menor')
    else:
        print('eres mayor')
edad()
'''
'''
# aqui lo mismo en shorthand (en una linea)
edad = int(input('dime tu edad: '))
print('eres menor' if edad<18 else 'eres mayor')
'''


#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña 
# en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

'''
def contraseña():
    contraseña = ''
    intentos = 0
    contraseña_original = '1234'
    while intentos < 5:
        contraseña = input('dime la contraseña (5 intentos): ')
        if contraseña == contraseña_original:
            print('bienvenido, contraseña correcta')
            break
        else: 
            print('contraseña incorrecta, vuelve a intentarlo')
            intentos += 1
            print(f'{intentos} intento')
contraseña()
'''


#Ejercicio 3
#Escribir un programa que pida al usuario dos números y 
# muestre por pantalla su división. Si el divisor es cero el 
# programa debe mostrar un error.

'''
def division():
    n1 = int(input('dame el primer numero: '))
    n2 = int(input('dame el segundo numero: '))
    division = n1 / n2
    if division == 0:
        print('error')
    else:
        print(division)
division()    
'''


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar.

'''
def par():
    num = int(input('dame un numero entero: '))
    if num %2 == 0:
        print('es par')
    else: 
        print('impar')
par()
'''


#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y 
# sus ingresos mensuales y muestre por pantalla si el usuario 
# tiene que tributar o no.

'''
def impuesto():
    edad = int(input('dame tu edad: '))
    ingresos = int(input('dime tus ingresos mensuales: '))
    if edad >= 16 or ingresos >= 1000:
        print('tienes que tributar')
    else: 
        print('no tributas')
impuesto()
'''


#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. El grupo A esta formado por 
# las mujeres con un nombre anterior a la M y los hombres con 
# un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

'''
def curso():
    nombre = str(input('dame tu nombre: '))
    sexo = str(input('sexo, hombre/mujer: (H/M)'))
    if nombre < 'm' and sexo == 'h':
        print('perteneces al grupo_A')
    else: 
        print('eres del grupo_B')
curso()
'''


#Ejercicio 7
#Los tramos impositivos para la declaración de la renta en un 
# determinado país son los siguientes:
#Renta 	Tipo impositivo
#Menos de 10000€ 	5%
#Entre 10000€ y 20000€ 	15%
#Entre 20000€ y 35000€ 	20%
#Entre 35000€ y 60000€ 	30%
#Más de 60000€ 	45%
#Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impositivo que le corresponde.

'''
def renta():
    renta = int(input('cual es su renta anual: '))
    if renta < 10000:
        print('se te impone el 5%')
    elif renta > 10000 and renta < 20000:
        print('tributas el 15%')
    elif renta > 20000 and renta < 35000:
        print('tributas el 20%')
    elif renta > 35000 and renta < 60000:
        print('tributas el 30%')
    else:
        print('pagas el 45%')
renta()
'''


#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final 
# de cada año. Los puntos que pueden obtener en la evaluación 
# comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores 
# beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre 
# las cifras mencionadas. A continuación se muestra una tabla con los 
# niveles correspondientes a cada puntuación. La cantidad de dinero 
# conseguida en cada nivel es de 2.400€ multiplicada por la puntuación 
# del nivel.
#Nivel 	Puntuación
#Inaceptable 	0.0
#Aceptable 	0.4
#Meritorio 	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel 
# de rendimiento, así como la cantidad de dinero que recibirá el usuario.

'''
def puntuaciones():
    puntos = float(input('que puntuacion obtuviste: '))
    if puntos == 0.0:
        print('nivel inaceptable')
    elif puntos == 0.4:
        print('nivel aceptable')
    elif puntos >= 0.6:
        print('nivel meritorio!')
    else:
        print('puntuacion no valida')
    print(f'con una puntuacion de {puntos} recibes {2400 * puntos} €')
puntuaciones()
'''


#Ejercicio 9
#Escribir un programa para una empresa que tiene salas de juegos 
# para todas las edades y quiere calcular de forma automática el 
# precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y 
# mostrar el precio de la entrada. Si el cliente es menor de 4 años 
# puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.

'''
def entrada():
    edad = int(input('que edad tienes: '))
    if edad < 4:
        print('entrada gratis')
    elif edad > 4 and edad < 18:
        print('pagas 5€')
    else:
        print('pagas 10€')
entrada()

def entrada2():
    edad = int(input('que edad tienes: '))
    if edad < 4:
        precio = 0
    elif edad > 4 and edad < 18:
        precio = 5
    else: 
        precio = 10
    print(f'con {edad} años, pagas {precio}€')
entrada2()
'''


#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no 
# vegetarianas a sus clientes. Los ingredientes para cada 
# tipo de pizza aparecen a continuación.

    #Ingredientes vegetarianos: Pimiento y tofu.
    #Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza 
# vegetariana o no, y en función de su respuesta le muestre un 
# menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe 
# mostrar por pantalla si la pizza elegida es vegetariana o no 
# y todos los ingredientes que lleva.

'''
# respuesta copiada

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


#region bucles
#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y 
#la muestre por pantalla 10 veces.

'''
def bucle_10():
    palabra = str(input('dame una palabra: '))
    contador = 0
    while contador < 10:
        print(palabra)
        contador += 1
bucle_10()
'''


#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

'''
def edad():
    edad = int(input('dime tu edad: '))
    for i in range(edad):
        print(i+1)
edad()
'''


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese 
# número separados por comas.

'''
def enteroposi():
    try:
        num = int(input('dame un entero positivo: '))
    except ValueError:
        print('te dije un numero positivo perro')
    else:
        for i in range(num+1):
            if i %2 != 0:
                print(i, end=',')
enteroposi()
'''


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta 
# cero separados por comas.

'''
def cuenta_atras():
    num = int(input('dame un entero positivo: '))
    lista = []
    for i in range(num+1):
        lista.append(i)
    print(lista[::-1])

    for i in range(num, 1, -1):
        print(i-2, end=',')
cuenta_atras()
'''


#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

'''
def inversion():
    invertir = float(input('cuanto inviertes? '))
    interes = float(input('a que interes? '))
    años = int(input('cuantos años? '))
    for i in range(años):
        invertir *= 1 + interes / 100
        print('capital tras', str(i+1), 'años: ', str(round(invertir, 2)))
inversion()
'''


#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

'''
def triangulo():
    numero = int(input('dame un numero entero: '))
    for i in range(numero): 
        for j in range(i+1):
            print('*', end='')
        print('')        
triangulo()
'''


#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

'''
def tabla():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end='\t')
        print('')
tabla()
'''


#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

'''
numero = int(input('dame un numero entero: '))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end='')
    print('')
'''


#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres 
# contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.

'''
contraseña = '1234'
contraseña_usuario = input('dame una contraseña: ')
while contraseña != contraseña_usuario:
    contraseña_usuario = input('vuelve a intentarlo: ')
print('contraseña correcta')
'''


#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es un número primo o no

'''
def entero():
    numero = int(input('dame un numero mayor a 2: '))
    if numero <= 1:
        print(f'{numero} No es primo, el numero debe ser mayor a 1')
    i = 2
    while numero % i != 0:
        i += 1
    if i == numero:
        print(f'{numero} es primo')
    else:
        print(f'{numero} NO es primo')
entero()
'''

'''
#lo hacemos con la raiz cuadrada:   int(numero**0.5) + 1
numero = int(input('dame un numero entero mayor a 1: '))
if numero <= 1:
    print(f'{numero} no es primo, tiene q ser mayor a 1 idiota')
else:
    num_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            num_primo = False
            break  
    if num_primo:
        print(f'{numero} es primo.')
    else:
        print(f'{numero} no es primo, ya que es divisible por {i}')
'''


#Ejercicio 11
#escribe un programa que pida al usuario una palabra y luego muesre por panatalla
# una a una de las letras de la palabra introducida empezando por la última.

'''
# dos maneras de hacerlo
palabra = input('dame una palabra: ')
palabra_invertida = palabra[::-1]
for i in range(len(palabra) -1, -1, -1,):
        print(palabra[i], end='')
print(f'\n{palabra_invertida}')
'''


#region listas y tuplas
#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica
#quimica, historia y lengua) en una lista y la muestre por pantalla

'''
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
print(asignaturas)
'''


#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
#  Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

'''
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
for i in asignaturas:
    print(f' yo estudio {i}', end=',')
print('')
'''


#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

'''
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
notas = []
for i in asignaturas:
    nota = int(input(f'que nota has sacado en {i}: '))
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f'en {asignaturas[i]} has sacado {notas[i]}',  end=',')
'''


#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

'''
contador = 0
listado = []
while contador < 5:
    numeros = int(input('dame los numermos de la loteria: '))
    listado.append(numeros)
    contador += 1
print(sorted(listado))
'''

 
#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

'''
numeros = []
for i in range(1,11):
    numeros.append(i)
print(numeros[::-1])
'''


#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en 
# cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
#  por pantalla las asignaturas que el usuario tiene que repetir.

'''
suspenso = []
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
for i in asignaturas:
    nota = int(input(f'que nota has sacado en {i}: '))
    if nota < 5:
        suspenso.append(i)
print(f'tienes que repetir {suspenso}')
'''


#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

'''
#con ayuda para lo del string
import string
abecedario = list(string.ascii_lowercase)
for i in range(len(abecedario),1,-1):
    if i %3 == 0:
        abecedario.pop(i-1)
print(abecedario)
'''


#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

'''
palabra = input('dame una palabra a ver si es palindromo: ')
print(palabra[::-1])
if palabra == palabra[::-1]:
    print('es palindromo')
else:
    print('NO es palindromo')
'''


#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

'''
vocales = ['a','e','i','o','u']
palabra = input('dame una palabra: ')
for i in vocales:
    contador = 0
    for letra in palabra:
        if letra == i:
            contador += 1
    print(f'la vocal {i} aparace {contador} veces en la palabra {palabra}')
'''


#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.

'''
precios = (50, 75, 46, 22, 80, 65, 8)
precio_minimo = min(precios)
precio_maximo = max(precios)
print(f'el numero mas grande es: {precio_maximo}')
print(f'el mas pequeño: {precio_minimo}')
new_precio = sorted(precios)
print(new_precio[0])
print(new_precio[-1])
'''


#Ejercicio 11
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

'''
uuhhhh
'''


#Ejercicio 12
#Escribir un programa que almacene las matrices
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.










#Ejercicio 13
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista 
# y muestre por pantalla su media y desviación típica.







#region diccionarios
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

'''
monedas = {'euro':'€', 'dollar':'D', 'yen':'Y'}
moneda = input('dime una moneda (euro, dollar o yen): ')
print(monedas.get(moneda.lower(), 'escribe bien, elige una moneda de la lista'))
''' 

'''
monedas = {'euro':'€', 'dollar':'D', 'yen':'Y'}
moneda = input('dime una moneda (euro, dollar o yen): ')
if moneda in monedas:
    print(monedas[moneda.lower()])
else:
    print('esa moneda no esta en la lista')
'''


# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

'''
nombre = input('dame tu nombre: ')
edad = int(input('que edad tienes: '))
direccion = input('donde vives: ')
telefono = int(input('numero telefono: '))
datos = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}
print(f'{nombre} tiene {edad} años, vive en {direccion} y su numero de telefono es {telefono}')
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
frutas = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}
fruta = input('que fruta quiere: ').lower()
kilos = float(input('cuantos quilos: '))
if fruta in frutas:
    precio = frutas[fruta] * kilos
print(f'{kilos} kg de {fruta} valen {precio:.2f} €' if fruta in frutas else 'no tenemos esa fruta, mira la lista')
'''


# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

""" 
def fecha():
    fecha = input('dame una fecha en formato dd/mm/aaaa: ')
    mes =  {
        1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre',
        10:'octubre', 11:'noviembre', 12:'diciembre'
    }

    fecha_separada = fecha.split('/')
    print(f'{fecha_separada[0]} de {mes[int(fecha_separada[1])]} de {fecha_separada[2]}')
fecha()
 """


# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
# asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
# asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.







# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez 
# que se añada un nuevo dato debe imprimirse el contenido del diccionario.





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










#Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
# cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con 
# las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla 
# palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.










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













#region  funciones
# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

'''
def saludo():
    print('hola')
saludo()
'''


# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

'''
def saludo_personal():
    nombre = 'manel'
    print(f'hola {nombre}')
saludo_personal()
'''


# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''
def factorial():
    cuenta = 1
    numero = int(input('dame un entero positivo: '))
    for i in range(numero):
        cuenta *= i+1
        print(cuenta)
factorial()        
'''
'''
def factorial(numero):
    cuenta = 1
    for i in range(numero):
        cuenta *= i+1
        print(cuenta)
    return cuenta
print(factorial(5))
'''


# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total 
# de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

'''
def total_factura(precio, iva=21):
    total = precio + (precio * iva) / 100
    return total
print(total_factura(123,15))
'''


# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

'''
def area_circulo(r):
    from math import pi as pi
    return pi * r**2

def volumen_cilindro(r, h):
    return area_circulo(r) * h

print(volumen_cilindro(3, 5))
'''


# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

'''
def media():
    numeros = [2,4,8,5,54,23,44,65,76]
    print(sum(numeros)/ len(numeros))
media()
'''


# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

'''
def cuadrados():
    numeros = [2,4,8,5,54,23,44,65,76]
    lista_cuadrados = []
    for i in numeros:
        lista_cuadrados.append(i*i)
    print(lista_cuadrados)
cuadrados()
'''        


# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
# varianza y desviación típica.

'''
numeros = [2,4,8,5,54,23,44,65,76]

def media():
    return sum(numeros) / len(numeros)

def cuadrado():
    cuadrados = []
    for i in numeros:
        cuadrados.append(i*i)
    return cuadrados
   
def varianza():
    lista = []
    for i in numeros:
        calculo = (i - media())**2
        lista.append(calculo)
    return sum(lista) / len(lista)

def desviacion():
    from math import sqrt as raiz #sqrt es la raiz completa //  isqrt es la raiz entera
    return raiz(varianza())

result = {
    'media' : f'{media():.2f}',
    'varianza' : f'{varianza():.2f}',
    'desviacion' : desviacion()
}

print(result)
'''

# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


def maximo_comun_divisor(n1, n2):
    pass


def minimo_comun_multiplo(n1, n2):
    pass







# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.









# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que 
# contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y 
# devuelva una tupla con la palabra más repetida y su frecuencia.















# Ejercicios de Programación Funcional
#region PROGRAMACION FUNCIONAL 
# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta 
# de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los 
# descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

""" 
def descuento(precio, descuento):
    return precio - ((precio * descuento) / 100)

def iva(precio, iva=21): 
    return precio + ((precio * iva) / 100)

def cesta_compra(cesta, funcion, *args):
    precio_total = 0
    print('precios: ')
    for producto, precio in cesta.items():
        precio_funcion = funcion(precio, *args)
        print(f'{producto}: {precio_funcion}€')
        precio_total += precio_funcion
    return precio_total

cesta = {
    'Laptop': 200,        
    'Auriculares': 30,   
    'Monitor': 25,       
    'Teclado': 50,        
    'Ratón': 20           
}

print(f'\ncesta compra con descuento\n')
total_descuento = cesta_compra(cesta, descuento, 10)
print(f'\ntotal con descuento: {total_descuento}€\n')

print(f'cesta compra con iva\n')
total_iva = cesta_compra(cesta, iva, 21)
print(f'\ntotal con iva: {total_iva}€')
"""


# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, 
# tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a 
# aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de 
# aplicar la función a esos enteros.






# Ejercicio 3
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de 
# aplicar la función dada a cada uno de los elementos de la lista.


#def funcion(otra_funcion, len(lista)):
    #return otra_lista
    #pass






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










#region ejercicios de ficheros
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
