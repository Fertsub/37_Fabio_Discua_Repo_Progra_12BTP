from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
window.title("Taquilla Cinepolis Plus")
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

pelicula = StringVar()
hora = StringVar()
fecha = StringVar()
idioma = StringVar()

def show_data():
    pelicula = entry_sala.get()
    hora = entry_butaka.get()
    fecha = entry_boletos.get()
    idioma = entry_precio.get()
    print(sala)
    print(hora)
    print(fecha)
    print(idioma)

def crear_sala():
    pelicula = entry_pelicula.get()
    hora = entry_hora.get()
    fecha = entry_fecha.get()
    idioma = entry_idioma.get()
    
    DB_CINE = cine_database.MyDatabase()
    data = (pelicula, hora, fecha, idioma)
    print(data)
    DB_CINE.insert_db(pelicula, hora, fecha, idioma)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_salas = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_salas.place(x=25, y=30)
label_pelicula = Label(frame_salas, 
              text="Película:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_pelicula.place(x=20, y=60)
entry_pelicula = Entry(frame_salas, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_pelicula.place(x=20, y=100)
label_hora= Label(frame_salas, 
              text="Hora:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_hora.place(x=20, y=130)
entry_hora= Entry(frame_salas, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_hora.place(x=20, y=170)
label_fecha = Label(frame_salas, 
              text="Fecha:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_fecha.place(x=20, y=200)
entry_fecha = Entry(frame_salas, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_fecha.place(x=20, y=240)
label_idioma = Label(frame_salas, 
              text="Idioma:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_idioma.place(x=20, y=270)
entry_idioma = Entry(frame_salas, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_idioma.place(x=20, y=310)

button_crear_sala = Button(frame_salas, text="Crear Sala", font=("Calibri", "14", "bold"), command=crear_sala)
button_crear_sala.place(x=20, y=370)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Cartelera",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="Cinepolis Plus", 
              font=("Calibri", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="¡Bienvenido(a)!", 
              font=("Calibri", "18"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()