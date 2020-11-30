print("Formas de concatenar: ")
nombre = "Federico"
apellido = "Cocimano"
print(nombre, apellido) #Esto no es concatenar, pero se obtiene el mismo resultado
print(nombre + " " + apellido)
print(f"{nombre} {apellido}")
print("Hola me llamo: {} {}".format(nombre, apellido))

print("Tipos de datos")
nada = None
cadena_txt = "Soy Federico Cocimano" #str
entero_num = 100 #int
decimano_num = 5.5 #float
complejo_num = 7j #complex
booleano = False #bool
lista_sequence = ["manzana",  "naranja", "banana"] #list
tupla_seq = (1,2,3,4,5) #tuple
rango_seq = range(5) #range
diccionario = {"nombre": "Mario", "edad": 23} #dict
dato_byte = b"dato" #bytes
print(type(nada))#Mostrar tipo de dato
