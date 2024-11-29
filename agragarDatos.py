import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear la tabla Personas si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS Personas (
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
)
''')

# Función para insertar datos en la tabla Personas
def insertar_persona(nombre, edad, ciudad):
    cursor.execute('''
    INSERT INTO Personas (nombre, edad, ciudad)
    VALUES (?, ?, ?)
    ''', (nombre, edad, ciudad))
    conexion.commit()

# Solicitar datos al usuario
nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
ciudad = input("Introduce la ciudad: ")

# Insertar los datos en la tabla
insertar_persona(nombre, edad, ciudad)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Datos insertados correctamente.")
