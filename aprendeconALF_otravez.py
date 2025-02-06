                    
                                  ###ejercicios remix aprendeconalf###





# region datossimples
# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

""" 
print('hola mundo :)')
 """


# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable 
# y luego muestre por pantalla el contenido de la variable.

""" 
hola = 'hola mundo'
print(hola)
 """


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla 
# la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

""" 
nombre = input('dame tu nombre: ')
print(f'hola {nombre}')
 """


# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética XX.

""" 
((3+2)/(2*5))**2
 """


# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

""" 
horas = float(input('cuantas horas trabajas: '))
coste_hora = float(input('a cuanto la hora: '))
print(f' te toocan {horas * coste_hora:.2f}€')
 """


# Ejercicio 6
# Escribir un programa que lea un entero positivo, "nombre entier"
# , introducido por el usuario y después muestre en pantalla la suma de todos los enteros 
# desde 1 hasta "n". 

""" 
numero_entero = int(input('dame un numero entero: '))
suma_numeros = 0
for i in range(1, numero_entero):
    suma_numeros += i+1
print(f'la suma de su rango es: {suma_numeros}')
 """


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (kg) y estatura (m), 
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase: "tu indice de masa corporal es "imc", 
# donde "imc" es el índice de masa corporal, calculado redondeado con dos decimales.

""" 
peso = float(input('cual es tu peso (kg): '))
altura = float(input('que altura (m): '))
imc = (peso / altura)**2
print(f'tu imc es {imc:.2f}')
 """


# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros 
# y muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

""" 
n_numero1 = int(input('necesito un numero entero: '))
m_numero2 = int(input('otro numero entero: '))
c_cociente = n_numero1 / m_numero2
r_resto = n_numero1 % m_numero2
print(f'{n_numero1} entre {m_numero2} da un cociente de {c_cociente:.2f} y un resto de {r_resto:.2f}')
 """ 


# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

"""   
    # formula del interes compuesto: M = (C (1+(r/n))) ** n t
    # M=monto incial, C=capital inicial, r=interes(decimal), n=numero de veces que capitaliza el interes anualmente, t=tiempo años

inversion = float(input('cantidad a invertir: '))
interes_anual = float(input('porcentaje interes anual: '))
años = int(input('cuantos años de inversion: '))
monto = inversion * (1 + ((interes_anual/100) / 12)) ** (12*años)
print(monto)
 """

""" 
def ahorro(cantidad_invertir, interes, años):
    cantidad = cantidad_invertir
    for i in range(1, años+1):
        cantidad = cantidad * (1+interes)
    print(f'ha obtenido {cantidad:.2f}€')
ahorro(1000, 0.04, 5)
 """


# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y 
# la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán 
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

""" 
def juguetes(ventas_payaso, ventas_muñeca):
    peso_payaso = 112
    peso_muñeca = 75
    payaso = ventas_payaso * peso_payaso
    muñeca = ventas_muñeca * peso_muñeca
    print(f'payasos: {ventas_payaso}, muñecas: {ventas_muñeca}, el peso del pedido es de {payaso + muñeca} gramos')
juguetes(10, 5)
 """


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

""" 
def cuenta_ahorros(interes=0.04, dinero_depositado=1000, años=3):
    cuenta = dinero_depositado
    for i in range(1, años+1):
        cuenta = cuenta * (1+interes)
        print(f'el año {i} tienes {cuenta:.2f}')
cuenta_ahorros()
 """


# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y el coste final total.

""" def panaderia(pan=3.49, descuento=60):
    descuento_decimal = descuento / 100
    barra_descuento = pan * (1- descuento_decimal)
    barras_vendidas_deayer = int(input('cuantas barras se vendieron de ayer: '))
    print(f'el precio de una barra de pan es {pan}€\nel descuento es del {descuento}%')
    print(f'el precio final de una barra es {barra_descuento}€\nel precio total es {barra_descuento * barras_vendidas_deayer:.2f}€')
panaderia()
 """


# region cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

""" 
def nombre():
    nombre = input('nombre: ')
    numero = int(input('que numero: '))
    print('\n'.join([nombre] * numero))
nombre()
 """

""" 
def nombre_bucle(nombre='currucu', numero=3):
    for i in range(numero):
        print(nombre)
nombre_bucle()
 """


# Ejercicio 2
# Escribir un programa que pregunte el nombre completo 
# del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas 
# las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y 
# minúsculas como quiera.

