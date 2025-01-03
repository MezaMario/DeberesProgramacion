import random  # Importamos la librería random
import tkinter as tk  # Importamos la librería tkinter

def ventana_principal():
    """
    Crea la ventana principal del juego del ahorcado.
    """
    root = tk.Tk()
    root.title("Ahorcado")
    root.geometry("300x300")

    etiqueta_bienvenida = tk.Label(root, text="¡Bienvenido al juego del ahorcado!", font=("Arial", 14))
    etiqueta_bienvenida.pack(pady=20)

    boton_jugar = tk.Button(root, text="Jugar", font=("Arial", 12), command=ventana_juego)
    boton_jugar.pack(pady=10)
    
    etiqueta_creador = tk.Label(root, text="Creado por: Mario Meza", font=("Arial", 10))
    etiqueta_creador.pack(pady=10)

    root.mainloop()

def palabra_aleatoria():
    """
    Selecciona una palabra aleatoria de una lista predefinida.
    """
    palabras = ["murcielago", "programacion", "python", "ahorcado", "computadora", "inteligencia", "artificial"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_correctas):
    """
    Genera el tablero del juego mostrando las letras correctas y espacios en blanco.
    """
    tablero = ""
    for letra in palabra:
        if letra in letras_correctas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def dibujo_ahorcado(vidas):
    """
    Genera el dibujo del ahorcado según el número de vidas restantes.
    """
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]
    return estados[6 - vidas]

def ventana_juego():
    """
    Crea la ventana de juego del ahorcado y gestiona la lógica del juego.
    """
    palabra = palabra_aleatoria()
    letras_correctas = []
    vidas = 6

    def actualizar_tablero():
        """
        Actualiza el tablero del juego y verifica el estado de la partida.
        """
        tablero = mostrar_tablero(palabra, letras_correctas)
        etiqueta_tablero.config(text=tablero)
        etiqueta_ahorcado.config(text=dibujo_ahorcado(vidas))
        if tablero.replace(" ", "") == palabra:
            etiqueta_resultado.config(text="¡Felicidades! ¡Ganaste!", fg="green")
            entrada_letra.config(state="disabled")
            boton_enviar.config(state="disabled")
        elif vidas == 0:
            etiqueta_resultado.config(text=f"¡Perdiste! La palabra era: {palabra}", fg="red")
            entrada_letra.config(state="disabled")
            boton_enviar.config(state="disabled")

    def ingresar_letra():
        """
        Captura y procesa la letra ingresada por el jugador.
        """
        nonlocal vidas
        letra = entrada_letra.get().lower()
        entrada_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            etiqueta_resultado.config(text="Por favor, ingresa una letra válida.", fg="orange")
            return

        if letra in letras_correctas:
            etiqueta_resultado.config(text="¡Ya ingresaste esa letra!", fg="orange")
            return

        if letra in palabra:
            letras_correctas.append(letra)
        else:
            vidas -= 1
            etiqueta_vidas.config(text=f"Te quedan {vidas} vidas.")

        actualizar_tablero()

    def volver_a_jugar():
        """
        Reinicia el juego.
        """
        ventana_juego.destroy()
        ventana_juego()

    ventana_juego = tk.Toplevel()
    ventana_juego.title("Juego del Ahorcado")
    ventana_juego.geometry("500x600")

    etiqueta_tablero = tk.Label(ventana_juego, text=mostrar_tablero(palabra, letras_correctas), font=("Courier", 18))
    etiqueta_tablero.pack(pady=20)

    etiqueta_ahorcado = tk.Label(ventana_juego, text=dibujo_ahorcado(vidas), font=("Courier", 12))
    etiqueta_ahorcado.pack(pady=10)

    etiqueta_vidas = tk.Label(ventana_juego, text=f"Te quedan {vidas} vidas.", font=("Arial", 12))
    etiqueta_vidas.pack(pady=10)

    entrada_letra = tk.Entry(ventana_juego, font=("Arial", 14))
    entrada_letra.pack(pady=10)

    boton_enviar = tk.Button(ventana_juego, text="Enviar", font=("Arial", 12), command=ingresar_letra)
    boton_enviar.pack(pady=10)

    etiqueta_resultado = tk.Label(ventana_juego, text="", font=("Arial", 12))
    etiqueta_resultado.pack(pady=20)

    boton_volver = tk.Button(ventana_juego, text="Volver a jugar", font=("Arial", 12), command=volver_a_jugar)
    boton_volver.pack(pady=10)

    boton_salir = tk.Button(ventana_juego, text="Salir", font=("Arial", 12), command=ventana_juego.destroy)
    boton_salir.pack(pady=10)

    ventana_juego.mainloop()

if __name__ == "__main__":
    ventana_principal()
