import clientes as cl
import tkinter as tk
from tkinter import messagebox

pacientes = cl.lista_pacientes()

#funciones de los botones
def agregar_pacientes():
    id_paciente = id_entry.get()
    nombre = nombre_entry.get()
    raza = raza_entry.get()
    edad = edad_entry.get()
    diagnostico = diagnostico_text.get("1.0", tk.END).strip()
    tratamiento = tratamiento_text.get("1.0", tk.END).strip()

    nuevo_paciente = cl.paciente(id_paciente, nombre, raza, edad, diagnostico, tratamiento)
    pacientes.agregar_paciente(nuevo_paciente)

    messagebox.showinfo("Información", "Paciente agregado exitosamente")

    # Limpiar los campos
    id_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    raza_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    diagnostico_text.delete("1.0", tk.END)
    tratamiento_text.delete("1.0", tk.END)

def mostrar_pacientes():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Lista de Pacientes")
    nueva_ventana.geometry("800x600")

    text_lista = tk.Text(nueva_ventana, wrap=tk.WORD, height=20, width=80)
    text_lista.pack(pady=10)
   
    pacientes_texto = pacientes.mostrar_pacientes()
    text_lista.insert(tk.END, pacientes_texto)

    label = tk.Label(nueva_ventana, text="Lista de Pacientes", font=("Arial",14))
    label.pack(pady=10)

    tk.Label(nueva_ventana, text="Eliminar Paciente").pack(pady=5)
    id_eliminar_entry = tk.Entry(nueva_ventana)
    id_eliminar_entry.pack(pady=5)

    def eliminar_paciente():
        id_paciente = id_eliminar_entry.get()
        if id_paciente:
            pacientes.eliminar_paciente(id_paciente)
            messagebox.showinfo("Información", f"Paciente con ID {id_paciente} eliminado")
            id_eliminar_entry.delete(0, tk.END)
            text_lista.delete("1.0", tk.END)
            paciente_texto = pacientes.mostrar_pacientes()
            text_lista.insert(tk.END, paciente_texto)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de paciente.")

    tk.Button(nueva_ventana, text="Eliminar Paciente", command=eliminar_paciente).pack(pady=10)

# ventana principal
ventana = tk.Tk()
ventana.title('Sistema gestor de pacientes')
ventana.geometry('800x600')

icono = tk.PhotoImage(file="icono-vet.png")
ventana.iconphoto(False, icono)

# boton de cierre de ventana 
ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)

titulo = tk.Label(ventana, text= 'Sistema gestor de pacientes', fg='red', font=('Arial', 12))
titulo.pack(pady=10)

img = tk.PhotoImage(file='background_img.png')
bg_imagen = tk.Label(ventana, image=img)
bg_imagen.place(x=0,y=180,relwidth=1,relheight=1)


# campos de entrada de datos
tk.Label(ventana, text="Id:").place(x=50, y=50)
id_entry = tk.Entry(ventana)
id_entry.place(x=150, y=50, width=150)

tk.Label(ventana, text="Nombre:").place(x=50, y=80)
nombre_entry = tk.Entry(ventana)
nombre_entry.place(x=150, y=80, width=150)

tk.Label(ventana, text="Raza:").place(x=50, y=110)
raza_entry = tk.Entry(ventana)
raza_entry.place(x=150, y=110, width=150)

tk.Label(ventana, text="Años:").place(x=50, y=140)
edad_entry = tk.Entry(ventana)
edad_entry.place(x=150, y=140, width=150)

tk.Label(ventana, text="Diagnostico:").place(x=50, y=170)
diagnostico_text = tk.Text(ventana, height=4, width=40)
diagnostico_text.place(x=150, y=170)

tk.Label(ventana, text="Tratamiento:").place(x=50, y=270)
tratamiento_text = tk.Text(ventana, height=4, width=40)
tratamiento_text.place(x=150, y=270)

tk.Button(ventana, text="Añadir Paciente", command=agregar_pacientes).place(x=120, y=350)
tk.Button(ventana, text="Mostrar Lista", command=mostrar_pacientes).place(x=280, y=350)

ventana.mainloop()