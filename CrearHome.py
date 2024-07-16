import os

# Lista de nombres de carpetas
carpetas = [
    "Sanchez Antoniolli",
    "Sanchez Antoniolli II",
    "Sanchez Antoniolli III",
    "Sanchez Antoniolli IV",
    "Sanchez Antoniolli V",
    "Sanchez Antoniolli VI",
    "Sanchez Antoniolli VII",
    "Sanchez Antoniolli VIII",
    "Sanchez Antoniolli IX",
    "Sanchez Antoniolli X",
    "Sanchez Anoniolli XI",
    "Sanchez Antoniolli XII",
    "Sanchez Antoniolli XIV",
    "Sanchez Antoniolli XV",
    "Sanchez Antoniolli XVI",
    "Sanchez Antoniolli XVII",
    "SANCHEZ ANTONIOLLI XVIII",
    "Sanchez Antoniolli XIX",
    "Sanchez Antoniolli XX",
    "Sanchez Antoniolli XXI",
    "Sanchez Antoniolli 23",
    "SANCHEZ ANTONIOLLI 24",
    "Sanchez Antoniolli 25",
    "Sanchez Antoniolli 26",
    "Sanchez Carestia"
]

# Obtener la ruta del escritorio
desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Crear carpeta principal en el escritorio
resultados_dir = os.path.join(desktop_dir, "resultados")
if not os.path.exists(resultados_dir):
    os.makedirs(resultados_dir)

# Crear subcarpetas
for carpeta in carpetas:
    carpeta_path = os.path.join(resultados_dir, carpeta)
    if not os.path.exists(carpeta_path):
        os.makedirs(carpeta_path)

print(f"Carpetas creadas en el directorio {resultados_dir}")
