# Preguntar al usuario
print(" ")
print("Mendez Sanchez Maria Guadalupe Yazmin 3w 1199")
print(" ")
preg = {"nombre": "", "edad": "", "direccion": "", "telefono": ""}  # Diccionario para almacenar los datos
for i in preg:                                                      # Solicitar información al usuario
    dt = input(f"¿Cuál es tu {i}? \n")                              # Usar f-string para mayor claridad
    preg[i] = dt
    print(" ")
# Mostrar la salidar 
print(f"{preg['nombre' ]} tiene {preg['edad']} años, vive en {preg['direccion']} y su número de teléfono es: {preg['telefono']}")
print(" ") 