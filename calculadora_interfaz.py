import tkinter as tk
from tkinter import messagebox

#***********************************************************************************
#                        Funciones de las operaciones
#***********************************************************************************
def sumar():
    try:
        num1 = int(numero1.get())
        num2 = int(numero2.get())
        result = num1 + num2
        mostrar_resultado(f"{num1} + {num2} = {result}")
    except ValueError:
        mostrar_error()

def restar():
    try:
        num1 = int(numero1.get())
        num2 = int(numero2.get())
        result = num1 - num2
        mostrar_resultado(f"{num1} - {num2} = {result}")
    except ValueError:
        mostrar_error()

def multiplicar():
    try:
        num1 = int(numero1.get())
        num2 = int(numero2.get())
        result = num1 * num2
        mostrar_resultado(f"{num1} * {num2} = {result}")
    except ValueError:
        mostrar_error()

def dividir():
    try:
        num1 = int(numero1.get())
        num2 = int(numero2.get())
        if num2 == 0:
            messagebox.showerror("Error", "División por 0 no permitida.")
        else:
            result = num1 / num2
            mostrar_resultado(f"{num1} / {num2} = {result}")
    except ValueError:
        mostrar_error()

def mostrar_resultado(mensaje):
    resultado_label.config(text=mensaje)

def mostrar_error():
    messagebox.showerror("Error", "Por favor, ingrese números válidos.")

#***********************************************************************************
#                                   interfaz
#***********************************************************************************
#***********************************************************************************
#                     Configuración de la ventana principal 
#***********************************************************************************
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400") 
ventana.config(bg="#f0f0f0")  
#*********************************************************************************
#                            Entradas de números
#*********************************************************************************
numero1 = tk.Entry(ventana, font=("Arial", 14), bd=2, bg="#fff", fg="#000")
numero1.pack(pady=10, padx=20)

numero2 = tk.Entry(ventana, font=("Arial", 14), bd=2, bg="#fff", fg="#000")
numero2.pack(pady=10, padx=20)

#***********************************************************************************
#                           Botones de operación
#***********************************************************************************
btn_suma = tk.Button(ventana, text="Sumar", command=sumar, font=("Arial", 12), bg="#4CAF50", fg="#fff", bd=2)
btn_suma.pack(pady=5)

btn_resta = tk.Button(ventana, text="Restar", command=restar, font=("Arial", 12), bg="#f44336", fg="#fff", bd=2)
btn_resta.pack(pady=5)

btn_multiplicacion = tk.Button(ventana, text="Multiplicar", command=multiplicar, font=("Arial", 12), bg="#2196F3", fg="#fff", bd=2)
btn_multiplicacion.pack(pady=5)

btn_division = tk.Button(ventana, text="Dividir", command=dividir, font=("Arial", 12), bg="#FF9800", fg="#fff", bd=2)
btn_division.pack(pady=5)

#***********************************************************************************
#                      Etiqueta para mostrar el resultado
#***********************************************************************************
resultado_label = tk.Label(ventana, text="", font=("Arial", 14), bg="#f0f0f0", fg="#000")
resultado_label.pack(pady=20)

#***********************************************************************************
#                     Iniciar el bucle de la interfaz
#***********************************************************************************
ventana.mainloop()
