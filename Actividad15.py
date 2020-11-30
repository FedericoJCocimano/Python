cont = 0 
nombres_apellidos = []
promfinal = []
materias_libres = []

while cont < 6:
    nombre = str(input("Ingrese el nombre del alumno: "))
    n = nombre.title()
    apellido = str(input("Ingrese el apellido del alumno: "))
    a = apellido.title()
    lista = [n,a]
    nombres_apellidos.extend(lista)
    promediofinal = float(input("Ingrese su promedio final: "))
    promfinal.append(promediofinal)
    materias = int(input("Ingrese la cantidad de materias que le quedan: "))
    materias_libres.append(materias)
    cont += 1


c = 0
name = 0
lastname = 1
alumnos_totales = []

def alumnos(c,name,lastname):
    while c != len(promfinal):
        alumnos_totales.insert(c, nombres_apellidos[name] + " " + nombres_apellidos[lastname])
        c += 1
        name += 2
        lastname += 2
alumnos(c,name,lastname)


alumnos_definitivos = []
alumnos_libres = {}
x = 0

def aprobados(x):
    while x != len(promfinal):
        if promfinal[x] >= 6 and materias_libres[x] == 0:
            alumnos_definitivos.append(alumnos_totales[x])
            x += 1
        else:
            alumnos_libres[alumnos_totales[x]] = materias_libres[x]
            x += 1
aprobados(x)


print("---------------------------------------------------------------------------------------")
print("Alumnos de la Promo 2020: ", alumnos_totales)
print("Promedio de cada alumno: ", promfinal)
print("Alumnos que terminaron definitivamente: ", alumnos_definitivos)
print("Alumnos que le quedan materias: ", alumnos_libres)

porcentaje_final = (len(alumnos_definitivos) / len(promfinal)) * 100
print("Porcentaje de alumnos egresados definitivamente: ", porcentaje_final, "%")

mejorpromedio = max(promfinal)
posicion = promfinal.index(mejorpromedio)
mejoralumno = alumnos_totales[posicion]
print("El mejor alumno/a es: ", mejoralumno, "// Promedio: ", mejorpromedio)
print("---------------------------------------------------------------------------------------")
