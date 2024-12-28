import sys
from pathlib import Path
from tkinter import Tk, Button, Entry, END, PhotoImage
from tkinter import messagebox, ttk, filedialog, colorchooser
from PIL import Image, ImageTk

def ruta_relativa_ac(imagen_borrar):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\AC.png').resolve())

def ruta_relativa_divi(imagen_divi):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\divi.png').resolve())

def ruta_relativa_multi(imagen_multi):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\multi.png').resolve())

def ruta_relativa_resta(imagen_resta):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\resta.png').resolve())

def ruta_relativa_suma(imagen_suma):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\suma.png').resolve())

def ruta_relativa_parent1(imagen_parent1):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\paren1.png').resolve())

def ruta_relativa_paren2(imagen_parent2):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\paren2.png').resolve())

def ruta_relativa_punto(imagen_punto):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\punto.png').resolve())

def ruta_relativa_igual(imagen_igual):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\igual.png').resolve())

def ruta_relativa_0(imagen_boton_0):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\0.png').resolve())

def ruta_relativa_1(imagen_boton_1):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\1.png').resolve())

def ruta_relativa_2(imagen_boton_2):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\2.png').resolve())

def ruta_relativa_3(imagen_boton_3):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\3.png').resolve())

def ruta_relativa_4(imagen_boton_4):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\4.png').resolve())

def ruta_relativa_5(imagen_boton_5):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\5.png').resolve())

def ruta_relativa_6(imagen_boton_6):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\6.png').resolve())

def ruta_relativa_7(imagen_boton_7):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\7.png').resolve())

def ruta_relativa_8(imagen_boton_8):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\8.png').resolve())

def ruta_relativa_9(imagen_boton_9):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\9.png').resolve())

def ruta_relativa_parent1(imagen_parent1):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\paren1.png').resolve())

def ruta_relativa_parent2(imagen_parent2):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\paren2.png').resolve())

def ruta_relativa_0(imagen_boton_0):
    return str(Path('C:\\Users\\Mario Meza\\Desktop\\DeberesProgramacion\\CalculadoraB\\dist\\0.png').resolve())


    

# Configuración de la raíz
ventana= Tk()
ventana.title("Calculadora MarioMeza")
e_texto= Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

imagen_borrar= Image.open("AC.png")
ancho, alto= 50, 50
imagen_borrar_redimensionada= imagen_borrar.resize((ancho, alto), Image.LANCZOS)
ima_boton_borrar= ImageTk.PhotoImage(imagen_borrar_redimensionada)

imagen_parent1= Image.open("paren1.png")
ancho, alto= 50, 50
imagen_parent1_redimensionada= imagen_parent1.resize((ancho, alto), Image.LANCZOS)
ima_boton_parent1= ImageTk.PhotoImage(imagen_parent1_redimensionada)

imagen_parent2= Image.open("paren2.png")
ancho, alto= 50, 50
imagen_parent2_redimensionada= imagen_parent2.resize((ancho, alto), Image.LANCZOS)
ima_boton_parent2= ImageTk.PhotoImage(imagen_parent2_redimensionada)

imagen_suma= Image.open("suma.png")
ancho, alto= 50, 50
imagen_suma_redimensionada= imagen_suma.resize((ancho, alto), Image.LANCZOS)
ima_boton_suma= ImageTk.PhotoImage(imagen_suma_redimensionada)

imagen_resta= Image.open("resta.png")
ancho, alto= 50, 50
imagen_resta_redimensionada= imagen_resta.resize((ancho, alto), Image.LANCZOS)
ima_boton_resta= ImageTk.PhotoImage(imagen_resta_redimensionada)

imagen_multi= Image.open("multi.png")
ancho, alto= 50, 50
imagen_multi_redimensionada= imagen_multi.resize((ancho, alto), Image.LANCZOS)
ima_boton_multi= ImageTk.PhotoImage(imagen_multi_redimensionada)

imagen_divi= Image.open("divi.png")
ancho, alto= 50, 50
imagen_divi_redimensionada= imagen_divi.resize((ancho, alto), Image.LANCZOS)
ima_boton_divi= ImageTk.PhotoImage(imagen_divi_redimensionada)

imagen_punto= Image.open("punto.png")
ancho, alto= 50, 50
imagen_punto_redimensionada= imagen_punto.resize((ancho, alto), Image.LANCZOS)
ima_boton_punto= ImageTk.PhotoImage(imagen_punto_redimensionada)

imagen_igual= Image.open("igual.png")
ancho, alto= 50, 50
imagen_igual_redimensionada= imagen_igual.resize((ancho, alto), Image.LANCZOS)
ima_boton_igual= ImageTk.PhotoImage(imagen_igual_redimensionada)

imagen_boton_1= Image.open("1.png")
ancho, alto= 50, 50
imagen_boton_1_redimensionada= imagen_boton_1.resize((ancho, alto), Image.LANCZOS)
ima_boton_1= ImageTk.PhotoImage(imagen_boton_1_redimensionada)

imagen_boton_2= Image.open("2.png")
ancho, alto= 50, 50
imagen_boton_2_redimensionada= imagen_boton_2.resize((ancho, alto), Image.LANCZOS)
ima_boton_2= ImageTk.PhotoImage(imagen_boton_2_redimensionada)

