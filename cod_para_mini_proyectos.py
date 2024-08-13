"""# Proyecto 1: Menú desplegable
import tkinter as tk
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Opciones', menu=submenu)
submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Opción 2')
ventana.mainloop() """

"""# Proyecto 2: Reloj simple
import tkinter as tk
import time
ventana = tk.Tk()
ventana.title('Reloj simple')
ventana.geometry('400x200')
reloj = tk.Label(ventana, font =
('Arial', 60), bg = 'blue', fg = 'white')
def hora():
    tiempo_actual =time.strftime('%H:%M')
    reloj.config(text = tiempo_actual)
ventana.after(1000, hora)
reloj.pack(anchor = 'center')
hora()
ventana.mainloop() """

"""# Proyecto 3: Barra de desplazamiento
import tkinter as tk
ventana = tk.Tk()
ventana.title('Barra de desplazamiento' )
ventana.geometry ('400x200' )
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill =tk.Y)
lista = tk.Listbox(marco, yscrollcommand= scrollbar .set)
for i in range(100):
        lista.insert(tk.END, f'Elemento{i+1}')
lista.pack(side = tk.LEFT, fill =tk.BOTH)
scrollbar .config(command = lista.yview)
ventana.mainloop () """

"""# Proyecto 4: Lista de tareas
import tkinter as tk
ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('400x200')
ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()
lista_tareas = []
def agregar_tarea():
    tarea = ingreso_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
    ingreso_tarea.delete(0, tk.END)
boton_agregar = tk.Button(ventana, text = 'Agregar tarea', command = agregar_tarea)
boton_agregar.pack()
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
boton_eliminar = tk.Button(ventana, text = 'Eliminar tarea', command = eliminar_tarea)
boton_eliminar.pack()
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()
ventana.mainloop() """