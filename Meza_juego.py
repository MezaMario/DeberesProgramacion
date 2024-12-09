import tkinter as tk  # Se importa tkinter con un alias para simplificar
import random  # Se importa el módulo random para generar números aleatorios

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.geometry("400x300")  # Dimensiones de la ventana
ventana.title("Juego de Adivinanza")  # Título de la ventana

# Etiqueta principal
etiqueta = tk.Label(ventana, text="¡Adivina un número entre 1 y 10!", bg="blue", fg="white", font=("Arial", 14))
etiqueta.pack(pady=10)  # Agrega un poco de espacio vertical

# Caja de texto para que el usuario ingrese un número
cajatex = tk.Entry(ventana, font=("Arial", 12))
cajatex.pack(pady=5)

# Etiqueta para mostrar mensajes al usuario
mensaje = tk.Label(ventana, text="", fg="black", font=("Arial", 12))
mensaje.pack(pady=10)

# Función que maneja la lógica del juego
def jugar():
    texto_ingresado = cajatex.get()  # Se obtiene el texto ingresado por el usuario
    try:
        numero_usuario = int(texto_ingresado)  # Convertimos el texto a un número entero
        if 1 <= numero_usuario <= 10:  # Verificamos que el número esté en el rango válido
            numero_aleatorio = random.randint(1, 10)  # Generamos un número aleatorio entre 1 y 10
            if numero_usuario == numero_aleatorio:
                mensaje.config(text=f"¡Correcto! El número era {numero_aleatorio}. ¡Ganaste!", fg="green")
            else:
                mensaje.config(text=f"Incorrecto. El número era {numero_aleatorio}. ¡Intenta de nuevo!", fg="red")
        else:
            mensaje.config(text="Por favor, ingresa un número entre 1 y 10.", fg="orange")
    except ValueError:
        mensaje.config(text="Entrada no válida. Ingresa un número entero.", fg="red")

# Botón para iniciar el juego
boton = tk.Button(ventana, text="Jugar", padx=10, pady=5, command=jugar, bg="green", fg="white", font=("Arial", 12))
boton.pack(pady=10)

# Bucle principal para ejecutar la aplicación
ventana.mainloop()
