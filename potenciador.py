import tkinter as tk
import random
from tkinter import messagebox

intentos_fallidos = 0

# Función para generar una potencia aleatoria del 0 al 7 en base a 2
def generar_potencia():
    global intentos_fallidos
    exponente = random.randint(0, 7)
    resultado = 2 ** exponente
    lbl_resultado.config(text=f"2", font=("Arial", 64))
    lbl_exponente.config(text=f"{exponente}", font=("Arial", 26))
    lbl_respuesta.config(text="")
    entry_respuesta.delete(0, tk.END)  # Borrar la respuesta anterior
    intentos_fallidos = 0

    # Mostrar el valor binario correspondiente
    valor_binario = ' '.join(format(resultado, '08b'))
    lbl_valor_binario.config(text=valor_binario)
    entry_respuesta.focus()  # Hacer foco en el campo de entrada

# Función para obtener la respuesta del usuario
def obtener_respuesta(event=None):
    global intentos_fallidos
    respuesta = entry_respuesta.get()
    respuesta_correcta = int(lbl_resultado["text"]) ** int(lbl_exponente["text"])
    try:
        respuesta = int(respuesta)
        if respuesta == respuesta_correcta:
            lbl_respuesta.config(text="¡Eres un Craaaaaa!", fg="green")
            ventana.after(2000, generar_potencia)  # Generar nueva potencia después de 1 segundo
        else:
            lbl_respuesta.config(text="Lero Lero!", fg="red")
            intentos_fallidos += 1
            if intentos_fallidos == 3:
                mostrar_alerta()
                intentos_fallidos = 0  # Reiniciar los intentos fallidos después de mostrar la alerta
            else:
                entry_respuesta.select_range(0, tk.END)  # Seleccionar el texto del campo de entrada
                entry_respuesta.icursor(tk.END)  # Mover el cursor al final del texto
    except ValueError:
        lbl_respuesta.config(text="3 Intentos Fallidos", fg="red")

# Función para mostrar la ventana de alerta
def mostrar_alerta():
    global intentos_fallidos
    messagebox.showwarning("3 Intentos Fallidos", "COME ON BOOOOOYYYY!!!")
    entry_respuesta.select_range(0, tk.END)  # Seleccionar el texto del campo de entrada
    entry_respuesta.icursor(tk.END)  # Mover el cursor al final del texto
    if intentos_fallidos < 3:
        ventana.after(1000, mostrar_alerta)  # Repetir la alerta después de 1 segundo si aún quedan intentos

# Función para validar la entrada y permitir solo caracteres numéricos
def validar_numerico(text):
    return text.isdigit() or text == ""

# Crear la ventana
ventana = tk.Tk()
ventana.title("PeterH4ck Potencias")

# Obtener las dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular la posición x e y para centrar la ventana
x = int((screen_width - 350) / 2)
y = int((screen_height - 500) / 2)

# Establecer la posición de la ventana
ventana.geometry(f"350x500+{x}+{y}")

# Marco principal para centrar el contenido
marco_principal = tk.Frame(ventana)
marco_principal.pack(expand=True)

# Marco para contener la potencia y el exponente
marco_potencia = tk.Frame(marco_principal)
marco_potencia.pack(pady=10)

# Etiqueta para mostrar el resultado de la potencia generada
lbl_resultado = tk.Label(marco_potencia, text="", font=("Arial", 24))
lbl_resultado.pack(side=tk.LEFT)

# Etiqueta para mostrar el exponente en tamaño pequeño en la parte superior derecha
lbl_exponente = tk.Label(marco_potencia, text="", font=("Arial", 12))
lbl_exponente.pack(side=tk.TOP)

# Etiqueta para mostrar el valor binario correspondiente al Resultado 1
lbl_valor_binario = tk.Label(marco_principal, text="", font=("Arial", 18))
lbl_valor_binario.pack(pady=10)

# Botón para generar una nueva potencia
btn_generar = tk.Button(marco_principal, text="Generar potencia", command=generar_potencia, font=("Arial", 16))
btn_generar.pack(pady=10)

# Entrada de texto para que el usuario ingrese su respuesta
validador = ventana.register(validar_numerico)  # Registrar la función de validación
entry_respuesta = tk.Entry(marco_principal, validate="key", validatecommand=(validador, "%S"), font=("Arial", 16))
entry_respuesta.pack(pady=10)
entry_respuesta.bind("<Return>", obtener_respuesta)  # Vincular la tecla Enter a la función obtener_respuesta
entry_respuesta.focus()  # Hacer foco en el campo de entrada

# Botón para verificar la respuesta del usuario
btn_verificar = tk.Button(marco_principal, text="Verificar respuesta", command=obtener_respuesta, font=("Arial", 16))
btn_verificar.pack(pady=10)

# Etiqueta para mostrar si la respuesta del usuario es correcta o no
lbl_respuesta = tk.Label(marco_principal, text="", font=("Arial", 16))
lbl_respuesta.pack(pady=20)

# Generar una potencia al abrir el programa
generar_potencia()

# Frame para el apartado de derechos de autor
frame_derechos = tk.Frame(ventana)
frame_derechos.pack(fill=tk.BOTH, expand=True)

# Etiqueta de derechos de autor
derechos_label = tk.Label(frame_derechos, text="© PeterH4ck 2023 ©", font=("smash", 14, "bold"))
derechos_label.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