""" 
def mayus(nombre='currupipi'):
    print(nombre.capitalize())
    print(nombre.upper())
    print(nombre.lower())
mayus()
 """


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca, muestre por pantalla <NOMBRE> 
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y 
# <n> es el número de letras que tienen el nombre.

""" 
def nombre(nombre='currupipi'):
    print(f'el nombre {nombre.upper()}, tiene {len(nombre)} letras')
nombre()
 """


# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este 
# formato y muestre por pantalla el número de teléfono sin el prefijo y 
# la extensión.

""" 
def numero_telf():
    numero = input('telefono en formato prefijo-numero-extension: ')
    print(numero[3:-3])
numero_telf()
 """


# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en 
# la consola y muestre por pantalla la frase invertida.

""" 
def frase(frase='la mare que et va parir'):
    print(frase[::-1])
frase()
 """ 


# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase 
# en la consola y una vocal, y después muestre por pantalla la misma 
# frase pero con la vocal introducida en mayúscula.

""" 
def vocal(frase='la mare que et va parir', vocal='a'):
    print(frase.replace(vocal, vocal.capitalize()))
vocal()
 """


# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario 
# en la consola y muestre por pantalla otro correo electrónico con el 
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.    

""" 
def correo(correo='micorreo@gmail.com'):
    return correo[:correo.find('@')] + '@ceu.es'
print(correo())
 """


# Ejercicio 8
# Escribir un programa que pregunte por consola el precio 
# de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.

""" 
def precio(precio=23.99):
    precio = str(precio)
    return precio[:precio.find('.')] + '€', precio[precio.rfind('.')+1 :] + ' centavos'
print(precio())
 """


# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento 
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día 
# o el mes se introduzcan con un solo carácter.

""" 
def fecha_nacimiento(fecha='23/01/2020'):
    dia = fecha[:fecha.find('/')]
    mes = fecha[fecha.find('/')+1:fecha.rfind('/')]
    año = fecha[fecha.rfind('/')+1:]
    return f'dia: {dia}, mes: {mes}, año: {año}'
print(fecha_nacimiento())
 """
""" 
def nacimiento():
    fecha = input('fecha de nacimiento (dd/mm/aaaa): ')
    print(f'dia: {fecha[:2]}, mes: {fecha[3:5]}, año: {fecha[6:]}')
nacimiento()
 """


# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos 
# de una cesta de la compra, separados por comas, y muestre por 
# pantalla cada uno de los productos en una línea distinta.

""" 
def lista_compra(listacompra = f'patatas, manzanas, peras, platanos'):
    return listacompra.replace(',', '\n')
print(lista_compra())
 """


# Ejercicio 11
# Escribir un programa que pregunte el nombre de un producto, 
# su precio y un número de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido de su precio unitario con 6 dígitos 
# enteros y 2 decimales, el número de unidades con tres dígitos 
# y el coste total con 8 dígitos enteros y 2 decimales.

""" 
def producto(nombre='pan', precio=1.10, unidades=2):
    total = precio * unidades
    return f'nombre: {nombre}, precio: {precio:08.2f}€, unidades: {unidades:3d}u., total = {total:10.2f}€'
print(producto())
 """


# region condicionales
# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla si es mayor de edad o no.

""" 
def edad(edad):
    if edad >= 18:
        print('eres mayor de edad')
    else:
        print('eres menor')
edad(22)
 """  

"""  
def edad(edad):
    print(f'eres mayor de edad' if edad>=18 else 'eres menor')
edad(17)
 """


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña 
# en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

""" 
def contraseña(contraseña_usuario):
    contraseña = '1234'
    print(f'bienvenido, contraseña correcta' if contraseña.lower()==contraseña_usuario.lower() else 'error, contraseña incorrecta')
contraseña('1234')
 """

""" 
    # voy a hacerlo con un bucle while (al final con un poco de ayuda lol)
def contraseña(contraseña_usuario):
    contraseña = '1234'
    contador = 0
    while contador <= 5:
        contraseña_usuario = input('dime la contraseña: ')
        if contraseña != contraseña_usuario:
            print('contraseña incorrecta, intentalo de nuevo')
            contador += 1
            print(f'intentos {contador}')
        else:
            print('bingo!')
            break
contraseña('kjhvh')
 """


# Ejercicio 3
# Escribir un programa que pida al usuario dos números y 
# muestre por pantalla su división. Si el divisor es cero el 
# programa debe mostrar un error.

