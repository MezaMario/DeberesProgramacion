import random
import tkinter as tk
from tkinter import messagebox

class Juego:
    def __init__(self):
        self.opciones = ["Piedra", "Papel", "Tijera"]

    def jugar(self, jugador):
        computadora = random.choice(self.opciones)
        if jugador == computadora:
            return f"Empate. Ambos eligieron {computadora}"
        elif (jugador == "Piedra" and computadora == "Tijera") or \
             (jugador == "Papel" and computadora == "Piedra") or \
             (jugador == "Tijera" and computadora == "Papel"):
            return f"Ganaste. Computadora eligió {computadora}"
        else:
            return f"Perdiste. Computadora eligió {computadora}"

class InterfazGrafica:
    def __init__(self, root):
        self.juego = Juego()
        self.root = root
        self.root.title("Juego Piedra, Papel o Tijera")
        self.root.geometry("260x160")
        self.root.configure(bg="blue")

        # Etiqueta de instrucciones
        self.label = tk.Label(root, text="Elige una opción:", font=("Calibri", 14), bg="blue", fg="white")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Botones
        self.boton_piedra = tk.Button(root, text="Piedra", font=("Calibri", 12), command=lambda: self.jugar("Piedra"))
        self.boton_papel = tk.Button(root, text="Papel", font=("Calibri", 12), command=lambda: self.jugar("Papel"))
        self.boton_tijera = tk.Button(root, text="Tijera", font=("Calibri", 12), command=lambda: self.jugar("Tijera"))

        self.boton_piedra.grid(row=1, column=0, padx=20, pady=20)
        self.boton_papel.grid(row=1, column=1, padx=20, pady=20)
        self.boton_tijera.grid(row=1, column=2, padx=20, pady=20)

        # Etiqueta final
        self.label2 = tk.Label(root, text="Gracias por jugar", font=("Arial", 14), bg="blue", fg="white")
        self.label2.grid(row=2, column=0, columnspan=3, pady=10)

    def jugar(self, eleccion):
        resultado = self.juego.jugar(eleccion)
        messagebox.showinfo("Resultado", resultado)

# Configuración principal
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
