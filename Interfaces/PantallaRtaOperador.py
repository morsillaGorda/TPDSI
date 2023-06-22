import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PantallaRtaOperador:
    def __init__(self, gestor):
        self.gestor = gestor
        self.ventana = tk.Tk()
        self.ventana.title("Registrar respuesta de operador")
        ancho_ventana = 800
        alto_ventana = 600
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
        self.ventana.resizable(False, False)

        self.container = ttk.Frame(self.ventana, padding=20)
        self.container.grid(sticky="nsew")

        self.label1 = ttk.Label(self.container, text="Cliente:")
        self.label1.config(font=("Calibri", 12, "bold"))
        self.label1.grid(row=0, column=0, sticky="w")

        self.label2 = ttk.Label(self.container, text="", wraplength=500)
        self.label2.config(font=("Calibri", 12))
        self.label2.grid(row=0, column=1, sticky="w")

        self.label3 = ttk.Label(self.container, text="", wraplength=500)
        self.label3.config(font=("Calibri", 12))
        self.label3.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

        self.resultadosMensajesValidacion = []
        self.todasCorrectas = False
        self.descripcion_consulta_label = None
        self.descripcion_consulta_input = None
        self.accion_realizar_label = None
        self.accion_realizar_input = None
        self.confirmar_button = None

    def mostrarDatosDeLaLlamada(self, nombreClienteLlamada, descripcionCategoriaYOpcion):
        self.label2.config(text=nombreClienteLlamada)
        self.label3.config(text=descripcionCategoriaYOpcion)

    def mostrarOpcionesDeValidacion(self, mensajesValidacionesDeSubopcionSeleccionada):
        for mensajeValidacion in mensajesValidacionesDeSubopcionSeleccionada:
            self.resultadosMensajesValidacion.append([mensajeValidacion[1], False])
            primer_texto = mensajeValidacion[0]
            opciones_validacion = mensajeValidacion[1]
            texto_mensajes = f"\n- {primer_texto}:\n"
            label_mensajes = ttk.Label(self.container, text=texto_mensajes)
            label_mensajes.grid(sticky="w", padx=10)
            opcion_seleccionada = tk.StringVar(value="")
            
            def actualizar_opcion(opcion):
                nonlocal opcion_seleccionada
                opcion_seleccionada.set(opcion)
                self.tomarOpcionDeValidacion(opcion)
                self.todasCorrectas = all(resultado[1] for resultado in self.resultadosMensajesValidacion)
                self.mostrarInputsNuevos()

            for opcion in opciones_validacion:
                radiobutton = ttk.Radiobutton(
                    self.container,
                    text=opcion,
                    variable=opcion_seleccionada,
                    value=opcion,
                    command=lambda opcion=opcion: actualizar_opcion(opcion)
                )
                opcion_seleccionada.set("")
                radiobutton.grid(sticky="w", padx=20)

    def mostrarInputsNuevos(self):
        self.eliminarInputsNuevos()

        if self.todasCorrectas:
            self.descripcion_consulta_label = ttk.Label(self.container, text="Descripción de consulta")
            self.descripcion_consulta_label.grid(sticky="w", padx=10, pady=10)
            self.descripcion_consulta_input = ttk.Entry(self.container)
            self.descripcion_consulta_input.grid(sticky="ew", padx=10, pady=5)

            self.accion_realizar_label = ttk.Label(self.container, text="Acción a realizar")
            self.accion_realizar_label.grid(sticky="w", padx=10, pady=10)
            self.accion_realizar_input = ttk.Combobox(self.container, values=["", "Opcion 1", " Opcion 2", "Opcion 3"])
            self.accion_realizar_input.grid(sticky="ew", padx=10, pady=5)

            self.confirmar_button = ttk.Button(self.container, text="Confirmar", command=self.confirmarRespuesta)
            self.confirmar_button.grid(sticky="w", pady=20)
        else:
            self.eliminarInputsNuevos()

    def eliminarInputsNuevos(self):
        if self.descripcion_consulta_label:
            self.descripcion_consulta_label.destroy()
            self.descripcion_consulta_label = None
        if self.descripcion_consulta_input:
            self.descripcion_consulta_input.destroy()
            self.descripcion_consulta_input = None
        if self.accion_realizar_label:
            self.accion_realizar_label.destroy()
            self.accion_realizar_label = None
        if self.accion_realizar_input:
            self.accion_realizar_input.destroy()
            self.accion_realizar_input = None
        if self.confirmar_button:
            self.confirmar_button.destroy()
            self.confirmar_button = None

    def confirmarRespuesta(self):
        descripcion_consulta = self.descripcion_consulta_input.get()
        accion_realizar = self.accion_realizar_input.get()
        self.tomarConfirmacion(descripcion_consulta, accion_realizar)

    def run(self):
        self.mostrarInputsNuevos()
        self.ventana.mainloop()

    def tomarOpcionDeValidacion(self, opcionSeleccionada):
        self.gestor.tomarOpcionDeValidacion(opcionSeleccionada)

    def habilitarSeleccionRespuesta(self, resultado, opcionSeleccionada):
        if resultado:
            messagebox.showinfo("Resultado", f"{opcionSeleccionada} - Opcion Correcta!")
        else:
            messagebox.showinfo("Resultado", f"{opcionSeleccionada} - Opcion Incorrecta!")
        for resultadoValidacion in self.resultadosMensajesValidacion:
            if opcionSeleccionada in resultadoValidacion[0]:
                resultadoValidacion[1] = resultado

    def tomarConfirmacion(self, descripcion_consulta, accion_realizar):
        self.gestor.tomarConfirmacion(descripcion_consulta, accion_realizar)

    def mostrarMensajeDeConfirmacion(self):
        messagebox.showinfo("Confirmación", "Respuesta registrada correctamente")
        self.descripcion_consulta_input.delete(0, tk.END)
        self.accion_realizar_input.delete(0, tk.END)

    def mostrarMensajeDeLlamadaTerminada(self):
        messagebox.showinfo("Llamada terminada", "El cliente colgó la llamada")                          