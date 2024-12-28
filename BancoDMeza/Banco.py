import tkinter as tk
from tkinter import messagebox, Button, Label, PhotoImage, filedialog
from PIL  import Image, ImageTk, ImageDraw


class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.transacciones = []
                 

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.transacciones.append(f"Depósito: +{monto}")
            return True
        else:
            return False

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(f"Retiro: -{monto}")
            return True
        else:
            return False

    def transferir(self, monto, cuenta_destino):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            cuenta_destino.depositar(monto)
            self.transacciones.append(f"Transferencia a {cuenta_destino.numero_cuenta}: -{monto}")
            return True
        else:
            return False

class GestorUsuarios:
    MAX_USUARIOS = 5

    def __init__(self):
        self.usuarios = {}
        self.cuentas = {}

    def crear_usuario(self, cedula, usuario, contrasena):
        if len(self.usuarios) >= self.MAX_USUARIOS:
            return "No se pueden agregar más usuarios."

        if not cedula.isdigit() or len(cedula) != 10:
            return "La cédula debe tener 10 dígitos."

        if usuario in self.usuarios:
            return "El usuario ya existe."

        self.usuarios[usuario] = {"cedula": cedula, "contrasena": contrasena}
        self.cuentas[usuario] = CuentaBancaria(numero_cuenta=usuario, titular=usuario, saldo=0, tipo_cuenta="Ahorro")
        return "Usuario creado con éxito."

    def validar_usuario(self, usuario, contrasena):
        if usuario in self.usuarios and self.usuarios[usuario]["contrasena"] == contrasena:
            return True
        return False

    def obtener_cuenta(self, usuario):
        return self.cuentas.get(usuario, None)

