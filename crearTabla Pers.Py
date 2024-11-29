import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear la tabla Personas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Personas (
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
)
''')

# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()
