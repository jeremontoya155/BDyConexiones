import os
import shutil
import random

# Lista de nombres de las carpetas
carpetas = [
    "99029498005", "99029499003", "99029404003", "99033358005", "99033295009",
    "99029500008", "99033296007", "99033294002", "99033663008", "99033293004",
    "99035665001", "99033291008", "99037419001", "99033297005", "99036568006",
    "99036629006", "99036998005", "99037744002", "99033579006", "99037766005",
    "99038657005", "99038046001", "99038698009", "99038968006", "99036479006"
]

# Obtener la ruta del escritorio del usuario
escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Ruta de la carpeta 'sucursales'
sucursales_path = os.path.join(escritorio, 'sucursales')

# Ruta de la carpeta de origen con archivos TIFF
origen_path = os.path.join(sucursales_path, "99029498005")

# Obtener todos los archivos TIFF en la carpeta de origen
tif_files = [f for f in os.listdir(origen_path) if f.endswith('.tif')]

# Copiar un número aleatorio de archivos TIFF a cada subcarpeta
for carpeta in carpetas[1:]:  # Omitir la primera carpeta ya que es la fuente
    # Crear la ruta de la subcarpeta
    carpeta_path = os.path.join(sucursales_path, carpeta)
    
    # Copiar un número aleatorio de archivos TIFF
    num_files_to_copy = random.randint(1, len(tif_files))
    files_to_copy = random.sample(tif_files, num_files_to_copy)
    
    for file in files_to_copy:
        shutil.copy(os.path.join(origen_path, file), os.path.join(carpeta_path, file))

print("Archivos TIFF copiados correctamente.")
