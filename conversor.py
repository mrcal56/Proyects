import tkinter as tk
from tkinter import ttk
import requests

# Obtener tasas de cambio desde una API
def obtener_tasas_de_cambio():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo errores HTTP
        datos = response.json()
        print("Tasas de cambio obtenidas exitosamente")  # Mensaje de depuración
        return datos["rates"]
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener tasas de cambio: {e}")
        return None

# Función para realizar la conversión
def convertir():
    try:
        cantidad = float(entry_cantidad.get())
        moneda_desde = combo_desde.get()
        moneda_hasta = combo_hasta.get()
        print(f"Convertir {cantidad} {moneda_desde} a {moneda_hasta}")  # Mensaje de depuración

        tasas = obtener_tasas_de_cambio()

        if tasas is None:
            label_resultado.config(text="Error al obtener tasas de cambio")
            print("Error al obtener tasas de cambio")  # Mensaje de depuración
            return

        if moneda_desde not in tasas or moneda_hasta not in tasas:
            label_resultado.config(text="Moneda no válida")
            print("Moneda no válida")  # Mensaje de depuración
            return

        tasa_desde = tasas[moneda_desde]
        tasa_hasta = tasas[moneda_hasta]
        resultado = (cantidad / tasa_desde) * tasa_hasta
        label_resultado.config(text=f"{cantidad} {moneda_desde} = {resultado:.2f} {moneda_hasta}")
        print(f"Resultado: {resultado:.2f}")  # Mensaje de depuración
    except ValueError:
        label_resultado.config(text="Por favor, ingresa una cantidad válida.")
        print("Valor ingresado no es válido")  # Mensaje de depuración
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")
        print(f"Error inesperado: {e}")  # Mensaje de depuración

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Moneda")
ventana.geometry("500x400")

# Etiqueta y entrada para la cantidad
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.pack(pady=10)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=10)

# Combobox para seleccionar la moneda de origen
label_desde = tk.Label(ventana, text="Moneda Origen:")
label_desde.pack(pady=10)
combo_desde = ttk.Combobox(ventana, values=list(obtener_tasas_de_cambio().keys()))
combo_desde.pack(pady=10)

# Combobox para seleccionar la moneda de destino
label_hasta = tk.Label(ventana, text="Moneda Destino:")
label_hasta.pack(pady=10)
combo_hasta = ttk.Combobox(ventana, values=list(obtener_tasas_de_cambio().keys()))
combo_hasta.pack(pady=10)

# Botón para realizar la conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=20)

# Etiqueta para mostrar el resultado, inicializada con un valor predeterminado
label_resultado = tk.Label(ventana, text="El resultado de la conversión aparecerá aquí.", font=(15))
label_resultado.pack(pady=10)





# Ejecutar la ventana principal
ventana.mainloop()
