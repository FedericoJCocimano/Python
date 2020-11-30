nombre = str(input("Ingrese el nombre de la ong: "))
preg_realizadas = int(input("Ingrese la cantidad de preguntas realizadas: "))
preg_correctas = int(input("Ingrese cuántas preguntas se respondieron correctamente: "))
ong1 = ["Nombre de ONG: ", nombre, "Preguntas realizadas: ", preg_realizadas, "Preguntas correctas: ", preg_correctas]

nombre2 = str(input("Ingrese el nombre de la ong: "))
preg_realizadas2 = int(input("Ingrese la cantidad de preguntas realizadas: "))
preg_correctas2 = int(input("Ingrese cuántas preguntas se respondieron correctamente: "))
ong2 = ["Nombre de ONG: ", nombre2, "Preguntas realizadas: ", preg_realizadas2, "Preguntas correctas: ", preg_correctas2]

nombre3 = str(input("Ingrese el nombre de la ong: "))
preg_realizadas3 = int(input("Ingrese la cantidad de preguntas realizadas: "))
preg_correctas3 = int(input("Ingrese cuántas preguntas se respondieron correctamente: "))
ong3 = ["Nombre de ONG: ", nombre3, "Preguntas realizadas: ", preg_realizadas3, "Preguntas correctas: ", preg_correctas3]

nombre4= str(input("Ingrese el nombre de la ong: "))
preg_realizadas4 = int(input("Ingrese la cantidad de preguntas realizadas: "))
preg_correctas4 = int(input("Ingrese cuántas preguntas se respondieron correctamente: "))
ong4 = ["Nombre de ONG: ", nombre4, "Preguntas realizadas: ", preg_realizadas4, "Preguntas correctas: ", preg_correctas4]

x = int ; y = int
def niveles(x,y):
    nivel = x / y
    print("NIVEL:", nivel)
    if nivel < 0.5:
        print("El nivel es bajo")
    elif nivel >= 0.5 and nivel <= 0.74:
        print("El nivel es medio")
    elif nivel >= 0.75 and nivel <= 0.89:
        print("El nivel es aceptable")
    elif nivel >= 0.9:
        print("El nivel es óptimo")
    
def final():
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("Primera ong: ", ong1)
    niveles(preg_correctas, preg_realizadas)
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

    print("Segunda ong: ", ong2)
    niveles(preg_correctas2, preg_realizadas2) 
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

    print("Tercera ong: ", ong3)
    niveles(preg_correctas3, preg_realizadas3)
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

    print("Cuarta ong: ", ong4)
    niveles(preg_correctas4, preg_realizadas4) 
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
final()



