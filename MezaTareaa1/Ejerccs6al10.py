import tkinter as tk
from tkinter import simpledialog


# Crear ventana principal
root = tk.Tk()
root.title("Ejercicios 6 al 10")

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

# Entrada de texto
entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
entry.pack(pady=10)

# Función para ejercicio 6: Edad para votar
def ejercicio_6():
    try:
        edad = int(entry.get())  # Obtener y convertir la entrada a un entero
        if edad >= 18:
            result = f"Puedes votar. Tienes {edad} años."
        else:
            result = f"No puedes votar. Tienes {edad} años."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa una edad válida.")  # Manejo de errores si no es un número

# Función para ejercicio 7: Mayor de tres números
def ejercicio_7():
    try:
        nums = list(map(int, entry.get().split(',')))  # Obtener y convertir los números a una lista
        mayor = max(nums)  # Encontrar el mayor número
        result = f"El número mayor es {mayor}."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa tres números válidos separados por coma.")  # Manejo de errores

# Función para ejercicio 8: Clasificación de edades
def ejercicio_8():
    try:
        edad = int(entry.get())  # Obtener y convertir la entrada a un entero
        if 0 <= edad <= 12:
            result = "Eres niño."
        elif 13 <= edad <= 17:
            result = "Eres adolescente."
        else:
            result = "Eres adulto."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa una edad válida.")  # Manejo de errores si no es un número

# Función para ejercicio 9: Calculadora básica
def open_calculator_window():
    # Crear una ventana secundaria para la calculadora
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculadora Básica")

    # Etiquetas y entrada para la calculadora
    tk.Label(calc_window, text="Ingresa el primer número:").pack(pady=5)
    num1_entry = tk.Entry(calc_window)
    num1_entry.pack(pady=5)

    tk.Label(calc_window, text="Ingresa el segundo número:").pack(pady=5)
    num2_entry = tk.Entry(calc_window)
    num2_entry.pack(pady=5)

    # Función para realizar el cálculo
    def calculate():
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())
            operation = simpledialog.askstring("Operación", "Escribe la operación (+, -, *, /):")
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    result = "Error: No se puede dividir entre cero."
                else:
                    result = num1 / num2
            else:
                result = "Operación no válida."
            result_label.config(text=f"Resultado: {result}")
        except ValueError:
            result_label.config(text="Por favor, ingresa números válidos.")

    # Botón para realizar el cálculo
    calculate_button = tk.Button(calc_window, text="Calcular", command=calculate)
    calculate_button.pack(pady=10)

    # Etiqueta para mostrar el resultado
    result_label = tk.Label(calc_window, text="Resultado: ")
    result_label.pack(pady=10)

# Función para ejercicio 10: Determinar un año bisiesto
def ejercicio_10():
    try:
        año = int(entry.get())  # Obtener y convertir el año a un entero
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            result = f"El año {año} es bisiesto."
        else:
            result = f"El año {año} no es bisiesto."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa un año válido.")  # Manejo de errores si no es un número

# Función para limpiar la entrada
def on_clear():
    entry.delete(0, tk.END)  # Limpia el campo de texto
    label.config(text="Elige un ejercicio y escribe los datos correspondientes:")  # Restaura el texto original

# Botón para ejercicio 6
button_6 = tk.Button(
    root,
    text="Ejercicio 6: Edad para votar",
    command=ejercicio_6,
    bg="#4CAF50",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#45a049",  # Color al presionar el botón
)
button_6.pack(pady=10)

# Botón para ejercicio 7
button_7 = tk.Button(
    root,
    text="Ejercicio 7: Mayor de tres números",
    command=ejercicio_7,
    bg="#2196F3",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#1e88e5",  # Color al presionar el botón
)
button_7.pack(pady=10)

# Botón para ejercicio 8
button_8 = tk.Button(
    root,
    text="Ejercicio 8: Clasificación de edades",
    command=ejercicio_8,
    bg="#FF9800",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#fb8c00",  # Color al presionar el botón
)
button_8.pack(pady=10)

# Botón para ejercicio 9 (Calculadora Básica)
button_9 = tk.Button(
    root,
    text="Ejercicio 9: Calculadora básica",
    command=open_calculator_window,  # Abre la ventana de la calculadora
    bg="#9C27B0",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#8e24aa",  # Color al presionar el botón
)
button_9.pack(pady=10)

# Botón para ejercicio 10
button_10 = tk.Button(
    root,
    text="Ejercicio 10: Año bisiesto",
    command=ejercicio_10,
    bg="#FF5722",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#e64a19",  # Color al presionar el botón
)
button_10.pack(pady=10)

# Botón para limpiar la entrada
clear_button = tk.Button(
    root,
    text="Limpiar",
    command=on_clear,
    bg="#f44336",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#e53935",  # Color al presionar el botón
)
clear_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
