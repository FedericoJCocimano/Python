frutas = ("Manzanas", "Bananas", "Duraznos", "Mandarinas", "Naranjas",
         "Peras", "Uvas", "Ciruelas", "Mangos", "Cerezas")

precio_frutas = {"Manzanas": [60, 100, 115], 
                 "Bananas": [45, 70, 105],
                 "Duraznos": [75, 130, 140],
                 "Mandarinas":[60, 85, 100],
                 "Naranjas": [65, 95, 125],
                 "Peras": [80, 105, 120],
                 "Uvas": [90, 150, 170],
                 "Ciruelas": [80, 95, 100],
                 "Mangos": [100, 150, 210],
                 "Cerezas": [95, 140, 190]}

valor = 1
valorfinal = 2

acumulador1 = 0
acumulador2 = 0
acumulador3 = 0

def LaFruteria():
    print("Bienvenido a fruteria Carlitos, yo soy Carlitos")
    print("Poseo las siguientes frutas:")
    for x in frutas:
        print(x)

def bolsas(b):
    return b * 5

def final():   
    Precio_final = acumulador1 + acumulador2 + acumulador3 + bolsas(b)
    if acumulador1 > acumulador2 and acumulador1 > acumulador3:
        def Cantidad_mas_comprada():
            print("Se pidio mas de un cuarto")
    elif acumulador2 > acumulador1 and acumulador2 > acumulador3:
        def Cantidad_mas_comprada():
            print("Se pidio mas de medio kilo")
    elif acumulador3 > acumulador1 and acumulador3 > acumulador2:
        def Cantidad_mas_comprada():
            print("Se pidio mas de un kilo")
    else:
        def Cantidad_mas_comprada():
            pass
    
    print("Muchas gracias por comprar")
    Cantidad_mas_comprada()
    print("Debe pagar: $", Precio_final)

    
LaFruteria()


while valor < valorfinal:
    fruta = input(str("¿Qué fruta desea llevar?"))
    fruta1 = fruta.title()
    cantidad = input(str("¿Cuánto desea llevar? Opciones: uncuarto, mediokilo, kilo. "))
    cantidad1 = cantidad.upper()
    if fruta1 in precio_frutas:
        lista = precio_frutas.get(fruta1)
        if cantidad1 == "UNCUARTO":
           precio1 = lista[0]
           acumulador1 = acumulador1 + precio1
        elif cantidad1 == "MEDIOKILO":
            precio2 = lista[1]
            acumulador2 = acumulador2 + precio2
        elif cantidad1 == "KILO":
            precio3 = lista[2]
            acumulador3 = acumulador3 + precio3
    respuesta = input(str("¿Algo más?"))
    res1 = respuesta.title()
    if res1 == "No":
        bols= input(str("¿Quiere bolsas?"))
        bols1=bols.title()
        if bols1 == "Si":
            bolsa = int(input("¿Cuántas?"))
            b = bolsa
            bolsas(b)
            valor = 3
            final()
        else:
            b = 0
            valor = 3
            final()
            
    elif res1 == "Si":
        valor = 0 




    



        