import tkinter as tk


# Crear ventana principal
root = tk.Tk()
root.title("Menú de Ejercicios")

# Ajustar el tamaño inicial de la ventana
root.geometry("600x700")  # Ancho x Alto en píxeles
root.configure(bg="#f0f0f0")  # Cambiar el color de fondo de la ventana

# Estilo de las etiquetas
label = tk.Label(
    root,
    text="Elige un ejercicio y escribe los datos correspondientes:",
    bg="#f0f0f0",  # Fondo igual al fondo de la ventana
    fg="#333333",  # Color del texto
    font=("Helvetica", 14),  # Fuente y tamaño del texto
    wraplength=550,  # Ajustar texto dentro de un ancho
    justify="center",  # Centrar el texto
)
label.pack(pady=20)


# Función para ejercicio 6: Factorial de un número
def ejercicio_6():
    def calcular_factorial():
        try:
            num = int(entry_factorial.get())
            if num < 0:
                result_label.config(text="Por favor, ingresa un número positivo.")
            else:
                factorial = 1
                for i in range(1, num + 1):
                    factorial *= i
                result_label.config(text=f"El factorial de {num} es: {factorial}")
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")
    
    # Crear ventana secundaria para el factorial
    factorial_window = tk.Toplevel(root)
    factorial_window.title("Ejercicio 6: Factorial de un número")

    tk.Label(factorial_window, text="Ingresa un número para calcular su factorial:").pack(pady=5)
    entry_factorial = tk.Entry(factorial_window)
    entry_factorial.pack(pady=5)

    button_calcular = tk.Button(factorial_window, text="Calcular factorial", command=calcular_factorial)
    button_calcular.pack(pady=5)

    result_label = tk.Label(factorial_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 7: Números primos entre 1 y 50
def ejercicio_7():
    # Crear ventana secundaria para los números primos
    prime_window = tk.Toplevel(root)
    prime_window.title("Ejercicio 7: Números primos")

    primes = []
    for num in range(2, 51):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    
    result = ', '.join(map(str, primes))
    tk.Label(prime_window, text=f"Números primos entre 1 y 50: {result}").pack(pady=20)


# Función para ejercicio 8: Invertir un número
def ejercicio_8():
    def invertir_numero():
        try:
            num = entry_numero.get()
            reversed_num = num[::-1]
            result_label.config(text=f"El número invertido es: {reversed_num}")
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")
    
    # Crear ventana secundaria para invertir el número
    invert_window = tk.Toplevel(root)
    invert_window.title("Ejercicio 8: Invertir un número")

    tk.Label(invert_window, text="Ingresa un número para invertir:").pack(pady=5)
    entry_numero = tk.Entry(invert_window)
    entry_numero.pack(pady=5)

    button_invertir = tk.Button(invert_window, text="Invertir número", command=invertir_numero)
    button_invertir.pack(pady=5)

    result_label = tk.Label(invert_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 9: Promedio de calificaciones
def ejercicio_9():
    def calcular_promedio():
        try:
            calificaciones = []
            while True:
                calificacion = float(entry_calificacion.get())
                if calificacion == -1:
                    break
                calificaciones.append(calificacion)
            if calificaciones:
                promedio = sum(calificaciones) / len(calificaciones)
                result_label.config(text=f"Promedio: {promedio:.2f}")
            else:
                result_label.config(text="No se ingresaron calificaciones válidas.")
        except ValueError:
            result_label.config(text="Por favor, ingresa una calificación válida.")
    
    # Crear ventana secundaria para el promedio
    promedio_window = tk.Toplevel(root)
    promedio_window.title("Ejercicio 9: Promedio de calificaciones")

    tk.Label(promedio_window, text="Ingresa calificaciones (termina con -1):").pack(pady=5)
    entry_calificacion = tk.Entry(promedio_window)
    entry_calificacion.pack(pady=5)

    button_calcular = tk.Button(promedio_window, text="Calcular promedio", command=calcular_promedio)
    button_calcular.pack(pady=5)

    result_label = tk.Label(promedio_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para abrir la ventana de selección de ejercicio
def open_exercise_window(exercise_number):
    if exercise_number == 6:
        ejercicio_6()
    elif exercise_number == 7:
        ejercicio_7()
    elif exercise_number == 8:
        ejercicio_8()
    elif exercise_number == 9:
        ejercicio_9()


# Botones para los ejercicios
button_6 = tk.Button(
    root,
    text="Ejercicio 6: Factorial de un número",
    command=lambda: open_exercise_window(6),
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12),
)
button_6.pack(pady=10)

button_7 = tk.Button(
    root,
    text="Ejercicio 7: Números primos",
    command=lambda: open_exercise_window(7),
    bg="#2196F3",
    fg="white",
    font=("Helvetica", 12),
)
button_7.pack(pady=10)

button_8 = tk.Button(
    root,
    text="Ejercicio 8: Invertir un número",
    command=lambda: open_exercise_window(8),
    bg="#FF9800",
    fg="white",
    font=("Helvetica", 12),
)
button_8.pack(pady=10)

button_9 = tk.Button(
    root,
    text="Ejercicio 9: Promedio de calificaciones",
    command=lambda: open_exercise_window(9),
    bg="#9C27B0",
    fg="white",
    font=("Helvetica", 12),
)
button_9.pack(pady=10)


# Ejecutar el bucle principal
root.mainloop()
