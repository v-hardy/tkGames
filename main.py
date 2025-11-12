import tkinter as tk
from tkinter import messagebox      # messagebox no está dentro del módulo raíz tkinter, sino que es un submódulo. Por eso lo importamos asi.
from mod_random import dame_numero_secreto

# Valor a numero_secreto
numero_secreto = dame_numero_secreto()
# Imprimir valor en pantalla
print(numero_secreto)

# Inicializo variable intentos
intentos = 0

# Función para verificar el número ingresado
def verificar():
    global intentos

    try:
        adivinanza = int(entrada.get())
        intentos += 1

        if adivinanza < numero_secreto:
            messagebox.showinfo("Resultado", "Demasiado bajo. Intenta otra vez.")
        elif adivinanza > numero_secreto:
            messagebox.showinfo("Resultado", "Demasiado alto. Intenta otra vez.")
        else:
            messagebox.showinfo("¡Felicidades!", f"Adivinaste el número en {intentos} intentos.")

    except ValueError:
        messagebox.showerror("Error","Por favor, ingresa un número válido.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("¡Bienvenido al juego de adivinanza!")
ventana.geometry("700x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Estoy pensando en un número entre 1 y 100. Ingresa un número:")
etiqueta.pack(pady=15)

# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=15)

# Botón para verificar
boton = tk.Button(ventana, text="Verificar", command=verificar)
boton.pack(pady=30)

# Ejecutar el bucle principal
ventana.mainloop()