imagen_boton_3= Image.open("3.png")
ancho, alto= 50, 50
imagen_boton_3_redimensionada= imagen_boton_3.resize((ancho, alto), Image.LANCZOS)
ima_boton_3= ImageTk.PhotoImage(imagen_boton_3_redimensionada)

imagen_boton_4= Image.open("4.png")
ancho, alto= 50, 50
imagen_boton_4_redimensionada= imagen_boton_4.resize((ancho, alto), Image.LANCZOS)
ima_boton_4= ImageTk.PhotoImage(imagen_boton_4_redimensionada)

imagen_boton_5= Image.open("5.png")
ancho, alto= 50, 50
imagen_boton_5_redimensionada= imagen_boton_5.resize((ancho, alto), Image.LANCZOS)
ima_boton_5= ImageTk.PhotoImage(imagen_boton_5_redimensionada)

imagen_boton_6= Image.open("6.png")
ancho, alto= 50, 50
imagen_boton_6_redimensionada= imagen_boton_6.resize((ancho, alto), Image.LANCZOS)
ima_boton_6= ImageTk.PhotoImage(imagen_boton_6_redimensionada)

imagen_boton_7= Image.open("7.png")
ancho, alto= 50, 50
imagen_boton_7_redimensionada= imagen_boton_7.resize((ancho, alto), Image.LANCZOS)
ima_boton_7= ImageTk.PhotoImage(imagen_boton_7_redimensionada)

imagen_boton_8= Image.open("8.png")
ancho, alto= 50, 50
imagen_boton_8_redimensionada= imagen_boton_8.resize((ancho, alto), Image.LANCZOS)
ima_boton_8= ImageTk.PhotoImage(imagen_boton_8_redimensionada)

imagen_boton_9= Image.open("9.png")
ancho, alto= 50, 50
imagen_boton_9_redimensionada= imagen_boton_9.resize((ancho, alto), Image.LANCZOS)
ima_boton_9= ImageTk.PhotoImage(imagen_boton_9_redimensionada)

imagen_boton_0= Image.open("0.png")
ancho, alto= 120, 50
imagen_boton_0_redimensionada= imagen_boton_0.resize((ancho, alto), Image.LANCZOS)
ima_boton_0= ImageTk.PhotoImage(imagen_boton_0_redimensionada)

#Funciones

def click_boton(valor):
    texto_actual= e_texto.get()
    e_texto.delete(0, END)
    e_texto.insert(0, texto_actual + str(valor))

def evaluar():
    try:
        ecuacion= e_texto.get()
        resultado= eval(ecuacion)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
    except:
        messagebox.showerror("Error", "Ecuación Incorrecta")
        e_texto.delete(0, END)


#Vamos a Crear Los Botones
boton1= Button(ventana, image=ima_boton_1, compound="top", command=lambda: click_boton(1))
boton2= Button(ventana, image=ima_boton_2, compound="top", command=lambda: click_boton(2))
boton3= Button(ventana, image=ima_boton_3, compound="top", command=lambda: click_boton(3))
boton4= Button(ventana, image=ima_boton_4, compound="top", command=lambda: click_boton(4))
boton5= Button(ventana, image=ima_boton_5, compound="top", command=lambda: click_boton(5))
boton6= Button(ventana, image=ima_boton_6, compound="top", command=lambda: click_boton(6))
boton7= Button(ventana, image=ima_boton_7, compound="top", command=lambda: click_boton(7))
boton8= Button(ventana, image=ima_boton_8, compound="top", command=lambda: click_boton(8))
boton9= Button(ventana, image=ima_boton_9, compound="top", command=lambda: click_boton(9))
boton0= Button(ventana, image=ima_boton_0, compound="top", command=lambda: click_boton(0))

boton_borrar= Button(ventana, image=ima_boton_borrar, compound="top", command=lambda: e_texto.delete(0, END))
boton_parent1= Button(ventana, image=ima_boton_parent1, compound="top", command=lambda: click_boton("("))
boton_parent2= Button(ventana, image=ima_boton_parent2, compound="top", command=lambda: click_boton(")"))
boton_punto= Button(ventana, image=ima_boton_punto, compound="top", command=lambda: click_boton("."))

boton_div= Button(ventana, image=ima_boton_divi, compound="top", command=lambda: click_boton("/")) 
boton_mult= Button(ventana, image=ima_boton_multi, compound="top", command=lambda: click_boton("*"))    
boton_sum= Button(ventana, image=ima_boton_suma, compound="top", command=lambda: click_boton("+"))
boton_res= Button(ventana, image=ima_boton_resta, compound="top", command=lambda: click_boton("-")) 
boton_igual= Button(ventana, image=ima_boton_igual, compound="top", command=lambda: evaluar())

#Agregar Botones en Pantalla

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parent1.grid(row=1, column=1, padx=5, pady=5)
boton_parent2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)
boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)
boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)
boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_res.grid(row=4, column=3, padx=5, pady=5)
boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


   

    
ventana.mainloop()