# 1. Solicitar información inicial
nombre_curso = input("Ingresa el nombre del curso: ")
cantidad_notas = int(input(f"¿Cuántas notas deseas ingresar para {nombre_curso}?: "))

# 2. Variable para acumular la suma de las notas
suma_total = 0

# 3. Ciclo for para pedir cada nota
# range(cantidad_notas) hará que el ciclo se repita las veces indicadas
for i in range(cantidad_notas):
    # Pedimos la nota y la convertimos a decimal (float)
    nota = float(input(f"Ingresa la nota número {i + 1}: "))
    # Sumamos la nota a nuestro acumulador
    suma_total += nota

# 4. Calcular el promedio
promedio = suma_total / cantidad_notas

# 5. Mostrar el resultado final
print("-" * 30)
print(f"En el curso {nombre_curso}, el promedio final es: {promedio:.2f}")