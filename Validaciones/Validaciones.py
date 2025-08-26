# Función que pide al usuario ingresar solo números
def leer_numeros():
    dato = input("Ingresa solo números: ")  # Lee la entrada del usuario
    if dato.isdigit():  # Verifica si la entrada contiene solo dígitos
        print("Correcto: es un número.")
    else:
        print("Error: solo se permiten números.")


# Función que pide al usuario ingresar solo letras minúsculas
def leer_minusculas():
    dato = input("Ingresa solo letras minúsculas: ")
    # Verifica si son solo letras, y todas en minúscula
    if dato.islower() and dato.isalpha():#Todo esté en minúscula → islower(). 
                                         #No haya símbolos ni números → isalpha(
        print("Correcto: solo minúsculas.")
    else:
        print("Error: deben ser solo letras minúsculas.")


# Función que pide al usuario ingresar solo letras mayúsculas
def leer_mayusculas():
    dato = input("Ingresa solo letras mayúsculas: ")
    # Verifica si son solo letras, y todas en mayúscula
    if dato.isupper() and dato.isalpha():#que sean todas mayúsculas → isupper().
        print("Correcto: solo mayúsculas.")
    else:
        print("Error: deben ser solo letras mayúsculas.")


# Función que permite letras o números (no símbolos)
def leer_letras_o_numeros():
    dato = input("Ingresa letras o números: ")
    # Verifica si son solo letras o números (sin espacios ni símbolos)
    if dato.isalnum():# devuelve true solo si contiene letras o numeros
        print("Correcto: solo letras o números.")
    else:
        print("Error: solo se permiten letras o números (sin símbolos).")


# Función que verifica que la cadena tenga al menos una letra y al menos un número
def leer_letras_y_numeros():
    dato = input("Ingresa una cadena con letras y números: ")
    # Verifica si hay al menos una letra en la cadena
    tiene_letra = any(c.isalpha() for c in dato)
    # Verifica si hay al menos un número en la cadena
    tiene_numero = any(c.isdigit() for c in dato)

    # Solo si tiene al menos una letra Y un número, está correcto
    if tiene_letra and tiene_numero:
        print("Correcto: contiene letras y números.")
    else:
        print("Error: debe contener al menos una letra y un número.")


# Menú para que el usuario elija qué validación desea hacer
while True:
    print("\nSelecciona una opción:")
    print("1. Leer solo números")
    print("2. Leer solo letras minúsculas")
    print("3. Leer solo letras mayúsculas")
    print("4. Leer letras o números")
    print("5. Leer letras y números (al menos uno de cada)")
    print("6. Salir")

    # Lee la opción ingresada por el usuario
    opcion = input("Opción: ")

    # Según la opción, llama a la función correspondiente
    if opcion == '1':
        leer_numeros()
    elif opcion == '2':
        leer_minusculas()
    elif opcion == '3':
        leer_mayusculas()
    elif opcion == '4':
        leer_letras_o_numeros()
    elif opcion == '5':
        leer_letras_y_numeros()
    elif opcion == '6':
        print("Saliendo...")  # Mensaje de despedida
        break  # Sale del bucle while y termina el programa
    else:
        print("Opción inválida. Intenta de nuevo.")  # En caso de que el usuario ingrese algo incorrecto
