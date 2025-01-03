import tkinter as tk
from tkinter import messagebox

class StudentManager:
    def __init__(self):
        self.students = {}

    def calculate_grade(self, nota):
        if nota < 5:
            return "SS"
        elif 5 <= nota < 7:
            return "AP"
        elif 7 <= nota < 9:
            return "NT"
        else:
            return "SB"

    def add_student(self, dni, apellidos, nombre, nota):
        if dni in self.students:
            raise ValueError("El DNI ya está registrado.")
        grade = self.calculate_grade(nota)
        self.students[dni] = {
            "apellidos": apellidos,
            "nombre": nombre,
            "nota": nota,
            "calificacion": grade
        }

    def remove_student(self, dni):
        if dni not in self.students:
            raise ValueError("El DNI no existe.")
        del self.students[dni]

    def get_student(self, dni):
        if dni not in self.students:
            raise ValueError("El DNI no existe.")
        return self.students[dni]

    def update_nota(self, dni, new_nota):
        if dni not in self.students:
            raise ValueError("El DNI no existe.")
        self.students[dni]["nota"] = new_nota
        self.students[dni]["calificacion"] = self.calculate_grade(new_nota)

    def get_suspensos(self):
        return {dni: student for dni, student in self.students.items() if student["nota"] < 5}

    def get_aprobados(self):
        return {dni: student for dni, student in self.students.items() if student["nota"] >= 5}

    def get_candidates_mh(self):
        return {dni: student for dni, student in self.students.items() if student["nota"] == 10}

# GUI setup
manager = StudentManager()

def add_student():
    try:
        dni = entry_dni.get()
        apellidos = entry_apellidos.get()
        nombre = entry_nombre.get()
        nota = float(entry_nota.get())
        manager.add_student(dni, apellidos, nombre, nota)
        messagebox.showinfo("Éxito", "Alumno añadido correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def remove_student():
    try:
        dni = entry_dni.get()
        manager.remove_student(dni)
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_students():
    all_students = "\n".join(f"{dni} {data['apellidos']}, {data['nombre']} {data['nota']} {data['calificacion']}" for dni, data in manager.students.items())
    messagebox.showinfo("Alumnos", all_students if all_students else "No hay alumnos registrados.")

# Tkinter elements
root = tk.Tk()
root.title("Gestión de Calificaciones")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entry fields
lbl_dni = tk.Label(frame, text="DNI")
lbl_dni.grid(row=0, column=0)
entry_dni = tk.Entry(frame)
entry_dni.grid(row=0, column=1)

lbl_apellidos = tk.Label(frame, text="Apellidos")
lbl_apellidos.grid(row=1, column=0)
entry_apellidos = tk.Entry(frame)
entry_apellidos.grid(row=1, column=1)

lbl_nombre = tk.Label(frame, text="Nombre")
lbl_nombre.grid(row=2, column=0)
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=2, column=1)

lbl_nota = tk.Label(frame, text="Nota")
lbl_nota.grid(row=3, column=0)
entry_nota = tk.Entry(frame)
entry_nota.grid(row=3, column=1)

# Buttons
btn_add = tk.Button(frame, text="Añadir Alumno", command=add_student)
btn_add.grid(row=4, column=0, pady=5)

btn_remove = tk.Button(frame, text="Eliminar Alumno", command=remove_student)
btn_remove.grid(row=4, column=1, pady=5)

btn_show = tk.Button(frame, text="Mostrar Alumnos", command=show_students)
btn_show.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