""" 
def division(n1, n2):
    if n2 == 0:
        print('error, el divisor no puede ser 0')
    else:
        result = n1/n2
        print(f'la division da {result}')
division(3,5)
 """  

"""  
def division(n1, n2):
    print('error'if n2==0 else f'la division es {n1/n2}')
division(23,5)
 """


# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar.

""" 
def par_impar(numero):
    if numero%2 == 0:
        print('es par')
    else:
        print('es impar')
par_impar(7)
 """


# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y 
# sus ingresos mensuales y muestre por pantalla si el usuario 
# tiene que tributar o no.

""" 
def impuestos(edad, ingresos):
    if edad < 16 or ingresos < 1000:
        print('sales a 0, no tributas')
    else:
        print('paga impuestos perro')
impuestos(22, 1800)
 """


# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. El grupo A esta formado por 
# las mujeres con un nombre anterior a la M y los hombres con 
# un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.

""" 
def alumnos(nombre, sexo):
    # hombre: h
    # mujer: f
    if sexo == 'f' and nombre < 'm' or sexo == 'h'and nombre > 'n':
        print('perteneces al grupo A')
    else:
        print('grupo B')
alumnos('paco', 'f')
 """


# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un 
# determinado país son los siguientes:
# Renta 	Tipo impositivo
# Menos de 10000€ 	5%
# Entre 10000€ y 20000€ 	15%
# Entre 20000€ y 35000€ 	20%
# Entre 35000€ y 60000€ 	30%
# Más de 60000€ 	45%
# Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impositivo que le corresponde.

""" 
def impuestos():
    renta = int(input('cual es tu renta anual: '))
    if renta < 10000:
        print('te corresponde el 5%')
    elif renta > 10000 and renta < 20000:
        print('pagas el 15%')
    elif renta > 20000 and renta < 35000:
        print('pagas el 20%')
    elif renta > 35000 and renta < 60000:
        print('pagas el 30%')
    else:
        print('pagas el 45%')
impuestos()
 """


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

""" 
def puntos_trabajador():
    puntuacion_usuario = float(input('cual ha sido tu puntuacion: '))
    if puntuacion_usuario == 0.0:
        nivel = 'inaceptable'
    elif puntuacion_usuario == 0.4:
        nivel = 'aceptable'
    elif puntuacion_usuario >= 0.6:
        nivel = 'meritorio'
    else:
        print('puntuacion incorrecta')
        return
    calculo = 2400 * puntuacion_usuario
    print(f'tu nivel es {nivel}, recibiras: {calculo}€')
puntos_trabajador()
 """
 

# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos 
# para todas las edades y quiere calcular de forma automática el 
# precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y 
# mostrar el precio de la entrada. Si el cliente es menor de 4 años 
# puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.

""" 
def precio_entrada(edad):
    if edad > 0 and edad < 4:
        precio = 0
    elif edad >= 4 and edad < 18:
        precio = 5
    elif edad >= 18:
        precio = 10
    else:
        print('edad incorrecta')
        return
    print(f'con {edad} años, su entrada cuesta {precio}€')
precio_entrada(7)
 """


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

""" 
def pizzeria():
    vegetarian = ['pimiento', 'tofu']
    no_vegetarian = ['peperoni', 'jamon', 'salmon']
    pregunta_usuario = input('quieres pizza vegeta?  (si/no): ').strip().lower()
    if pregunta_usuario == 'si':
        print(f'pizza vegetariana: {vegetarian}')
        opcion = vegetarian
    elif pregunta_usuario == 'no': 
        print(f'las pizzas no vegeta son de: {no_vegetarian}')
        opcion = no_vegetarian
    else:
        print('error, opciones: si / no')
        return
    ingrediente = input('elige un ingrediente de los opcionales: ').strip().lower()         # .strip() para quitar los espacios del str
    if ingrediente in opcion:
        print(f'elegiste la pizza con {ingrediente}, buen provecho')
    else:
        print('ingrediente seleccionado no disponible')
        return
pizzeria()
 """


# region bucles
# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y 
# la muestre por pantalla 10 veces.

""" 
def palabrax10(palabra):
    contador = 0
    while contador < 10:
        print(palabra)
        contador += 1
palabrax10('mane')
 """


# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

""" 
def edad_iteracion(edad):
    for i in range(1, edad+1):
        print(i)
edad_iteracion(6)
 """


# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese 
# número separados por comas.

