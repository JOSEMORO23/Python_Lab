import os
import shutil
import time
import threading
import filecmp

BACKUP_FOLDER = "backups/"
ORIGINAL_FOLDER = "original_files/"

def escoger_directorio():
    directorio = input("Introduce la ruta del directorio a respaldar (por defecto 'original_files/'): ").strip()
    return directorio if directorio else ORIGINAL_FOLDER

def hacer_backup(directorio):
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)
    for archivo in os.listdir(directorio):
        origen = os.path.join(directorio, archivo)
        destino = os.path.join(BACKUP_FOLDER, archivo)
        if os.path.isfile(origen):
            shutil.copy2(origen, destino)
            print(f"[✓] Backup creado para: {archivo}")

def backup_periodico(directorio):
    while True:
        hacer_backup(directorio)
        print("Esperando 5 minutos para el siguiente backup...")
        time.sleep(300)  # 5 minutos

def restaurar_archivo(nombre_archivo):
    backup_path = os.path.join(BACKUP_FOLDER, nombre_archivo)
    original_path = os.path.join(ORIGINAL_FOLDER, nombre_archivo)
    if os.path.exists(backup_path):
        shutil.copy2(backup_path, original_path)
        print(f"[✓] Archivo restaurado: {nombre_archivo}")
        if filecmp.cmp(backup_path, original_path, shallow=False):
            print("[✓] Validación completa: el archivo restaurado es idéntico al original.")
        else:
            print("[✗] El archivo restaurado es diferente al original.")
    else:
        print("[!] No se encontró un respaldo de ese archivo.")

def menu():
    directorio = ORIGINAL_FOLDER
    hilo_backup = None

    while True:
        print("\n--- MENÚ DE BACKUP ---")
        print("1. Escoger directorio a respaldar")
        print("2. Hacer backup manual")
        print("3. Activar backup automático (cada 5 min)")
        print("4. Restaurar archivo")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            directorio = escoger_directorio()
        elif opcion == '2':
            hacer_backup(directorio)
        elif opcion == '3':
            if hilo_backup is None or not hilo_backup.is_alive():
                hilo_backup = threading.Thread(target=backup_periodico, args=(directorio,))
                hilo_backup.daemon = True
                hilo_backup.start()
                print("Backup automático activado.")
            else:
                print("Ya está activo.")
        elif opcion == '4':
            archivo = input("Nombre del archivo a restaurar: ")
            restaurar_archivo(archivo)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
