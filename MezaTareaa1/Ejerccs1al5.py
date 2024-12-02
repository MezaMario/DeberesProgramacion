import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicios del 1 al 5")

# Ajustar el tamaño inicial de la ventana
root.geometry("600x600")  # Ancho x Alto en píxeles
root.configure(bg="#f0f0f0")  # Cambiar el color de fondo de la ventana

# Estilo de las etiquetas
label = tk.Label(
    root,
    text="Elige un ejercicio y escribe un número para verificar:",
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

# Función para ejercicio 1: Mayor, menor o igual que 10
def ejercicio_1():
    try:
        a = int(entry.get())  # Obtener y convertir la entrada a un entero
        if a > 10:
            result = f"El número {a} es mayor a 10."
        elif a == 10:
            result = f"El número {a} es igual a 10."
        else:
            result = f"El número {a} es menor a 10."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa un número válido.")  # Manejo de errores si no es un número

# Función para ejercicio 2: Positivo, negativo o cero
def ejercicio_2():
    try:
        a = int(entry.get())  # Obtener y convertir la entrada a un entero
        if a > 0:
            result = f"El número {a} es positivo."
        elif a < 0:
            result = f"El número {a} es negativo."
        else:
            result = "El número es cero."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa un número válido.")  # Manejo de errores si no es un número

# Función para ejercicio 3: Par o impar
def ejercicio_3():
    try:
        a = int(entry.get())  # Obtener y convertir la entrada a un entero
        if a % 2 == 0:
            result = f"El número {a} es par."
        else:
            result = f"El número {a} es impar."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa un número válido.")  # Manejo de errores si no es un número

# Función para ejercicio 4: Aprobado o reprobado
def ejercicio_4():
    try:
        calificacion = float(entry.get())  # Obtener y convertir la entrada a un número flotante
        if calificacion >= 7:
            result = f"¡Aprobado! La calificación es {calificacion}."
        else:
            result = f"Reprobado. La calificación es {calificacion}."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa una calificación válida.")  # Manejo de errores si no es un número

# Función para ejercicio 5: Descuento en tienda
def ejercicio_5():
    try:
        gasto = float(entry.get())  # Obtener y convertir la entrada a un número flotante
        if gasto > 100:
            descuento = gasto * 0.20
            monto_final = gasto - descuento
            result = f"Monto final: ${monto_final:.2f} (Descuento del 20%)."
        else:
            result = f"Monto final: ${gasto:.2f} (Sin descuento)."
        label.config(text=result)  # Actualizar el texto de la etiqueta con el resultado
    except ValueError:
        label.config(text="Por favor, ingresa un monto válido.")  # Manejo de errores si no es un número

# Botón para ejercicio 1
button_1 = tk.Button(
    root,
    text="Ejercicio 1: Mayor o menor que 10",
    command=ejercicio_1,
    bg="#4CAF50",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#45a049",  # Color al presionar el botón
)
button_1.pack(pady=10)

# Botón para ejercicio 2
button_2 = tk.Button(
    root,
    text="Ejercicio 2: Positivo, negativo o cero",
    command=ejercicio_2,
    bg="#2196F3",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#1e88e5",  # Color al presionar el botón
)
button_2.pack(pady=10)

# Botón para ejercicio 3
button_3 = tk.Button(
    root,
    text="Ejercicio 3: Par o impar",
    command=ejercicio_3,
    bg="#FF9800",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#fb8c00",  # Color al presionar el botón
)
button_3.pack(pady=10)

# Botón para ejercicio 4
button_4 = tk.Button(
    root,
    text="Ejercicio 4: Aprobado o reprobado",
    command=ejercicio_4,
    bg="#9C27B0",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#8e24aa",  # Color al presionar el botón
)
button_4.pack(pady=10)

# Botón para ejercicio 5
button_5 = tk.Button(
    root,
    text="Ejercicio 5: Descuento en tienda",
    command=ejercicio_5,
    bg="#FF5722",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    font=("Helvetica", 12),
    activebackground="#e64a19",  # Color al presionar el botón
)
button_5.pack(pady=10)

# Botón para limpiar la entrada
def on_clear():
    entry.delete(0, tk.END)  # Limpia el campo de texto
    label.config(text="Elige un ejercicio y escribe un número para verificar:")  # Restaura el texto original

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
