print(" ")
print("Mendez Sanchez Maria Guadalupe Yazmin 3w 1199")
print(" ")
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(materias)
print(" ")
calificaciones = {}  #Diccionario para que se almasenen las calificaciones
for materias in materias:  #Pedir las calificaciones
    calif = int(input(f"Ingresa la calificación de {materias}: "))
    print(" ")
    calificaciones[materias] = calif
# Eliminar asignaturas aprobadas
asignaturas_repetir = [asignatura for asignatura, calif in calificaciones.items() if calif < 6]
print(asignaturas_repetir)
print(" ")
# Mostrar asignaturas que se deben repetir
if asignaturas_repetir:
    print("Materia que tienes que repetir:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
print(" ")