""" 
# 'separador'.join(lista) para unir elementos de la lista
def entero_positivo(numero):
    impares = []
    if not isinstance(numero, int) or numero < 1:       # isinstance(dato, type) para comprobar el typo y condicionarlo
        return print('numero erroneo')
    else:
        for i in range(1, numero+1):
            if i % 2 != 0:
                impares.append(str(i))
    print(','.join(impares))
entero_positivo(20)
 """


# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta 
# cero separados por comas.

""" 
def cuenta_atras(numero):
    listado = []
    for i in range(numero, 0, -1):
        listado.append(str(i))
    print(','.join(listado))
cuenta_atras(7)
 """


# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

""" 
def inversiones(capital=2000, interes=4, años=10):
    cuenta = 0
    for i in range(1, años+1):
        capital *= 1 + interes / 100
        print(f'capital tras el {i} año: {capital:.2f}€')
    return capital
inversiones()
 """


# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido.

""" 
# copiado
def triangulo(numero):
    for i in range(numero):
        for j in range(i +1):
            print('*', end='')
        print('')
triangulo(6)
 """


# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

""" 
# copiado
def tabla_multiplicar():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end='\t')
        print('')
tabla_multiplicar()
 """ 


# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.

""" 
def otro_triangulo(numero):
    for i in range(1, numero+1):
        for j in range(i+1):
            print('*', end='')
        print('')
otro_triangulo(3)
 """


# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres 
# contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.

""" 
def contraseña():
    contraseña = 'hola perra'
    while True:
        usuario = str(input('dame la contraseña: '))
        if usuario == contraseña:
            print('bienvenido')
            break
        else:
            print('contraseña incorrecta, prueba otra vez')
contraseña()
 """


# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es un número primo o no

""" 
# con ayuda de chat, haciendolo con la raiz cuadrada envez de hacer el for para todo el numero

import math
def numero_primo(numero):
    if numero < 2:
        print('no es primo')
        return
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            print('no es primo')
            return
    print('numero primo')

numero = int(input('Introduce un número entero: ')) 
numero_primo(numero)
 """


# Ejercicio 11
# escribe un programa que pida al usuario una palabra y luego muesre por panatalla
# una a una de las letras de la palabra introducida empezando por la última.

""" 
def al_reves(palabra):
    print(palabra[::-1])
al_reves('macarroni')
 """

""" 
def alreves(palabra):
    for i in palabra[::-1]:
        print(i)
alreves('carbonari')
 """


# region listas y tuplas
# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo matematicas, fisica
# quimica, historia y lengua) en una lista y la muestre por pantalla

""" 
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
print(', '.join(asignaturas))
 """


# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
# Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

""" 
asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
print(f'yo estudio {asignaturas}')
for i in asignaturas:
    print(f'yo estudio {i}')
 """


# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

""" 
# resuelto con ayuda
def asignaturas():
    asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
    notas = []
    for asignatura in asignaturas:
        nota = float(input(f'que nota has sacado en {asignatura}: '))
        notas.append(nota)
    for i in range(len(asignaturas)):
        print(f'en {asignaturas[i]} has sacado {notas[i]}')
asignaturas()
 """


# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

""" 
# version simple

def loteria():
    numeros = []
    contador = 0
    while contador < 5:    
        numero = int(input('dime los numeros ganadores: '))
        numeros.append(numero)
        contador += 1
    print(sorted(numeros))
loteria()
 """

""" 
# con ayuda
def loteria():
    numeros = []
    while len(numeros) < 6:
        try:
            numero = int(input('dame el numero ganador: '))
            if numero < 1 or numero > 49:
                print('error, el numero tiene que estar entre 1 y 49')
            elif numero in numeros:
                print('error, numero repetido')
            else:
                numeros.append(numero)
        except ValueError:
            print('tienes que introducir numeros')
    print(f'los numeros ganadores son: {sorted(numeros)}')
loteria()
 """


# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

""" 
# me estaba liando, al final facil con un bucle
def lista_inversa():
    lista = []
    for i in range(1, 11):
        lista.append(i)
    print(lista[::-1])
lista_inversa()
 """


# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en 
# cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
#  por pantalla las asignaturas que el usuario tiene que repetir.

""" 
def asignaturas_suspensas():
    asignaturas = ['matematicas', 'fisica', 'quimica', 'historia', 'lengua']
    notas = []
    for i in asignaturas:
        nota = float(input(f'que nota has sacado en {i} '))
        if nota < 5:
            notas.append(i)
    if notas:        
        print(f'debes repetir: {", ".join(notas)}')
    else:
        print('todo aprovado, genial')
asignaturas_suspensas()
 """


# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
 
"""  
#  con ayuda
import string
abecedario = list(string.ascii_lowercase)
for i in range(len(abecedario),0,-1):
    if i %3 == 0:
        abecedario.pop(i-1)
print(abecedario)
 """


# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

""" 
def palindromo(palabra):  
    palabra = palabra.lower().replace(' ', '')
    if palabra == palabra[::-1]:
        print(f'{palabra} es palindromo')
    else:
        print(f'{palabra} NO es palindromo')
palindromo('dabale arroz a la zorra el abad')
 """


# Ejercicio 9
# Escribir un programa que pida al usuario una palabra/frase y muestre por pantalla el número de veces que contiene cada vocal.

""" 
def contador_vocales_bucle():
    vocales = ['a','e','i','o','u']
    palabra = input('dame una palabra: ')
    for i in vocales:
        contador = 0
        for letra in palabra:
            if letra == i:
                contador += 1
        print(f'la vocal {i} aparace {contador} veces en la palabra {palabra}')
contador_vocales_bucle()
 """

""" 
def contador_vocales(palabra):
    vocales = 'aeiou'
    contador = {vocal:0 for vocal in vocales}       # dict compression
    for i in palabra.lower():
        if i in vocales:
            contador[i] += 1
    print(contador)
contador_vocales('cuantas vocales hay en esta frase?')
 """


# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.

""" 
def menor_mayor():
    listado = [50, 75, 46, 22, 80, 65, 8]
    listado = sorted(listado)
    print(listado[0], listado[-1])
menor_mayor()
 """

""" 
def menor_mayor_funciones():
    listado = [50, 75, 46, 22, 80, 65, 8]
    print(min(listado), max(listado))
menor_mayor_funciones()    
 """


# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.


# producto a escalar = primer elemento x primer elemento + segundo x segundo + tercero x tercero + ...
# los vectores (listas de numeros) tienen que tener el mismo numero de elementos

def producto_a_escalar():
    listado1 = [2,3,4]      
    listado2 = [5,6,7,]
    if len(listado1) != len(listado2):
        print('los vectores tienen que contener el mismo numero de elementos')
        return
    else:
        producto = 0
        for i in range(len(listado1)):
            producto += listado1[i] * listado2[i]
        print(producto)
producto_a_escalar()


def producto_a_escalar_comprido():
    listado1 = [2,3,4]      
    listado2 = [5,6,7,]
    if len(listado1) != len(listado2):
        print('los vectores tienen que contener el mismo numero de elementos')
        return
    else:
        producto = sum(a*b for a, b in zip(listado1, listado2))
    print(f'producto a escalar: {producto}')
producto_a_escalar()


# Ejercicio 12
# Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.










# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista 
# y muestre por pantalla su media y desviación típica.







# region diccionarios
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.









# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.






# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número 
# de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Fruta 	Precio
# Plátano 	1.35
# Manzana 	0.80
# Pera 	0.85
# Naranja 	0.70










# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.








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










# Ejercicio 8
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













# region  funciones
# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.







# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.







# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.






# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total 
# de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.









# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.











# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.













# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.












# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, 
# varianza y desviación típica.












# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.









# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.









# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que 
# contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y 
# devuelva una tupla con la palabra más repetida y su frecuencia.















# Ejercicios de Programación Funcional
# region PROGRAMACION FUNCIONAL 
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










# region ejercicios de ficheros
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





# region Ejercicios depuracion
# Ejercicio 1
# Corregir los errores sintácticos del siguiente programa:

# contraseña = input('Introduce la contraseña: ")
# if contraseña in ['sesamo'):
#   print('Pasa')
# else
#   print('No pasa')










# Ejercicio 2
# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:

# base = input('Introduce la base imponible de la factura: ')
# print(aplica_iva(base, iva))

# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base 






# Ejercicio 3
# Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:

# u = (1, 2, 3)
# v = (4, 5, 6)

# def producto_escalar(u, v):
#     for i in u:
#         u[i+1] *= v[i+1]
#     return sum(u)

# print(producto_escalar(u, v))









# Ejercicio 4
# Detectar y corregir los errores del siguiente programa que devuelve y elimina el teléfono de un listín telefónico a través del nombre del usuario:

# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     del listin[usuario]
#     return listin[usuario]

