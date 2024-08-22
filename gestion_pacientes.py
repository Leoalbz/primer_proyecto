import tkinter as tk
from tkinter import messagebox

# import clientes
ventana = tk.Tk()
ventana.title('Sistema gestor de pacientes')
ventana.geometry('800x600')
titulo = tk.Label(ventana, text= 'Sistema gestor de pacientes', fg='red', font=('Arial', 18))
titulo.pack()
img = tk.PhotoImage(file='background_img.png')
bg_imagen = tk.Label(ventana, image=img)
bg_imagen.place(x=0,y=0,relwidth=1,relheight=1)
#ingreso_pacientes = tk.Entry(ventana)
#ingreso_pacientes.pack()
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
lista_pacientes = tk.Listbox(marco)

def agregar_paciente():
    nombre = tk.StringVar()
    raza = tk.StringVar()
    diagnostico = tk.StringVar()
    tratamiento = tk.StringVar()
    # tarea = ingreso_pacientes.get()
    nombre_paciente = tk.Entry(marco, textvariable=nombre)
    nombre_paciente.pack()
    raza_paciente = tk.Entry(marco, textvariable=raza)
    raza_paciente.pack()
    diagnostico_paciente = tk.Entry(marco, textvariable=diagnostico)
    diagnostico_paciente.pack()
    tratamiento_paciente = tk.Entry(marco, textvariable=tratamiento)
    tratamiento_paciente.pack()
    boton_enviar_datos = tk.Button(marco, text='Enviar datos', command=lambda:agregar_a_la_lista(nombre.get(), raza.get(), diagnostico.get(), tratamiento.get()))
    boton_enviar_datos.pack()
def agregar_a_la_lista(nombre, raza, diagnostico, tratamiento):
    lista_pacientes.insert(tk.END, f'Nombre: {nombre}')
    lista_pacientes.insert(tk.END, f'Raza: {raza}')
    lista_pacientes.insert(tk.END, f'Diagnostico: {diagnostico}')
    lista_pacientes.insert(tk.END, f'Tratamiento: {tratamiento}')
    lista_pacientes.insert(tk.END, '\n')

boton_agregar = tk.Button(ventana, text = 'Agregar paciente', command = agregar_paciente)
boton_agregar.pack()

def eliminar_paciente():
    seleccion = lista_pacientes.curselection()
    if seleccion:
        lista_pacientes.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar paciente', command = eliminar_paciente)
boton_eliminar.pack()

def consultar_paciente():
    #marco = tk.Frame(ventana)
    #marco.pack(padx = 10, pady = 10)
    scrollbar = tk.Scrollbar (marco)
    scrollbar.config(command=lista_pacientes.yview)
    scrollbar .pack(side = tk.RIGHT, fill =tk.Y)
    #lista_pacientes = tk.Listbox(marco, yscrollcommand= scrollbar .set)
    lista_pacientes.config(yscrollcommand=scrollbar.set)
    lista_pacientes.pack()
    #scrollbar .config(command = lista_pacientes.yview)
    for item in lista_pacientes.curselection():
        consulta_paciente = tk.Label(ventana, text=lista_pacientes.get(item)).pack()
boton_consultar = tk.Button(ventana, text = 'Consultar paciente', command = consultar_paciente)
boton_consultar.pack()
ventana.mainloop()