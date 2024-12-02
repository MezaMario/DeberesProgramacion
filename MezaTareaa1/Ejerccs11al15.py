import tkinter as tk
from tkinter import simpledialog
import random


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


# Función para ejercicio 11: Validar contraseñas
def ejercicio_11():
    def check_password():
        password = entry_password.get()
        if password == "12345":
            result = "Acceso concedido."
        else:
            result = "Contraseña incorrecta."
        result_label.config(text=result)

    # Crear ventana secundaria para la contraseña
    password_window = tk.Toplevel(root)
    password_window.title("Ejercicio 11: Validar contraseñas")

    tk.Label(password_window, text="Ingresa la contraseña:").pack(pady=5)
    entry_password = tk.Entry(password_window, show="*")  # Mostrar los caracteres como asteriscos
    entry_password.pack(pady=5)

    check_button = tk.Button(password_window, text="Verificar", command=check_password)
    check_button.pack(pady=5)

    result_label = tk.Label(password_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 12: Juego de números
def ejercicio_12():
    def guess_number():
        try:
            guess = int(entry_guess.get())
            if guess == random_number:
                result = "¡Felicidades, acertaste!"
            else:
                result = "Intenta de nuevo."
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Por favor, ingresa un número válido.")

    # Generar número aleatorio entre 1 y 10
    random_number = random.randint(1, 10)

    # Crear ventana secundaria para el juego de números
    number_game_window = tk.Toplevel(root)
    number_game_window.title("Ejercicio 12: Juego de números")

    tk.Label(number_game_window, text="Adivina el número entre 1 y 10:").pack(pady=5)
    entry_guess = tk.Entry(number_game_window)
    entry_guess.pack(pady=5)

    guess_button = tk.Button(number_game_window, text="Adivinar", command=guess_number)
    guess_button.pack(pady=5)

    result_label = tk.Label(number_game_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 13: Calcular el signo zodiacal
def ejercicio_13():
    def calculate_zodiac():
        try:
            day, month = map(str, entry_date.get().split(','))
            day = int(day.strip())
            month = month.strip().lower()

            if month == "marzo" and 21 <= day <= 31 or month == "abril" and 1 <= day <= 19:
                result = "Tu signo es Aries"
            elif month == "abril" and 20 <= day <= 30 or month == "mayo" and 1 <= day <= 20:
                result = "Tu signo es Tauro"
            elif month == "mayo" and 21 <= day <= 31 or month == "junio" and 1 <= day <= 20:
                result = "Tu signo es Géminis"
            # Se pueden seguir agregando más signos zodiacales según la fecha
            else:
                result = "No se pudo determinar el signo zodiacal con la fecha ingresada."
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Por favor, ingresa una fecha válida.")

    # Crear ventana secundaria para el signo zodiacal
    zodiac_window = tk.Toplevel(root)
    zodiac_window.title("Ejercicio 13: Calcular el signo zodiacal")

    tk.Label(zodiac_window, text="Ingresa el día y mes de nacimiento (Ejemplo: 22, marzo):").pack(pady=5)
    entry_date = tk.Entry(zodiac_window)
    entry_date.pack(pady=5)

    calculate_button = tk.Button(zodiac_window, text="Calcular signo", command=calculate_zodiac)
    calculate_button.pack(pady=5)

    result_label = tk.Label(zodiac_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para ejercicio 14: Sistema de calificaciones
def ejercicio_14():
    def calculate_grade():
        try:
            grade = float(entry_grade.get())
            if 90 <= grade <= 100:
                result = "Tu calificación es A."
            elif 80 <= grade < 90:
                result = "Tu calificación es B."
            elif 70 <= grade < 80:
                result = "Tu calificación es C."
            elif 60 <= grade < 70:
                result = "Tu calificación es D."
            else:
                result = "Tu calificación es F."
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Por favor, ingresa una calificación válida.")

    # Crear ventana secundaria para el sistema de calificaciones
    grade_window = tk.Toplevel(root)
    grade_window.title("Ejercicio 14: Sistema de calificaciones")

    tk.Label(grade_window, text="Ingresa la calificación:").pack(pady=5)
    entry_grade = tk.Entry(grade_window)
    entry_grade.pack(pady=5)

    calculate_button = tk.Button(grade_window, text="Calcular calificación", command=calculate_grade)
    calculate_button.pack(pady=5)

    result_label = tk.Label(grade_window, text="Resultado: ")
    result_label.pack(pady=10)


# Función para abrir la ventana de selección de ejercicio
def open_exercise_window(exercise_number):
    if exercise_number == 11:
        ejercicio_11()
    elif exercise_number == 12:
        ejercicio_12()
    elif exercise_number == 13:
        ejercicio_13()
    elif exercise_number == 14:
        ejercicio_14()


# Botones para los ejercicios
button_11 = tk.Button(
    root,
    text="Ejercicio 11: Validar contraseñas",
    command=lambda: open_exercise_window(11),
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 12),
)
button_11.pack(pady=10)

button_12 = tk.Button(
    root,
    text="Ejercicio 12: Juego de números",
    command=lambda: open_exercise_window(12),
    bg="#2196F3",
    fg="white",
    font=("Helvetica", 12),
)
button_12.pack(pady=10)

button_13 = tk.Button(
    root,
    text="Ejercicio 13: Calcular el signo zodiacal",
    command=lambda: open_exercise_window(13),
    bg="#FF9800",
    fg="white",
    font=("Helvetica", 12),
)
button_13.pack(pady=10)

button_14 = tk.Button(
    root,
    text="Ejercicio 14: Sistema de calificaciones",
    command=lambda: open_exercise_window(14),
    bg="#9C27B0",
    fg="white",
    font=("Helvetica", 12),
)
button_14.pack(pady=10)


# Ejecutar el bucle principal
root.mainloop()
