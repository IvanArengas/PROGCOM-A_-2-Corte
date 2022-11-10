import sys

lista = []
maximo = 5

semestre1cred = {
    "Fundamentos de programación": 3,
    "Dibujo básico": 1,
    "Seminario de ingeniería I": 1,
    "Expresión": 4,
    "Cálculo de una variable": 4,
    "Álgebra lineal": 4
}
semestre2cred = {
    "Programación de computadoras": 3,
    "Dibujo técnico": 1,
    "Seminario de ingeniería II": 1,
    "Mecánica": 3,
    "Cálculo en varias variables": 4,
    "Química para ingenieros": 3,
    "Identidad y emprendimiento": 3
}
semestre3cred = {
    "Estática": 2,
    "Estadística general": 3,
    "Seminario de ingeniería III 3": 1,
    "Electromagnetismo": 3,
    "Ecuaciones diferenciales": 4,
    "Termodinámica": 3
}


semestre1 = {
    "Fundamentos de programación": 0,
    "Dibujo básico": 0,
    "Seminario de ingeniería I": 0,
    "Expresión": 0, "Cálculo de una variable": 0, "Álgebra lineal": 0
}
semestre2 = {
    "Programación de computadoras": 0,
    "Dibujo técnico": 0,
    "Seminario de ingeniería II": 0,
    "Mecánica": 0,
    "Cálculo en varias variables": 0,
    "Química para ingenieros": 0,
    "Identidad y emprendimiento": 0
}
semestre3 = {
    "Estática": 0,
    "Estadística general": 0,
    "Seminario de ingeniería III 3": 0,
    "Electromagnetismo": 0,
    "Ecuaciones diferenciales": 0,
    "Termodinámica": 0
}

class Alumnos():
    def __init__(self):
        self.ID = ""
        self.nombre = ""
        self.edad = ""
        self.carrera = ""
        self.semestre = ""
        self.materias = []
        self.creditos = 0

def menu():
    while True:
        seleccion = 0
        print("Bienvenidos a la aplicación de registro de alumnos de la UNAB")
        print("Cosmos UNAB")
        print("Elija una de las opciones")
        print("-------------------------------------------------------------------")
        print("1. Registrar el alumno")
        print("2. Mostrar alumnos registrados")
        print("3. Salir")
        seleccion = int(input("Eliga una opción: "))
        if seleccion == 1:
            registrar()
        if seleccion == 2:
            mostrar()
        if seleccion == 3:
            salir()

def registrar():
    alumno = Alumnos()
    alumno.ID = input("Introduce el ID: ")
    alumno.nombre = input("Introduce el nombre: ")
    alumno.edad = input("Introduce la edad: ")
    alumno.carrera = input("Introduce la carrera que cursa: ")
    alumno.semestre = input("Ingrese el semestre a matricular (1/2/3): ")
    a = 0
    materia = alumno.materias

    def mat(semestre, semestrecred, clase):
        print("Personas matriculadas:")
        print(semestre[clase])
        if clase in materia:
          print("Ya matriculaste esta materia.")
        elif int(semestre[clase]) == maximo:
            print("La materia ya llegó al límite de estudiantes.")
        else:
            semestre[clase] = int(semestre[clase])+1
            alumno.creditos += semestrecred[clase]
            materia.append(clase)
            print("Has matriculado", clase)

    mensaje = "Escribe el número correspondiente a la materia que quieres matricular o presiona 0 si quieres volver al menú principal. "
    if alumno.semestre == "1":
        semestre = semestre1
        semestrecred = semestre1cred
        for x in semestre1:
            a += 1
            print(str(a) + ".", x)
        while True:
            sel = input(mensaje)
            if sel == "1":
                mat(semestre, semestrecred, "Fundamentos de programación")
            if sel == "2":
                mat(semestre, semestrecred, "Dibujo básico")
            if sel == "3":
                mat(semestre, semestrecred, "Seminario de ingeniería I")
            if sel == "4":
                mat(semestre, semestrecred, "Expresión")
            if sel == "5":
                mat(semestre, semestrecred, "Cálculo de una variable")
            if sel == "6":
                mat(semestre, semestrecred, "Álgebra lineal")
            if sel == "0":
                break
    elif alumno.semestre == "2":
        semestre = semestre2
        semestrecred = semestre2cred
        for x in semestre2:
            a += 1
            print(str(a) + ".", x)
        while True:
            sel = input(mensaje)
            if sel == "1":
                mat(semestre, semestrecred, "Programación de computadoras")
            if sel == "2":
                mat(semestre, semestrecred, "Dibujo técnico")
            if sel == "3":
                mat(semestre, semestrecred, "Seminario de ingeniería II")
            if sel == "4":
                mat(semestre, semestrecred, "Mecánica")
            if sel == "5":
                mat(semestre, semestrecred, "Cálculo en varias variables")
            if sel == "6":
                mat(semestre, semestrecred, "Química para ingenieros")
            if sel == "7":
                mat(semestre, semestrecred, "Identidad y emprendimiento")
            if sel == "0":
                break
    elif alumno.semestre == "3":
        semestre = semestre3
        semestrecred = semestre3cred
        for x in semestre3:
            a += 1
            print(str(a) + ".", x)
        while True:
            sel = input(mensaje)
            if sel == "1":
                mat(semestre, semestrecred, "Estática")
            if sel == "2":
                mat(semestre, semestrecred, "Estadística general")
            if sel == "3":
                mat(semestre, semestrecred, "Seminario de ingeniería III 3")
            if sel == "4":
                mat(semestre, semestrecred, "Electromagnetismo")
            if sel == "5":
                mat(semestre, semestrecred, "Ecuaciones diferenciales")
            if sel == "6":
                mat(semestre, semestrecred, "Termodinámica")
            if sel == "0":
                break
    if len(alumno.materias) > 1:
        lista.append(alumno)
    else:
        print(
            "No se matriculó ningúna materia, por ende no se guardara ningúna información.")

def mostrar():
    print("Esta es la función para mostrar los alumnos registrados")
    for alumno in lista:
        print("\nEl/La estudiante", alumno.nombre, "de ID", alumno.ID, "con edad de", alumno.edad, "que cursa la carrera",
              alumno.carrera, "matrículó", alumno.creditos, "creditos para el semestre", alumno.semestre,
              "con las materias:")
        for x in alumno.materias:
            print(x)

def salir():
    print("Gracias por usar Cosmos para matricularte")
    sys.exit()

menu()