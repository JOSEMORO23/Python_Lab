import mysql.connector#conector para conectar Python con MySQL
# Función para establecer la conexión con la base de datos MySQL (XAMPP)
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # usuario por defecto en XAMPP
        password="",         # sin contraseña por defecto
        database="seguridad" # Nombre de la base de datos creada en phpMyAdmin
    )
# Función que autentica al usuario verificando sus datos en la base de datos
def autenticar(usuario_input, contrasena_input):
    conexion = conectar()      # Llamamos a la función para conectar a la base
    cursor = conexion.cursor()      # Creamos un cursor para ejecutar consultas
   

    # Consulta preparada para evitar inyección SQL
    consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
    valores = (usuario_input, contrasena_input)# Tupla con los valores que se van a insertar en la consulta
    cursor.execute(consulta, valores) # Ejecutamos la consulta pasando los valores de forma segura

    resultado = cursor.fetchone()  # Obtenemos el primer resultado que coincida (si existe)

    if resultado:
        print("Acceso concedido.")
    else:
        print(" Acceso denegado.")

    cursor.close()# Cerramos el cursor (buena práctica)
    conexion.close() # Cerramos la conexión a la base de datos

# Pedir datos al usuario
usuario = input("Usuario: ")
clave = input("Contraseña: ")
autenticar(usuario, clave)
