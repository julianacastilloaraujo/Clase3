def solicitar_datos():
  nombre = input("Ingrese su nombre: ")
  asignaturas = ["Linea de Profundizacion III", "Ingles II", "Gerencia Informatica"]
  notas = {}
  for asignatura in asignaturas:
    while True:
      try:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        if nota < 0:
          raise ValueError("Ingresaste un valor no numerico negativo")
        break
      except ValueError:
        print("Hay un error, debes volver a cargar tus datos")
    notas[asignatura] = nota
  return nombre, notas

def calcular_promedio(notas):
  suma_notas = 0
  for nota in notas.values():
    suma_notas += nota
  return suma_notas / len(notas)

def determinar_estado(nota):
  if nota < 1:
    return "Estudiante Reprobado"
  elif nota < 2.5:
    return "Estudiante en Condicionamiento"
  elif nota < 2.9:
    return "Estudiante con probabilidades de aprobar"
  elif nota < 3:
        return "Estudiante aprobado"
  elif nota < 4:
    return "Estudiante aprobado"
  elif nota < 5:
        return "Estudiante aprobado con excelente promedio"
  else:
    return "Estudiante aprobado con excelente promedio"

def mostrar_resultado(nombre, notas, promedio):
  print(f"Nombre: {nombre}")
  for asignatura, nota in notas.items():
    estado = determinar_estado(nota)
    print(f"{asignatura}: {nota:.2f} ({estado})")
  print(f"Promedio: {promedio:.2f}")

if __name__ == "__main__":
  nombre, notas = solicitar_datos()
  promedio = calcular_promedio(notas)
  mostrar_resultado(nombre, notas, promedio)
