import tkinter as tk
import math


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


# Función para ejercicio 1: Saludo personalizado
def ejercicio_1():
    def saludar():
        name = entry_name.get()
        saludo = f"Hola, {name}!"
        result_label.config(text=saludo)
    
    # Crear ventana secundaria para el saludo
    saludo_window = tk.Toplevel(root)
    saludo_window.title("Ejercicio 1: Saludo personalizado")

    tk.Label(saludo_window, text="Ingresa tu nombre:").pack(pady=5)
    entry_name = tk.Entry(saludo_window)
    entry_name.pack(pady=5)

    button_saludar = tk.Button(saludo_window, text="Saludar", command=saludar)
    button_saludar.pack(pady=5)

    result_label = tk.Label(saludo_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 2: Suma de dos números
def ejercicio_2():
    def sumar():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            suma = num1 + num2
            result_label.config(text=f"La suma es: {suma}")
        except ValueError:
            result_label.config(text="Por favor, ingresa números válidos.")
    
    # Crear ventana secundaria para la suma
    suma_window = tk.Toplevel(root)
    suma_window.title("Ejercicio 2: Suma de dos números")

    tk.Label(suma_window, text="Ingresa dos números:").pack(pady=5)
    entry_num1 = tk.Entry(suma_window)
    entry_num1.pack(pady=5)
    entry_num2 = tk.Entry(suma_window)
    entry_num2.pack(pady=5)

    button_sumar = tk.Button(suma_window, text="Sumar", command=sumar)
    button_sumar.pack(pady=5)

    result_label = tk.Label(suma_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 3: Número par o impar
def ejercicio_3():
    def verificar_par_impar():
        try:
            num = int(entry_num.get())
            if num % 2 == 0:
                result_label.config(text=f"{num} es par.")
            else:
                result_label.config(text=f"{num} es impar.")
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")
    
    # Crear ventana secundaria para par o impar
    par_impar_window = tk.Toplevel(root)
    par_impar_window.title("Ejercicio 3: Número par o impar")

    tk.Label(par_impar_window, text="Ingresa un número:").pack(pady=5)
    entry_num = tk.Entry(par_impar_window)
    entry_num.pack(pady=5)

    button_verificar = tk.Button(par_impar_window, text="Verificar", command=verificar_par_impar)
    button_verificar.pack(pady=5)

    result_label = tk.Label(par_impar_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 4: Calcular el cuadrado
def ejercicio_4():
    def calcular_cuadrado():
        try:
            num = float(entry_num.get())
            cuadrado = num ** 2
            result_label.config(text=f"El cuadrado de {num} es: {cuadrado}")
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")
    
    # Crear ventana secundaria para el cuadrado
    cuadrado_window = tk.Toplevel(root)
    cuadrado_window.title("Ejercicio 4: Calcular el cuadrado")

    tk.Label(cuadrado_window, text="Ingresa un número:").pack(pady=5)
    entry_num = tk.Entry(cuadrado_window)
    entry_num.pack(pady=5)

    button_calcular = tk.Button(cuadrado_window, text="Calcular cuadrado", command=calcular_cuadrado)
    button_calcular.pack(pady=5)

    result_label = tk.Label(cuadrado_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 5: Calcular el área de un círculo
def ejercicio_5():
    def calcular_area():
        try:
            radio = float(entry_radio.get())
            area = math.pi * (radio ** 2)
            result_label.config(text=f"El área del círculo es: {area:.2f}")
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")
    
    # Crear ventana secundaria para el área
    area_window = tk.Toplevel(root)
    area_window.title("Ejercicio 5: Calcular el área de un círculo")

    tk.Label(area_window, text="Ingresa el radio del círculo:").pack(pady=5)
    entry_radio = tk.Entry(area_window)
    entry_radio.pack(pady=5)

    button_calcular = tk.Button(area_window, text="Calcular área", command=calcular_area)
    button_calcular.pack(pady=5)

    result_label = tk.Label(area_window, text="Resultado: ")
    result_label.pack(pady=10)


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
    text="Ejercicio 1: Saludo personalizado",
    command=lambda: open_exercise_window(1),
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12),
)
button_1.pack(pady=10)

button_2 = tk.Button(
    root,
    text="Ejercicio 2: Suma de dos números",
    command=lambda: open_exercise_window(2),
    bg="#2196F3",
    fg="white",
    font=("Helvetica", 12),
)
button_2.pack(pady=10)

button_3 = tk.Button(
    root,
    text="Ejercicio 3: Número par o impar",
    command=lambda: open_exercise_window(3),
    bg="#FF9800",
    fg="white",
    font=("Helvetica", 12),
)
button_3.pack(pady=10)

button_4 = tk.Button(
    root,
    text="Ejercicio 4: Calcular el cuadrado",
    command=lambda: open_exercise_window(4),
    bg="#9C27B0",
    fg="white",
    font=("Helvetica", 12),
)
button_4.pack(pady=10)

button_5 = tk.Button(
    root,
    text="Ejercicio 5: Calcular el área de un círculo",
    command=lambda: open_exercise_window(5),
    bg="#FF5722",
    fg="white",
    font=("Helvetica", 12),
)
button_5.pack(pady=10)


# Ejecutar el bucle principal
root.mainloop()
