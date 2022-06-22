import tkinter as tk
import argparse
from time import sleep
from random import shuffle
########## VENTANA PRINCIPAL ##########

ventana = tk.Tk()
ventana.title("Fixture")
ventana.geometry("400x500+700+100")
ventana.minsize(width=600, height=600)
ventana.configure(bg="lightblue")

########## FUNCIONES ##########

def agregar():
        part = entrada_participante.get() + '\n'
        archivo = open("example.txt", 'a')
        archivo.write(part)
        print(part)
        archivo.close()
        entrada_participante.config(state='disabled')
        boton_agregar.config(state='disabled')

def borrar():
    entrada_participante.config(state='normal')
    boton_agregar.config(state='normal')
    entrada_participante.delete(0,tk.END)

def crearFixture():
    import fixtureLeeTxt

########## ROTULO DEL TITULO ##########

rotulo_titulo = tk.Label(ventana,
                         text="INGRESO PARTICIPANTES",
                         bg="lightblue", fg="black",
                         font="consolas 20 bold",
                         relief=tk.GROOVE, bd=2,
                         padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

########## CUADRO PRIMERO ##########

cuadro1 = tk.Frame(ventana,
                   bg="lightblue")

rotulo_part = tk.Label(cuadro1,
                          text="PARTICIPANTES:",
                          bg="lightblue",
                          font="consolas 18 bold",
                          width=12,
                          anchor=tk.W)
rotulo_part.pack(side=tk.LEFT, padx=10, pady=10)

entrada_participante = tk.Entry(cuadro1,
                          bg="white", fg="black",
                          font="consolas 18 bold",
                          relief=tk.SUNKEN,
                          width=10,
                          justify=tk.RIGHT,
                          state="normal")
entrada_participante.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack(pady=10)

############ BOTONES #################
cuadro3 = tk.Frame(ventana,
                   bg="lightblue")

boton_borrar = tk.Button(cuadro3,
                 text="Borrar",
                 bg="grey",
                 font="consolas 18 bold",
                 width=10,
                command=borrar)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=2)

boton_agregar = tk.Button(cuadro3,
                        text="Agregar",
                        bg="orange",
                        font="consolas 18 bold",
                        width=10,
                        state="normal",
                       command=agregar)
boton_agregar.pack(side=tk.LEFT, padx=20, pady=20)

boton_crear = tk.Button(cuadro3,
                        text="Fixture",
                        bg="orange",
                        font="consolas 18 bold",
                        width=30,
                        state="normal",
                       command=crearFixture)
boton_crear.pack(side=tk.LEFT, padx=50, pady=5)

cuadro3.pack(pady=30)

entrada_participante.focus()

##### BUCLE PRINCIPAL #####

ventana.mainloop()