class InterfazBanco:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco Internacional Meza")
        self.root.geometry("350x550")
        imagen= Image.open("bank.png")
        imagen= imagen.resize((100, 100))
        self.imagen= ImageTk.PhotoImage(imagen)
        root.configure(bg="lightblue")
        self.imagen_usuario = None

        self.gestor_usuarios = GestorUsuarios()
        self.usuario_actual = None

        self.mostrar_pantalla_login()

    def mostrar_pantalla_login(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 16), bg="Green").pack(pady=10)

        tk.Label(self.root, text="Usuario:").pack(pady=5)
        usuario_entry = tk.Entry(self.root)
        usuario_entry.pack(pady=5)

        tk.Label(self.root, text="Contraseña:").pack(pady=5)
        contrasena_entry = tk.Entry(self.root, show="*")
        contrasena_entry.pack(pady=5)
        
        label_imagen= tk.Label(self.root, image= self.imagen)
        label_imagen.pack(pady=20)

        def validar_login():
            usuario = usuario_entry.get()
            contrasena = contrasena_entry.get()
            if self.gestor_usuarios.validar_usuario(usuario, contrasena):
                self.usuario_actual = usuario
                messagebox.showinfo("Login Exitoso", "Bienvenido al sistema.")
                self.mostrar_pantalla_principal()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

        tk.Button(self.root, text="Iniciar Sesión", command=validar_login).pack(pady=10)
        tk.Button(self.root, text="Crear Usuario", command=self.mostrar_gestion_usuarios).pack(pady=10)

    def mostrar_pantalla_principal(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Menú Principal", font=("Arial", 16)).pack(pady=10)
 
              
        imaBoton= Image.open("cons.png")
        ima_bot= imaBoton.resize((50,50))
        self.imagen_boton= ImageTk.PhotoImage(ima_bot)
        
        imaBoton1= Image.open("depo.png")
        ima_bot1= imaBoton1.resize((50,50))
        self.imagen_boton1= ImageTk.PhotoImage(ima_bot1)
        
        imaBoton2= Image.open("reti.png")
        ima_bot2= imaBoton2.resize((50,50))
        self.imagen_boton2= ImageTk.PhotoImage(ima_bot2)
        
        imaBoton3= Image.open("transf.png")
        ima_tran= imaBoton3.resize((50,50))
        self.imagen_transfe= ImageTk.PhotoImage(ima_tran)
        
        imaBoton4= Image.open("salir.png")
        ima_sal= imaBoton4.resize((50,50))
        self.imagen_salir= ImageTk.PhotoImage(ima_sal)
        
        self.boton_foto_usuario= tk.Button(self.root, text="Añadir Foto", command= self.agregar_foto_usuario)
        self.boton_foto_usuario.pack(pady=10)
        
        tk.Button(self.root, image=self.imagen_boton, text="Consultar Saldo", compound="top", command=self.mostrar_saldo).pack(pady=5)
        tk.Button(self.root, image=self.imagen_boton1, text="Depositar", compound="top", command=self.mostrar_ventana_deposito).pack(pady=5)
        tk.Button(self.root, image=self.imagen_boton2, text="Retirar", compound="top", command=self.mostrar_ventana_retiro).pack(pady=5)
        tk.Button(self.root, image=self.imagen_transfe, text="Transferir", compound="top", command=self.mostrar_ventana_transferencia).pack(pady=5)
        tk.Button(self.root, image=self.imagen_salir, text="Cerrar Sesión", compound="top", command=self.mostrar_pantalla_login).pack(pady=5)

    def mostrar_gestion_usuarios(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Crear Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Ingrese cédula (10 dígitos):").pack(pady=5)
        cedula_entry = tk.Entry(self.root)
        cedula_entry.pack(pady=5)

        tk.Label(self.root, text="Ingrese usuario:").pack(pady=5)
        usuario_entry = tk.Entry(self.root)
        usuario_entry.pack(pady=5)

        tk.Label(self.root, text="Ingrese contraseña:").pack(pady=5)
        contrasena_entry = tk.Entry(self.root, show="*")
        contrasena_entry.pack(pady=5)

        def crear_usuario():
            cedula = cedula_entry.get()
            usuario = usuario_entry.get()
            contrasena = contrasena_entry.get()
            resultado = self.gestor_usuarios.crear_usuario(cedula, usuario, contrasena)
            messagebox.showinfo("Gestor de Usuarios", resultado)
            if "éxito" in resultado:
                self.mostrar_pantalla_login()

        tk.Button(self.root, text="Crear Usuario", command=crear_usuario).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_pantalla_login).pack(pady=5)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def agregar_foto_usuario(self):
        ruta_imagen= filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")]
        )
        if not ruta_imagen:
            return
        
        imagen_original= Image.open(ruta_imagen).resize((100, 100))
        mascarilla= Image.new("L", (100, 100), 0)
        draw= ImageDraw.Draw(mascarilla)
        draw.ellipse((0, 0, 100, 100), fill=255)
        imagen_redonda= Image.new("RGBA",(100, 100))
        imagen_redonda.paste(imagen_original, (0, 0), mask=mascarilla)
        
        self.imagen_usuario= ImageTk.PhotoImage(imagen_redonda)
        
        self.boton_foto_usuario.config(image= self.imagen_usuario, text="")
        

    def mostrar_saldo(self):
        cuenta = self.gestor_usuarios.obtener_cuenta(self.usuario_actual)
        if cuenta:
            saldo = cuenta.consultar_saldo()
            messagebox.showinfo("Saldo Disponible", f"El saldo de la cuenta es: ${saldo}")

    def mostrar_ventana_deposito(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Depositar Dinero", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Monto a depositar:").pack(pady=5)
        monto_entry = tk.Entry(self.root)
        monto_entry.pack(pady=5)

        def depositar():
            monto = float(monto_entry.get())
            cuenta = self.gestor_usuarios.obtener_cuenta(self.usuario_actual)
            if cuenta and cuenta.depositar(monto):
                messagebox.showinfo("Depósito", "Depósito realizado con éxito.")
                self.mostrar_pantalla_principal()
            else:
                messagebox.showerror("Error", "Monto inválido.")

        tk.Button(self.root, text="Depositar", command=depositar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_pantalla_principal).pack(pady=5)

    def mostrar_ventana_retiro(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Retirar Dinero", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Monto a retirar:").pack(pady=5)
        monto_entry = tk.Entry(self.root)
        monto_entry.pack(pady=5)

        def retirar():
            monto = float(monto_entry.get())
            cuenta = self.gestor_usuarios.obtener_cuenta(self.usuario_actual)
            if cuenta and cuenta.retirar(monto):
                messagebox.showinfo("Retiro", "Retiro realizado con éxito.")
                self.mostrar_pantalla_principal()
            else:
                messagebox.showerror("Error", "Saldo insuficiente o monto inválido.")

        tk.Button(self.root, text="Retirar", command=retirar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_pantalla_principal).pack(pady=5)

    def mostrar_ventana_transferencia(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Transferir Dinero", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Usuario destino:").pack(pady=5)
        usuario_destino_entry = tk.Entry(self.root)
        usuario_destino_entry.pack(pady=5)

        tk.Label(self.root, text="Monto a transferir:").pack(pady=5)
        monto_entry = tk.Entry(self.root)
        monto_entry.pack(pady=5)

        def transferir():
            usuario_destino = usuario_destino_entry.get()
            monto = float(monto_entry.get())
            cuenta_origen = self.gestor_usuarios.obtener_cuenta(self.usuario_actual)
            cuenta_destino = self.gestor_usuarios.obtener_cuenta(usuario_destino)

            if cuenta_origen and cuenta_destino:
                if cuenta_origen.transferir(monto, cuenta_destino):
                    messagebox.showinfo("Transferencia", "Transferencia realizada con éxito.")
                    self.mostrar_pantalla_principal()
                else:
                    messagebox.showerror("Error", "Saldo insuficiente o monto inválido.")
            else:
                messagebox.showerror("Error", "Usuario destino no encontrado.")

        tk.Button(self.root, text="Transferir", command=transferir).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_pantalla_principal).pack(pady=5)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBanco(root)
    root.mainloop()