from time import sleep
from ListaDoble import ListaDoble
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

lista_sistemas = ListaDoble()
lista_mensajes = ListaDoble()
lista_drones = ListaDoble()

test = False

if test:
    path = "C:\\Users\\entradaV3.xml"
    response = lista_sistemas.leerArchivo(path)
    lista_drones = response["lista_drones"]
    lista_mensajes = response["lista_mensajes"]
    lista_mensajes.analizar(lista_sistemas)
    lista_mensajes.generarXML()


def cargar_archivo():
    global lista_sistemas
    global lista_mensajes
    global lista_drones

    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        response = lista_sistemas.leerArchivo(ruta_archivo)
        lista_drones = response["lista_drones"]
        lista_mensajes = response["lista_mensajes"]
        lista_mensajes.analizar(lista_sistemas)
        lista_mensajes.generarXML()
        messagebox.showinfo("Cargar Archivo", f"Archivo seleccionado: {ruta_archivo}")


def generar_archivo():
    # open file respuesta.xml
    file = "respuesta.xml"
    if os.name == "nt":
        os.system(f"start {file}")

    messagebox.showinfo("Generar XML", "Generando un nuevo archivo...")


def listar_sistemas():
    global lista_sistemas
    marco_dashboard.pack_forget()
    marco_lista_sistemas.pack()

    for widget in marco_lista_sistemas.winfo_children():
        widget.destroy()

    etiqueta_nombre_sistema = ttk.Label(
        marco_lista_sistemas, text="Sistemas:", font=("Helvetica", 10)
    )
    boton_volver_dashboard3 = ttk.Button(
    marco_lista_sistemas, text="Volver al Tablero", command=mostrar_dashboard
    )

    boton_volver_dashboard3.pack(pady=10)

    etiqueta_nombre_sistema.pack(pady=10)
    actual = lista_sistemas.primero
    while actual:
        etiqueta_sistema = ttk.Label(
            marco_lista_sistemas, text=f"{actual.dato.nombre}", font=("Helvetica", 10)
        )
        etiqueta_sistema.pack()
        etiqueta_sistema_alturas = ttk.Label(
            marco_lista_sistemas,
            text=f"Alturas: {actual.dato.altura}",
            font=("Helvetica", 8),
        )

        etiqueta_sistema_alturas.pack()
        etiqueta_sistema_cantidad = ttk.Label(
            marco_lista_sistemas,
            text=f"Cantidad: {actual.dato.cantidad}",
            font=("Helvetica", 8),
        )

        etiqueta_sistema_cantidad.pack()

        actual2 = actual.dato.drones.primero
        while actual2:
            etiqueta_dron = ttk.Label(
                marco_lista_sistemas,
                text=f"Dron: {actual2.dato.nombre}",
                font=("Helvetica", 8),
            )
            etiqueta_dron.pack(padx=20)
            actual2 = actual2.siguiente

        boton_ver_grafo = ttk.Button(
            marco_lista_sistemas,
            text="Ver Grafo",
            command=crear_funcion_ver_grafo("sistema_" + actual.dato.nombre),
        )

        boton_ver_grafo.pack(pady=10)

        actual = actual.siguiente


def listar_mensajes():
    global lista_mensajes
    lista_mensajes.ordenar_alfabeticamente_nombre()
    marco_dashboard.pack_forget()
    marco_lista_mensajes.pack()
    
    for widget in marco_lista_mensajes.winfo_children():
        widget.destroy()

    etiqueta_titulo_lista_mensajes = ttk.Label(
        marco_lista_mensajes, text="Lista de Mensajes", font=("Helvetica", 10)
    )

    etiqueta_titulo_lista_mensajes.pack(pady=10)

    boton_volver_dashboard4 = ttk.Button(
        marco_lista_mensajes, text="Volver al Tablero", command=mostrar_dashboard
    )

    boton_volver_dashboard4.pack(pady=10)
    actual = lista_mensajes.primero
    while actual:
        etiqueta_mensaje = ttk.Label(
            marco_lista_mensajes, text=f"{actual.dato.nombre}", font=("Helvetica", 10)
        )
        etiqueta_mensaje.pack()
        # mostrar tiempo optimo
        etiqueta_tiempo_optimo = ttk.Label(
            marco_lista_mensajes,
            text=f"Tiempo optimo: {actual.dato.tiempo_optimo}",
            font=("Helvetica", 10),
        )

        etiqueta_tiempo_optimo.pack()

        # mostrar mensaje
        etiqueta_mensaje = ttk.Label(
            marco_lista_mensajes,
            text=f"Mensaje: {actual.dato.mensaje}",
            font=("Helvetica", 10),
        )

        etiqueta_mensaje.pack()

        # mostrar el nombre del sistema a usar
        etiqueta_sistema = ttk.Label(
            marco_lista_mensajes,
            text=f"Sistema: {actual.dato.sistema_drones}",
            font=("Helvetica", 10),
        )

        etiqueta_sistema.pack()

        boton_ver_grafo = ttk.Button(
            marco_lista_mensajes,
            text="Ver Grafo",
            command=crear_funcion_ver_grafo("mensaje_" + actual.dato.nombre),
        )

        boton_ver_grafo.pack(pady=10)

        actual = actual.siguiente