# print(elimina(listin, 'Pablo'))










# Ejercicio 5
# Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

# a = ((1, 2, 3),
#      (3, 2, 1))
# b = ((1, 2),
#      (3, 4),
#      (5, 6))

# def producto(a, b):
#     producto = []
#     for i in range(len(b)):
#         fila = []
#         for j in range(len(a[0])):
#             suma = 0
#             for k in range(len(a[0]+1)):
#                 suma += a[i][k] * b[k+1][j]
#             fila[j] = suma
#         producto[i] = tuple(fila)
#     return tuple(producto)

# print(producto(a, b))







# region Pandas
# Ejercicios de la Librería Pandas

# Ejercicio 1
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie 
# con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.








# Ejercicio 2
# Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una 
# serie con la nota mínima, la máxima, media y la desviación típica.





# Ejercicio 3
# Escribir una función que reciba un diccionario con las notas de los alumnos de un curso 
# y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.






# Ejercicio 4
# Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
# Mes 	Ventas 	Gastos
# Enero 	30500 	22000
# Febrero 	35600 	23400
# Marzo 	28300 	18100
# Abril 	33900 	20700









# Ejercicio 5
# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, 
# una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.









# Ejercicio 6
# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes 
# columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
# Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
# volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). 
# Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y devuelva 
# otro DataFrame con el mínimo, el máximo y la media de dada columna.








# Ejercicio 7
# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
    # Generar un DataFrame con los datos del fichero.
    # Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
    # Mostrar por pantalla los datos del pasajero con identificador 148.
    # Mostrar por pantalla las filas pares del DataFrame.
    # Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
    # Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
    # Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
    # Eliminar del DataFrame los pasajeros con edad desconocida.
    # Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
    # Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
    # Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.










# Ejercicio 8
# Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos 
# sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente.
# Escribir un programa con los siguientes requisitos:

#     Generar un DataFrame con los datos de los cuatro ficheros.
#     Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes 
# a los días D01, D02, etc.
#     Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
#     Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
#     Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por 
# estaciones contaminantes y fecha.
#     Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
#     Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las 
# emisiones del contaminante dado en la estación y rango de fechas dado.
#     Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
#     Mostrar un resumen descriptivo para cada contaminante por distritos.
#     Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones 
# del contaminante indicado en la estación indicada.
#     Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
#     Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos 
# tipos de contaminantes.










# region Matplotlib
# Ejercicios de la librería Matplotlib

# Ejercicio 1
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de 
# líneas con la evolución de las ventas.












# Ejercicio 2
# Escribir una función que reciba una diccionario con las notas de las asignaturas de un curso y una cadena con 
#  el nombre de un color y devuelva un diagrama de barras de las notas en el color dado.











# Ejercicio 3
# Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso y devuelva 
# un diagrama de cajas con las notas. El diagrama debe tener el título “Distribución de notas”.










# Ejercicio 4
# Escribir una función que reciba una serie de Pandas con el número de ventas de un producto durante los meses 
# de un trimestre y un título y cree un diagrama de sectores con las ventas en formato png con el titulo dado. 
# El diagrama debe guardarse en un fichero con formato png y el título dado.













# Ejercicio 5
# Escribir una función que reciba una serie de Pandas con el número de ventas de un producto por años y una cadena con 
# el tipo de gráfico a generar (lineas, barras, sectores, areas) y devuelva un diagrama del tipo indicado con la evolución 
# de las ventas por años y con el título “Evolución del número de ventas”.















# Ejercicio 6
# Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa por meses y 
# devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos. El diagrama debe 
# tener una leyenda identificando la línea de los ingresos y la de los gastos, un título con el nombre “Evolución 
# de ingresos y gastos” y el eje y debe empezar en 0.













# Ejercicio 7
# El fichero bancos.csv contiene las cotizaciones de los principales bancos de España con : Empresa (nombre de la empresa), 
# Apertura (precio de la acción a la apertura de bolsa), Máximo (precio máximo de la acción durante la jornada), 
# Mínimo (precio mínimo de la acción durante la jornada), Cierre (precio de la acción al cierre de bolsa), 
# Volumen (volumen al cierre de bolsa). Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas
#  con las series temporales de las cotizaciones de cierre de cada banco.













# Ejercicio 8
# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y 
# a partir de él generar los siguientes diagramas.
#     Diagrama de sectores con los fallecidos y supervivientes.
#     Histograma con las edades.
#     Diagrama de barras con el número de personas en cada clase.
#     Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
#     Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.

