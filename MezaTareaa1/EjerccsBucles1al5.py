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


# Función para ejercicio 1: Imprimir números del 1 al 10
def ejercicio_1():
    # Crear ventana secundaria para mostrar los números
    num_window = tk.Toplevel(root)
    num_window.title("Ejercicio 1: Imprimir números del 1 al 10")
    
    result = ', '.join(str(i) for i in range(1, 11))
    tk.Label(num_window, text=f"Números del 1 al 10: {result}").pack(pady=20)


# Función para ejercicio 2: Suma de los primeros 10 números
def ejercicio_2():
    # Crear ventana secundaria para mostrar la suma
    sum_window = tk.Toplevel(root)
    sum_window.title("Ejercicio 2: Suma de los primeros 10 números")
    
    total_sum = sum(range(1, 11))
    tk.Label(sum_window, text=f"La suma de los primeros 10 números es: {total_sum}").pack(pady=20)


# Función para ejercicio 3: Tabla de multiplicar
def ejercicio_3():
    def show_multiplication_table():
        try:
            number = int(entry_number.get())
            table_result = '\n'.join(f"{number} x {i} = {number * i}" for i in range(1, 11))
            result_label.config(text=table_result)
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")

    # Crear ventana secundaria para mostrar la tabla
    table_window = tk.Toplevel(root)
    table_window.title("Ejercicio 3: Tabla de multiplicar")

    tk.Label(table_window, text="Ingresa un número para su tabla de multiplicar:").pack(pady=5)
    entry_number = tk.Entry(table_window)
    entry_number.pack(pady=5)

    show_button = tk.Button(table_window, text="Mostrar tabla", command=show_multiplication_table)
    show_button.pack(pady=5)

    result_label = tk.Label(table_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 4: Contar números pares
def ejercicio_4():
    # Crear ventana secundaria para mostrar los números pares
    even_window = tk.Toplevel(root)
    even_window.title("Ejercicio 4: Contar números pares")
    
    even_numbers = ', '.join(str(i) for i in range(2, 21, 2))
    tk.Label(even_window, text=f"Números pares entre 1 y 20: {even_numbers}").pack(pady=20)


# Función para ejercicio 5: Contador regresivo
def ejercicio_5():
    # Crear ventana secundaria para mostrar el contador regresivo
    countdown_window = tk.Toplevel(root)
    countdown_window.title("Ejercicio 5: Contador regresivo")
    
    countdown = ', '.join(str(i) for i in range(10, 0, -1))
    tk.Label(countdown_window, text=f"Contador regresivo del 10 al 1: {countdown}").pack(pady=20)


# Función para abrir la ventana de selección de ejercicio
def open_exercise_window(exercise_number):
    if exercise_number == 1:
        ejercicio_1()
    elif exercise_number == 2:
        ejercicio_2()
    elif exercise_number == 3:
        ejercicio_3()
    elif exercise_number == 4:
        ejercicio_4()
    elif exercise_number == 5:
        ejercicio_5()


# Botones para los ejercicios
button_1 = tk.Button(
    root,
    text="Ejercicio 1: Imprimir números del 1 al 10",
    command=lambda: open_exercise_window(1),
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12),
)
button_1.pack(pady=10)

button_2 = tk.Button(
    root,
    text="Ejercicio 2: Suma de los primeros 10 números",
    command=lambda: open_exercise_window(2),
    bg="#2196F3",
    fg="white",
    font=("Helvetica", 12),
)
button_2.pack(pady=10)

button_3 = tk.Button(
    root,
    text="Ejercicio 3: Tabla de multiplicar",
    command=lambda: open_exercise_window(3),
    bg="#FF9800",
    fg="white",
    font=("Helvetica", 12),
)
button_3.pack(pady=10)

button_4 = tk.Button(
    root,
    text="Ejercicio 4: Contar números pares",
    command=lambda: open_exercise_window(4),
    bg="#9C27B0",
    fg="white",
    font=("Helvetica", 12),
)
button_4.pack(pady=10)

button_5 = tk.Button(
    root,
    text="Ejercicio 5: Contador regresivo",
    command=lambda: open_exercise_window(5),
    bg="#E91E63",
    fg="white",
    font=("Helvetica", 12),
)
button_5.pack(pady=10)


# Ejecutar el bucle principal
root.mainloop()
