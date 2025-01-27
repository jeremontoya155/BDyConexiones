import os
import psycopg2
from psycopg2 import sql
import tkinter as tk
from tkinter import filedialog

# Función para seleccionar un archivo
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Conexión a la base de datos
conn = psycopg2.connect(
    "postgresql://postgres:TDXQSEjHNRoHGqlQmcuNuSClWoUlUujB@viaduct.proxy.rlwy.net:45221/railway"
)
cur = conn.cursor()

# Realizar modificaciones en la tabla
cur.execute("ALTER TABLE recetas ADD COLUMN IF NOT EXISTS sucursales TEXT;")

# Seleccionar archivo
file_path = select_file()

# Obtener el nombre de la carpeta que contiene el archivo
sucursal = os.path.basename(os.path.dirname(file_path))

# Leer el archivo y enviar los datos a la base de datos
with open(file_path, 'r') as file:
    for line in file:
        numero_receta = line.strip()
        estado = "P"
        cur.execute(
            sql.SQL("INSERT INTO recetas (numero, estado, sucursales) VALUES (%s, %s, %s) ON CONFLICT (numero) DO NOTHING;"),
            [numero_receta, estado, sucursal]
        )

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()

print("Datos enviados correctamente.")
