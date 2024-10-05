from tkinter import *
from tkinter import messagebox

#Definicion de las funciones
def Enviar_Datos():
    try:
        nombre = entry_Nombre.get()
        apellido = entry_apellido.get()
        dni = entry_dni.get()

        if not nombre or not apellido or not dni:
            messagebox.showwarning("Advertencia","Por favor complete todos los campos")
            return

        archivo_Nombres = open("Nombres.txt","a")
        archivo_Nombres.write(nombre + '\n')

        archivo_apellido = open("Apellidos.txt","a")
        archivo_apellido.write(apellido + '\n')

        archivo_dni = open("DNI.txt","a")
        archivo_dni.write(dni + '\n')

        messagebox.showinfo("Informacion","Datos Cargados Correctamente")
        entry_Nombre.delete(0,END)
        entry_apellido.delete(0,END)
        entry_dni.delete(0,END)
    except:
        messagebox.showerror("Advertencia!","Se a producido un error al cargar los datos")

def Buscar_Datos():
    dni = entry_dni.get()

    Archivo_DNI = open("DNI.txt","r")
    Lista_DNI = Archivo_DNI.readlines()
    Archivo_Nombres = open("Nombres.txt","r")
    Lista_Nombres = Archivo_Nombres.readlines()
    Archivo_Apellido = open("Apellidos.txt","r")
    Lista_Apellidos = Archivo_Apellido.readlines()

    if dni + '\n' in Lista_DNI:
        i = Lista_DNI.index(dni + '\n')
        nombre = Lista_Nombres[i]
        apellido = Lista_Apellidos[i]

        entry_Nombre.insert(0,nombre)
        entry_apellido.insert(0,apellido)
    else:
        messagebox.showwarning("Advertencia","usuario no encontrado")
        entry_Nombre.delete(0,END)
        entry_apellido.delete(0,END)
        entry_dni.delete(0,END)

        

#Creacion de la interfaz grafica
root = Tk()
root.title("Script De Prueba")
root.geometry("300x400")
root.resizable(0,0)


Titulo = Label(root,text="Carga De Usuarios",font=("Verdana",15))
Titulo.place(x=60,y=40)

label_Nombre = Label(root,text="Nombre",font=("Verdana",10))
label_Nombre.place(x=40,y=100)

label_apellido = Label(root,text="Apellido",font=("Verdana",10))
label_apellido.place(x=40,y=130)

label_DNI = Label(root,text="DNI",font=("Verdana",10))
label_DNI.place(x=50,y=155)

entry_Nombre = Entry(root)
entry_Nombre.place(x=100,y=100)

entry_apellido = Entry(root)
entry_apellido.place(x=100,y=130)

entry_dni = Entry(root)
entry_dni.place(x=100,y=155)

boton_enviar = Button(root,text="Enviar",height=2,width=10,command=Enviar_Datos)
boton_enviar.place(x=120,y=190)

boton_buscar = Button(root,text="Buscar",height=2,width=10,command=Buscar_Datos)
boton_buscar.place(x=120,y=240)


root.mainloop()