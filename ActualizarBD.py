import os
import re
import psycopg2
from psycopg2 import sql
import tkinter as tk
from tkinter import filedialog
from datetime import date

# Función para seleccionar un archivo
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Función para convertir números romanos a enteros
def roman_to_int(roman):
    roman_numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_numeral_map.get(char, 0)
        if value == 0:
            return None  # No es un número romano válido
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

# Función para extraer el último número o número romano de una cadena
def extract_last_number_or_roman(text):
    # Buscar el último número
    match = re.search(r'(\d+)$', text)
    if match:
        return match.group(0)
    # Buscar el último número romano
    match = re.search(r'([IVXLCDM]+)$', text, re.IGNORECASE)
    if match:
        return roman_to_int(match.group(0).upper())
    return None

# Función para validar si una cadena es un número
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Conexión a la base de datos
conn = psycopg2.connect(
    "postgresql://postgres:TDXQSEjHNRoHGqlQmcuNuSClWoUlUujB@viaduct.proxy.rlwy.net:45221/railway"
)
cur = conn.cursor()

# Realizar modificaciones en la tabla
cur.execute("""
    ALTER TABLE recetas 
    ADD COLUMN IF NOT EXISTS sucursales TEXT,
    ADD COLUMN IF NOT EXISTS FechaCreacion DATE;
""")

# Asegurar que 'numero' es la clave primaria
cur.execute("""
    DO $$
    BEGIN
        IF NOT EXISTS (
            SELECT constraint_name 
            FROM information_schema.table_constraints 
            WHERE table_name = 'recetas' AND constraint_type = 'PRIMARY KEY'
        ) THEN
            ALTER TABLE recetas ADD CONSTRAINT recetas_pkey PRIMARY KEY (numero);
        END IF;
    END
    $$;
""")

# Seleccionar archivo
file_path = select_file()

# Obtener el nombre de la carpeta que contiene el archivo
sucursal = os.path.basename(os.path.dirname(file_path))

# Extraer el último número o número romano de la carpeta contenedora
sucursal_numero = extract_last_number_or_roman(sucursal)
if sucursal_numero is None:
    sucursal_numero = sucursal  # Si no hay número, usar el nombre completo

# Leer el archivo y enviar los datos a la base de datos
with open(file_path, 'r') as file:
    for line in file:
        numero_receta = line.strip()
        if is_number(numero_receta):
            estado = "P"
            fecha_creacion = date.today()
            cur.execute(
                sql.SQL("INSERT INTO recetas (numero, estado, sucursales, FechaCreacion) VALUES (%s, %s, %s, %s) ON CONFLICT (numero) DO NOTHING;"),
                [numero_receta, estado, sucursal_numero, fecha_creacion]
            )
        else:
            print(f"El valor '{numero_receta}' no es un número válido y será omitido.")

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()

print("Datos enviados correctamente.")
