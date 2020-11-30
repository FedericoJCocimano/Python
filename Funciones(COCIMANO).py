def ejercicio1():
    print("----------EJERCICIO 1----------")
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    num3 = int(input("Introduzca el tercer número: "))

    def numero(num1,num2,num3):
        num_siguiente1 = num1 + 1
        num_siguiente2 = num2 + 1
        num_siguiente3 = num3 + 1
        print("Número posterior de cada número elegido previamente: ")
        print(num_siguiente1,num_siguiente2,num_siguiente3)
    
    numero(num1,num2,num3)
    
def ejercicio2():
    print("----------EJERCICIO 2----------")
    def lista():
        num = []
        val = int
        while val != 0:
            val = int(input("Ingrese un valor para la lista (0 para parar): "))
            num.append(val)
            print(num)
        
        num.remove(0)
        print("Números en la lista: ", num)
        def multiplicacion():
            import math
            resultado = math.prod(num)
            print("Resultado al multiplicar los números entre si: ", resultado)
        multiplicacion()
    lista()

def ejercicio3():
    print("----------EJERCICIO 3----------")
    primer_num = int(input("Ingrese el primer número a sumar: "))
    cantidad_num = int(input("Ingrese la cantidad de números que quiere sumar: "))
    import random
    valores_aleatorios = random.sample(range(1,101),cantidad_num)
    valores_aleatorios.append(primer_num)
    print("Valores de la cantidad: ", valores_aleatorios)
    valores_sumados = sum(valores_aleatorios)
    print("Valores sumados: ", valores_sumados)

a = int(input("Elija el ejercicio que desea realizar (1,2 o 3): "))
if a == 1:
    ejercicio1()
elif a == 2:
    ejercicio2()
elif a == 3:
    ejercicio3()