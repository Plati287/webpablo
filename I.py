import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import json
import os
import traceback

class ExamGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ExamGen Pro")
        self.root.geometry("800x600")
        
        # Configuración de estilo
        style = ttk.Style()
        style.theme_use('clam')  # Tema moderno
        
        # Configuración de colores
        bg_color = '#f0f0f0'
        accent_color = '#3498db'
        text_color = '#333333'
        
        self.root.configure(bg=bg_color)
        
        # Personalizar estilo de botones
        style.configure('TButton', 
            background=accent_color, 
            foreground='white', 
            font=('Arial', 12, 'bold'),
            padding=10
        )
        style.map('TButton', 
            background=[('active', '#2980b9')],
            foreground=[('active', 'white')]
        )
        
        # Configurar fuentes
        style.configure('.', font=('Arial', 10))
        
        # Carpeta de datos
        self.carpeta_datos = os.path.join(os.path.expanduser('~'), '.exam_generator')
        os.makedirs(self.carpeta_datos, exist_ok=True)
        
        self.archivo_examenes = os.path.join(self.carpeta_datos, 'examenes_test.json')
        
        self.examenes = {}
        self.cargar_examenes()
        
        # Evento de cierre
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.crear_interfaz_principal()
        
    def cargar_examenes(self):
        try:
            if os.path.exists(self.archivo_examenes):
                with open(self.archivo_examenes, 'r', encoding='utf-8') as f:
                    self.examenes = json.load(f)
            else:
                self.examenes = {}
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar los exámenes: {e}")
            self.examenes = {}
    
    def guardar_examenes(self):
        try:
            # Asegurar que la carpeta exista
            os.makedirs(os.path.dirname(self.archivo_examenes), exist_ok=True)
            
            with open(self.archivo_examenes, 'w', encoding='utf-8') as f:
                json.dump(self.examenes, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar los exámenes: {e}")
    
    def on_closing(self):
        # Guardar antes de cerrar
        self.guardar_examenes()
        self.root.destroy()
    
    def crear_interfaz_principal(self):
        # Marco principal con padding
        marco_principal = ttk.Frame(self.root, padding="50 50 50 50")
        marco_principal.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(marco_principal, text="ExamGen Pro", 
                          font=('Arial', 24, 'bold'), 
                          foreground='#2c3e50')
        titulo.pack(pady=20)
        
        # Descripción
        descripcion = ttk.Label(marco_principal, 
                               text="Generador de Exámenes Tipo Test",
                               font=('Arial', 14))
        descripcion.pack(pady=10)
        
        # Marco de botones
        marco_botones = ttk.Frame(marco_principal)
        marco_botones.pack(pady=20)
        
        # Botones con estilo
        botones = [
            ("Crear Nuevo Examen", self.crear_examen),
            ("Gestionar Exámenes", self.gestionar_examenes),
            ("Realizar Examen", self.seleccionar_examen)
        ]
        
        for texto, comando in botones:
            boton = ttk.Button(marco_botones, text=texto, 
                               command=comando, style='TButton')
            boton.pack(pady=10, fill=tk.X)
    
    def crear_examen(self):
        nombre_examen = simpledialog.askstring("Crear Examen", "Nombre del examen:")
        if nombre_examen:
            self.examenes[nombre_examen] = []
            self.guardar_examenes()  # Guardar inmediatamente
            self.agregar_pregunta(nombre_examen)
    
    def agregar_pregunta(self, nombre_examen):
        ventana_pregunta = tk.Toplevel(self.root)
        ventana_pregunta.title("Agregar Pregunta Tipo Test")
        
        tk.Label(ventana_pregunta, text="Pregunta:").pack()
        entrada_pregunta = tk.Text(ventana_pregunta, height=3, width=50)
        entrada_pregunta.pack()
        
        # Campos para opciones de respuesta
        opciones_frame = tk.Frame(ventana_pregunta)
        opciones_frame.pack(pady=10)
        
        etiquetas_opciones = ['A', 'B', 'C', 'D']
        entradas_opciones = []
        
        for i, letra in enumerate(etiquetas_opciones):
            tk.Label(opciones_frame, text=f"Opción {letra}:").grid(row=i, column=0)
            entrada_opcion = tk.Entry(opciones_frame, width=50)
            entrada_opcion.grid(row=i, column=1)
            entradas_opciones.append(entrada_opcion)
        
        # Selección de respuesta correcta
        tk.Label(ventana_pregunta, text="Seleccione la respuesta correcta:").pack()
        respuesta_correcta_var = tk.StringVar(value='A')
        respuesta_correcta_menu = tk.OptionMenu(ventana_pregunta, respuesta_correcta_var, 'A', 'B', 'C', 'D')
        respuesta_correcta_menu.pack()
        
        def guardar_pregunta():
            try:
                pregunta = entrada_pregunta.get("1.0", tk.END).strip()
                opciones = [entrada.get().strip() for entrada in entradas_opciones]
                respuesta_correcta = respuesta_correcta_var.get()
                
                if pregunta and all(opciones):
                    nueva_pregunta = {
                        "pregunta": pregunta,
                        "opciones": {
                            "A": opciones[0],
                            "B": opciones[1],
                            "C": opciones[2],
                            "D": opciones[3]
                        },
                        "respuesta_correcta": respuesta_correcta
                    }
                    
                    # Verificar si es una lista de preguntas o un diccionario con resumen
                    if isinstance(self.examenes[nombre_examen], list):
                        self.examenes[nombre_examen].append(nueva_pregunta)
                    else:
                        self.examenes[nombre_examen]['preguntas'].append(nueva_pregunta)
                    
                    self.guardar_examenes()  # Guardar después de añadir cada pregunta
                    
                    respuesta = messagebox.askyesno("Pregunta Agregada", "¿Desea agregar otra pregunta?")
                    if respuesta:
                        entrada_pregunta.delete("1.0", tk.END)
                        for entrada in entradas_opciones:
                            entrada.delete(0, tk.END)
                        respuesta_correcta_var.set('A')
                    else:
                        ventana_pregunta.destroy()
                else:
                    messagebox.showwarning("Error", "Debe llenar todos los campos")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")
        
        tk.Button(ventana_pregunta, text="Guardar Pregunta", command=guardar_pregunta).pack(pady=10)
    
    def gestionar_examenes(self):
        ventana_gestion = tk.Toplevel(self.root)
        ventana_gestion.title("Gestionar Exámenes")
        
        for nombre in self.examenes:
            frame = tk.Frame(ventana_gestion)
            frame.pack(pady=5)
            
            tk.Label(frame, text=nombre).pack(side=tk.LEFT)
            tk.Button(frame, text="Agregar Pregunta", 
                      command=lambda n=nombre: self.agregar_pregunta(n)).pack(side=tk.LEFT)
            tk.Button(frame, text="Eliminar Examen", 
                      command=lambda n=nombre: self.eliminar_examen(n, ventana_gestion)).pack(side=tk.LEFT)
            tk.Button(frame, text="Añadir/Editar Resumen", 
                      command=lambda n=nombre: self.editar_resumen(n)).pack(side=tk.LEFT)
    
    def editar_resumen(self, nombre_examen):
        # Crear una ventana para editar el resumen del examen
        ventana_resumen = tk.Toplevel(self.root)
        ventana_resumen.title(f"Resumen de {nombre_examen}")
        ventana_resumen.geometry("500x300")
        
        # Etiqueta para instrucciones
        tk.Label(ventana_resumen, text="Escriba un resumen para este examen:").pack(pady=10)
        
        # Área de texto para el resumen
        area_resumen = tk.Text(ventana_resumen, height=10, width=50, wrap=tk.WORD)
        area_resumen.pack(pady=10)
        
        # Cargar resumen existente si lo hay
        # Modificar para manejar tanto la estructura antigua como la nueva
        if isinstance(self.examenes[nombre_examen], dict) and 'resumen' in self.examenes[nombre_examen]:
            area_resumen.insert(tk.END, self.examenes[nombre_examen]['resumen'])
        
        def guardar_resumen():
            # Obtener el texto del resumen
            resumen = area_resumen.get("1.0", tk.END).strip()
            
            # Verificar y convertir la estructura si es necesario
            if isinstance(self.examenes[nombre_examen], list):
                self.examenes[nombre_examen] = {
                    'preguntas': self.examenes[nombre_examen],
                    'resumen': resumen
                }
            else:
                self.examenes[nombre_examen]['resumen'] = resumen
            
            # Guardar los cambios
            self.guardar_examenes()
            
            # Cerrar la ventana
            ventana_resumen.destroy()
            
            # Mostrar mensaje de confirmación
            messagebox.showinfo("Éxito", "Resumen guardado correctamente")
        
        # Botón para guardar el resumen
        tk.Button(ventana_resumen, text="Guardar Resumen", command=guardar_resumen).pack(pady=10)
    
    def eliminar_examen(self, nombre, ventana):
        del self.examenes[nombre]
        self.guardar_examenes()  # Guardar después de eliminar
        ventana.destroy()
        self.gestionar_examenes()
    
    def seleccionar_examen(self):
        if not self.examenes:
            messagebox.showinfo("Error", "No hay exámenes creados")
            return
        
        ventana_seleccion = tk.Toplevel(self.root)
        ventana_seleccion.title("Seleccionar Examen")
        
        for nombre in self.examenes:
            tk.Button(ventana_seleccion, text=nombre, 
                      command=lambda n=nombre: self.realizar_examen(n, ventana_seleccion)).pack(pady=5)
    
    def realizar_examen(self, nombre_examen, ventana_seleccion):
        ventana_seleccion.destroy()
        
        # Mostrar resumen si existe
        # Modificar para manejar tanto la estructura antigua como la nueva
        if (isinstance(self.examenes[nombre_examen], dict) and 'resumen' in self.examenes[nombre_examen]) or \
           isinstance(self.examenes[nombre_examen], dict):
            ventana_resumen = tk.Toplevel(self.root)
            ventana_resumen.title(f"Resumen de {nombre_examen}")
            
            # Mostrar resumen
            resumen = (self.examenes[nombre_examen].get('resumen', '') 
                       if isinstance(self.examenes[nombre_examen], dict) 
                       else '')
            
            tk.Label(ventana_resumen, text="Resumen del Examen:", font=('Arial', 14, 'bold')).pack(pady=10)
            texto_resumen = tk.Text(ventana_resumen, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
            texto_resumen.pack(padx=20, pady=10)
            texto_resumen.insert(tk.END, resumen)
            
            def comenzar_examen():
                ventana_resumen.destroy()
                self.comenzar_examen_real(nombre_examen)
            
            tk.Button(ventana_resumen, text="Comenzar Examen", command=comenzar_examen).pack(pady=10)
        else:
            # Si no hay resumen, comenzar directamente el examen
            self.comenzar_examen_real(nombre_examen)
    
    def comenzar_examen_real(self, nombre_examen):
        # Obtener las preguntas de la estructura nueva o antigua
        preguntas = (self.examenes[nombre_examen]['preguntas'] 
                     if isinstance(self.examenes[nombre_examen], dict) 
                     else self.examenes[nombre_examen])
        
        # Generar un examen aleatorio con preguntas y orden de respuestas aleatorias
        preguntas_aleatorias = random.sample(preguntas, len(preguntas))
        
        # Aleatorizar el orden de las respuestas para cada pregunta
        for pregunta in preguntas_aleatorias:
            # Crear lista de opciones para reordenar
            opciones_originales = list(pregunta['opciones'].items())
            random.shuffle(opciones_originales)
            
            # Encontrar la posición de la respuesta correcta original
            respuesta_correcta = pregunta['respuesta_correcta']
            
            # Crear nuevo diccionario de opciones reordenado
            nueva_opciones = {letra: texto for letra, texto in opciones_originales}
            
            # Encontrar la nueva letra para la respuesta correcta
            for nueva_letra, (letra_original, _) in enumerate(opciones_originales):
                if letra_original == respuesta_correcta:
                    break
            
            # Actualizar la pregunta con las opciones reordenadas y la nueva respuesta correcta
            pregunta['opciones'] = nueva_opciones
            pregunta['respuesta_correcta'] = chr(ord('A') + nueva_letra)

            ventana_examen = tk.Toplevel(self.root)
        ventana_examen.title(f"Examen: {nombre_examen}")
        
        class EstadoExamen:
            def __init__(self):
                self.pregunta_actual = 0
                self.respuestas = []
        
        estado = EstadoExamen()
        
        # Variables para manejar la selección de respuestas
        respuesta_var = tk.StringVar()
        
        frame_pregunta = tk.Frame(ventana_examen)
        frame_pregunta.pack(pady=20)
        
        label_pregunta = tk.Label(frame_pregunta, text="", wraplength=500)
        label_pregunta.pack()
        
        frame_opciones = tk.Frame(ventana_examen)
        frame_opciones.pack(pady=20)
        
        label_resultado = tk.Label(ventana_examen, text="")
        label_resultado.pack(pady=10)
        
        def mostrar_pregunta():
            if estado.pregunta_actual < len(preguntas_aleatorias):
                # Limpiar frame de opciones
                for widget in frame_opciones.winfo_children():
                    widget.destroy()
                
                pregunta_actual = preguntas_aleatorias[estado.pregunta_actual]
                label_pregunta.config(text=pregunta_actual['pregunta'])
                
                # Crear botones de opción
                for letra, texto in pregunta_actual['opciones'].items():
                    tk.Radiobutton(
                        frame_opciones, 
                        text=f"{letra}: {texto}", 
                        variable=respuesta_var, 
                        value=letra
                    ).pack(anchor=tk.W)
                
                # Resetear selección
                respuesta_var.set(None)
                label_resultado.config(text="")
            else:
                mostrar_resultados()
        
        def verificar_respuesta():
            if respuesta_var.get() is None:
                messagebox.showwarning("Advertencia", "Debe seleccionar una respuesta")
                return
            
            pregunta_actual = preguntas_aleatorias[estado.pregunta_actual]
            respuesta_usuario = respuesta_var.get()
            
            if respuesta_usuario == pregunta_actual['respuesta_correcta']:
                resultado = "¡Correcto!"
                estado.respuestas.append(True)
            else:
                resultado = f"Incorrecto. La respuesta correcta era: {pregunta_actual['respuesta_correcta']} - {pregunta_actual['opciones'][pregunta_actual['respuesta_correcta']]}"
                estado.respuestas.append(False)
            
            label_resultado.config(text=resultado)
            
            # Preparar siguiente pregunta
            estado.pregunta_actual += 1
            ventana_examen.after(2000, mostrar_pregunta)
        
        def mostrar_resultados():
            ventana_resultados = tk.Toplevel(ventana_examen)
            ventana_resultados.title("Resultados del Examen")
            
            total_preguntas = len(preguntas_aleatorias)
            correctas = sum(estado.respuestas)
            porcentaje = (correctas / total_preguntas) * 100
            
            tk.Label(ventana_resultados, text=f"Preguntas Correctas: {correctas}/{total_preguntas}").pack()
            tk.Label(ventana_resultados, text=f"Porcentaje: {porcentaje:.2f}%").pack()
        
        boton_responder = tk.Button(ventana_examen, text="Responder", command=verificar_respuesta)
        boton_responder.pack(pady=10)
        
        mostrar_pregunta()
    
    def run(self):
        self.root.mainloop()

# Manejar errores no capturados
def show_error(exc_type, exc_value, exc_traceback):
    err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(f"Ocurrió un error no controlado:\n{err_msg}")
    messagebox.showerror("Error Crítico", f"Ocurrió un error inesperado:\n{err_msg}")

# Configurar el manejador de errores global
tk.Tk.report_callback_exception = show_error

# Iniciar la aplicación
if __name__ == "__main__":
    app = ExamGenerator()
    app.run()