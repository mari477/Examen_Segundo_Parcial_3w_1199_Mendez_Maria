print(" ")
print("Mendez Sanchez Maria Guadalupe Yazmin 3w 1199")
print(" ")
creditos = {             #Diccionario con los creditos
    'Matemáticas':6,
    'Física':4,
    'Química':5
}
#Enseñar los créditos de cada asignatura
for asignatura, credito in creditos.items():
    print(f"{asignatura} tiene {credito} créditos.") #Se da los creditos con una f para no póner puntos o separaciones
total_creditos = sum(creditos.values())              #Calcular el total de los creditos
print(f"El número total de créditos es: {total_creditos}") #Se pone el numero total de los creditos y la f para hacerlo mas rapido
print(" ")