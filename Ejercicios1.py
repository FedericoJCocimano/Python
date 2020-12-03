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



