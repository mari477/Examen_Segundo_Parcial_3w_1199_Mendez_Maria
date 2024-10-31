print(" ")
print("Mendez Sanchez Maria Guadalupe Yazmin 3w 1199")
print(" ")
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] #Lista de asignaturas
calificaciones = {} #Diccionario para almacenar las calificaciones
for asignatura in materias: #Solicitar calificaciones
    nota = float(input(f"Ingresa la calificación de {asignatura}: ")) #Definir nota "ingresa la calificacion"
    calificaciones[asignatura] = nota                                 #Calificacion = a la nota
for asignatura, nota in calificaciones.items():                       # Mostrar resultados
    print(f"En {asignatura} has sacado {nota}.")                      #Muestra los resultados
print(" ")