def crear_funcion_ver_grafo(nombre):
    return lambda: ver_grafo(nombre)


def ver_grafo(nombre):
    os.system(f"start graphs/{nombre}.png")


def crear_dron():
    mostrar_formulario_creacion_dron()

def listar_drones():
    mostrar_lista_drones()

def mostrar_dashboard():
    marco_formulario.pack_forget()
    marco_lista_drones.pack_forget()
    marco_lista_sistemas.pack_forget()
    marco_lista_mensajes.pack_forget()
    marco_dashboard.pack()


def mostrar_formulario_creacion_dron():
    marco_dashboard.pack_forget()
    marco_formulario.pack()


def mostrar_lista_drones():
    marco_dashboard.pack_forget()
    marco_lista_drones.pack()

    for widget in marco_lista_drones.winfo_children():
        widget.destroy()

    etiqueta_titulo_lista_drones = ttk.Label(
        marco_lista_drones, text="Lista de Drones", font=("Helvetica", 14)
    )
    etiqueta_titulo_lista_drones.pack(pady=10)

    boton_volver_dashboard2 = ttk.Button(
        marco_lista_drones, text="Volver al Tablero", command=mostrar_dashboard
    )

    boton_volver_dashboard2.pack(pady=10)
    global lista_drones
    lista_drones.ordenar_alfabeticamente()
    actual = lista_drones.primero
    while actual:
        etiqueta_dron = ttk.Label(
            marco_lista_drones, text=f"Dron: {actual.dato}", font=("Helvetica", 12)
        )
        etiqueta_dron.pack()
        actual = actual.siguiente


def crear_nuevo_dron():
    global lista_drones
    nombre = entrada_nombre.get()
    if nombre:
        buscar = lista_drones.buscarDato(nombre)
        if buscar:
            messagebox.showwarning(
                "Crear Dron", f"El dron con el nombre {nombre} ya existe."
            )
        else:
            lista_drones.insertar(nombre)
            entrada_nombre.delete(0, tk.END)
        messagebox.showinfo(
            "Crear Dron", f"Creando un nuevo dron con el nombre: {nombre}"
        )
    else:
        messagebox.showwarning(
            "Crear Dron", "Por favor, ingresa un nombre para el dron."
        )


root = tk.Tk()
root.title("Tablero de Control")
root.geometry("1000x800")


class EstiloPersonalizado:
    def _init_(self):
        self.estilo = ttk.Style()
        self.estilo.configure(
            "BotonPersonalizado.TButton",
            width=40,
            height=40,
            borderwidth=3,
            relief="ridge",
            font=("Helvetica", 12, "bold"),
        )


estilo_personalizado = EstiloPersonalizado()

marco_dashboard = ttk.Frame(root)
marco_dashboard.pack(expand=True, fill="both", padx=10, pady=10)

botones = []

funciones_botones = [
    cargar_archivo,
    generar_archivo,
    listar_sistemas,
    crear_dron,
    listar_drones,
    listar_mensajes,
    lambda: messagebox.showinfo(
        "Ayuda",
        "Estudiante: Josue Daniel Chavez Portillo"
        + "\n"
        + "carnet: 202100033"
        + "\n"
        + "https://github.com/jchaveeez23/IPC2_PROYECTO2_202100033/blob/main/Documentacion/Documentaci%C3%B3n_202100033.pdf",
    ),
]
textos_botones = [
    "Cargar Archivo",
    "Generar XML",
    "Listar Sistemas",
    "Agregar Dron",
    "Listar Drones",
    "Listar Mensajes",
    "Ayuda",
]

for i, texto in enumerate(textos_botones):
    boton = ttk.Button(
        marco_dashboard,
        text=texto,
        command=funciones_botones[i],
        style="BotonPersonalizado.TButton",
    )
    botones.append(boton)

for i, boton in enumerate(botones):
    fila = i // 2
    columna = i % 2
    boton.grid(row=fila, column=columna, padx=10, pady=10)

marco_formulario = ttk.Frame(root)
marco_lista_drones = ttk.Frame(root)
marco_lista_sistemas = ttk.Frame(root)
marco_lista_mensajes = ttk.Frame(root)

etiqueta_titulo_formulario = ttk.Label(
    marco_formulario, text="Agregar Dron", font=("Helvetica", 14)
)

etiqueta_nombre = ttk.Label(marco_formulario, text="Nombre:")
entrada_nombre = ttk.Entry(marco_formulario)
boton_crear_dron = ttk.Button(
    marco_formulario, text="Crear Dron", command=crear_nuevo_dron
)
boton_volver_dashboard = ttk.Button(
    marco_formulario, text="Volver al Tablero", command=mostrar_dashboard
)

etiqueta_titulo_formulario.pack(pady=10)
etiqueta_nombre.pack()
entrada_nombre.pack()
boton_crear_dron.pack(pady=10)
boton_volver_dashboard.pack(pady=10)

marco_dashboard.pack()

root.mainloop()