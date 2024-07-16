import psycopg2
from psycopg2 import sql

# Conexión a la base de datos
conn = psycopg2.connect(
    "postgresql://postgres:TDXQSEjHNRoHGqlQmcuNuSClWoUlUujB@viaduct.proxy.rlwy.net:45221/railway"
)
cur = conn.cursor()

# Borrar todo el contenido de la tabla
cur.execute("DELETE FROM recetas;")

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()

print("Contenido de la tabla 'recetas' borrado correctamente.")
