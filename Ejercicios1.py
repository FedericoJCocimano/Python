'''
Ejercicio 1:
    -Ingresar variable "país" y "Contintente".
    -Mostrar su valor por pantalla.
    -Indicar el tipo de dato por pantalla.
'''
def ejercicio1():
    pais = str(input("Ingrese el pais: "))
    continente = str(input("Ingrese el continente al que pertenece: "))
    print(f"El país es {pais} y se encuentra en el continente de {continente}")
    dato = type(pais)
    print("Tipo de dato: ", dato)

'''
Ejercicio 2: Escribir un script que nos muestre por pantalla
todos los números pares del 1 al 120.
'''

def ejercicio2():
    num_pares = []
    for x in range(1, 121):
        if x % 2 == 0:
            num_pares.append(x)
    print("Los números pares son: ", num_pares)

'''
Ejercicio 3: Escribir un programa que muestre los cuadrados de
los 60 primeros números naturales. Resolverlo con for o while.
'''

def ejercicio3():
    for x in range(1, 61):
        print(f"{x} * {x} = {x*x}")

'''
Ejercicio 4: Pedir dos números al usuario y hacer todas las operaciones
básicas de una calculadora y mostrarlo por pantalla.
'''

def ejercicio4():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    suma = n1 + n2
    resta1 = n1 - n2
    resta2 = n2 - n1
    multiplicación = n1 * n2
    división1 = n1 / n2
    división2 = n2 / n1
    resto1 = n1 % n2
    resto2 = n2 % n1

    print("Suma:", suma,"\nResta1:", resta1,"\nResta2:", resta2,"\nMultiplicación:", multiplicación)
    print("División1:", división1,"\nDivisión2:", división2,"\nResto1:", resto1,"\nResto2:", resto2)

'''
Ejercicio 5: Hacer un programa que muestre todos los números
entre dos números que especifique el usuario.
'''

def ejercicio5():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    ab = a - b
    ba = b - a
    if a < b:
        a += 1
        for i in range(a, b):
            print(i)
        if ab == 1 or ba == 1:
            print("No hay números enteros entre ambos, son contiguos")
    elif a > b:
        b += 1
        for i in range(b, a):
            print(i)
        if ab == 1 or ba == 1:
            print("No hay números enteros entre ambos, son contiguos")
    else:
        print("No pueden ser los mismos números")

'''
Ejercicio 6: Mostrar todas las tablas de multiplicar del 1 al 10; que se 
muestre el título de la tabla y multiplicaciones del 1 al 10.
'''

def ejercicio6():
    c = 1
    while c != 11:
        print("Tabla de multiplicar del: ", c)
        for x in range(1, 11):
            print(f"{x} * {c} = {x*c}")
        c += 1

'''
Ejercicio 7: Hacer un programa que muestre todos los números impares
entre dos números elegidos por el usuario.
'''

def ejercicio7():
    n1 = int(input("Ingrese el primer número:"))
    n2 = int(input("Ingrese el segundo número:"))
    if n1 < n2:
        if n1 - n2 == 1 or n2 - n1 == 1:
            print("No hay números enteros entre ambos, son contiguos")
        n1 += 1
        for i in range(n1, n2):
            if i % 2 != 0:
                print(i)
    elif n1 > n2:
        if n1 - n2 == 1 or n2 - n1 == 1:
            print("No hay números enteros entre ambos, son contiguos")
        n2 += 1
        for i in range(n2, n1):
            if i % 2 != 0:
                print(i)
    else:
        print("No pueden ser los mismos números")

'''
Ejercicio 8: ¿Cuánto es el Y por ciento de X número?(X, Y lo define el usuario)
Ejemplo: 20% de 100
'''
def ejercicio8():
    num = int(input("Eliga el número: "))   
    porcentaje = int(input("Diga el procentaje que quiera sacar: "))
    operacion = num * (porcentaje/100)
    print(f"El {porcentaje}% de {num} es igual a: {operacion}")

'''
Ejercicio9: Hacer un programa que pida números al usuario 
indefinidamente hasta elegir el número 111.
'''

def ejercicio9():
    num = int
    while num != 111:
        num = int(input("Ingrese un número(111 para finalizar): "))
        if num == 111:
            print("Hasta luego!!")
        else:
            print(num)

'''
Ejercicio 10: El programa tiene que pedir la nota de 15 alumnos y que diga
cuántos alumnos han aprobado y cuántos han reprobado.
'''

def ejercicio10():
    c = 1
    aprobados = 0
    reprobados = 0
    while c <= 15:
        nota = int(input("Ingrese la nota: "))
        if nota > 5:
            aprobados = aprobados + 1
            c += 1 
        elif nota <= 5:
            reprobados = reprobados + 1
            c += 1
    print("Cantidad de alumnos aprobados: ", aprobados)
    print("Cantidad de alumnos reprobados: ", reprobados)

ejercicio = int(input("Elija el ejercicio que desea realizar(1 al 10): "))
if ejercicio == 1:
    ejercicio1()
elif ejercicio == 2:
    ejercicio2()
elif ejercicio == 3:
    ejercicio3()
elif ejercicio == 4:
    ejercicio4()
elif ejercicio == 5:
    ejercicio5()
elif ejercicio == 6:
    ejercicio6()
elif ejercicio == 7:
    ejercicio7()
elif ejercicio == 8:
    ejercicio8()
elif ejercicio == 9:
    ejercicio9()
elif ejercicio == 10:
    ejercicio10()
