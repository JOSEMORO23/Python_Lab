def cargar_usuarios():
    usuarios = {}# Creamos un diccionario vacío para guardar usuario: contraseña
    with open("usuarios.txt", "r") as archivo: # Abrimos el archivo 'usuarios.txt' en modo lectura ('r')
        for linea in archivo:# Recorremos cada línea del archivo
            datos = linea.strip().split(",")# Eliminamos saltos de línea y separamos por coma
            if len(datos) == 2:# # Validamos que haya dos elementos: usuario y clave
                usuario, clave = datos # Asignamos los valores separados a variables
                usuarios[usuario] = clave# Guardamos en el diccionari
    return usuarios

def autenticar():
    usuarios = cargar_usuarios()# Cargamos los usuarios desde el archivo
    # Pedimos al usuario que escriba su nombre de usuario y contraseña
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("✅ Acceso concedido.")
    else:
        print("❌ Acceso denegado.")

autenticar()
