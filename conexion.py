import sqlite3 
# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db') 
# Crear un cursor 
cursor = conexion.cursor() 
# Ejecutar una consulta 
cursor.execute('SELECT * FROM Personas') 
# Obtener los resultados 
resultados = cursor.fetchall() 
# Imprimir los resultados 
for fila in resultados: print(fila) 
# Cerrar la conexión 
conexion.close()