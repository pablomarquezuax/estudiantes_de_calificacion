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

# Input del usuario: introducir la nota del estudiante
nota_estudiante = float(input("Introduce la nota del estudiante (0-100): "))

# Redondear la nota y obtener la calificación
nota_redondeada = gradingStudents(nota_estudiante)
calificacion = resultado(nota_redondeada)

# Mostrar resultados
print(f"Nota final: {nota_redondeada}")
print(f"Resultado: {calificacion}")
