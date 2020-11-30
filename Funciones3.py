text = str(input("Ingrese el texto(punto para que termine):"))
x = text.endswith(".")
if x == True:
    print("!----------------------------------------------------------------------!")
    print("Texto: ", text)
    print("!----------------------------------------------------------------------!")
else:
    print("Error, debe colocar punto al final.")
    import sys
    sys.exit(0)

Texto = text.lower()
Texto1 = Texto.split()
print("Palabras en el texto: ", Texto1) 

def cuenta_letra(letra):  
    contt = 0
    cantidad_t = 0
    palabra = 0
    cantidad_palabras = len(Texto1)
    while contt != len(Texto1):
        if Texto1[palabra].count(letra) == 1:
            cantidad_t += 1 
            palabra += 1
            contt += 1
        else:
            palabra += 1
            contt += 1
    if cantidad_t == 0:
        print("No hay palabras con una sola t")
    else:
        porcentaje = (cantidad_t / cantidad_palabras) * 100
        print("Cantidad de palabras con una sola t:", cantidad_t)
        print("Representan un:", porcentaje, "%", "del total de palabras.")

cuenta_letra("t")

def palabras_mayores():
    mayor = 0
    cont = 0
    z = 0
    y = 1
    while cont != len(Texto1) - 1:
        if len(Texto1[z]) < len(Texto1[y]):
            mayor = mayor + 1 
            z += 1
            y += 1
            cont += 1
        else:
            z += 1
            y += 1
            cont += 1

    print("Cantidad de palabras que tienen mas letras que la anterior: ", mayor)

palabras_mayores()

def palabras_pares_c(val):
    c = 0
    pal = 0
    cantidad_paryc = 0
    while c != len(Texto1):
        if Texto1[pal].startswith(val) == 0 and len(Texto1[pal])%2 == 0:
            cantidad_paryc += 1
            pal += 1
            c += 1
        else:
            pal += 1
            c += 1
    
    print("Cantidad de palabras con cantidad pares de letras y empiezan con c: ", cantidad_paryc)

palabras_pares_c("c")