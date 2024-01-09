def gradingStudents(nota):
    if nota < 40:
        return nota  # No redondear si la nota es inferior a 40 (calificación suspensa)
    else:
        # Calcular el próximo múltiplo de 5
        siguiente_multiplo_5 = (nota // 5 + 1) * 5

        # Redondear si la diferencia es menor que 3
        if siguiente_multiplo_5 - nota < 3:
            return siguiente_multiplo_5
        else:
            return nota

def resultado(nota):
    if nota < 40:
        return "Suspenso"
    else:
        return "Aprobado"

# Input del usuario: introducir el array de notas de los estudiantes
notas_estudiantes = input("Introduce el array de notas de los estudiantes separadas por espacios: ")
notas_array = [float(nota) for nota in notas_estudiantes.split()]

# Procesar cada nota en el array
for i, nota in enumerate(notas_array):
    nota_redondeada = gradingStudents(nota)
    calificacion = resultado(nota_redondeada)
    print(f"Estudiante {i + 1}: Nota final: {nota_redondeada}, Calificación: {calificacion}")
