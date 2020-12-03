'''
Ejercicio 1:
    -Ingresar variable "pais" y "Contintente".
    -Mostrar su valor por pantalla.
    -Indicar el tipo de dato por pantalla.
'''
def ejercicio1():
    pais = str(input("Ingrese el pais: "))
    continente = str(input("Ingrese el continente al que pertenece: "))
    print(f"El pais es {pais} y se encuentra en el continente de {continente}")
    dato = type(pais)
    print("Tipo de dato: ", dato)

'''
Ejercicio 2: Escribir un script que nos muestre por pantalla
todos los numeros pares del 1 al 120.
'''

def ejercicio2():
    num_pares = []
    for x in range(1, 121):
        if x % 2 == 0:
            num_pares.append(x)
    print("Los numeros pares son: ", num_pares)

'''
Ejercicio 3: Escribir un programa que muestre los cuadrados de
los 60 primeros numeros naturales. Resolverlo con for o while.
'''

def ejercicio3():
    for x in range(1, 61):
        print(f"{x} * {x} = {x*x}")
        
'''
Ejercicio 4: Pedir dos números al usuario y hacer todas las operaciones
básicas de una calculador y mostrarlo por pantalla.
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
Ejercicio 5: Hacer un programa que muestre todos los numeros
entre dos numeros que especifique el usuario.
'''

def ejercicio5():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if a < b:
        a += 1
        for i in range(a, b):
            print(i)
    elif a > b:
        b += 1
        for i in range(b, a):
            print(i)
    else:
        print("No pueden ser los mismos numeros")


