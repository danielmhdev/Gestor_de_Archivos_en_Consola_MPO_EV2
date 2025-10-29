import time
import os
from colorama import Fore, Style, init

init(autoreset=True)
def mostrar_menu():
    print (Fore.CYAN + f"Te encuentras en {os.getcwd()}")
    print(Fore.YELLOW + "\n### MENÚ ###")
    print("1 - Listar contenido del directorio actual")
    print("2 - Crear un nuevo directorio")
    print("3 - Crear un archivo de texto")
    print("4 - Escribir texto en un archivo existente")
    print("5 - Eliminar un archivo o directorio")
    print("6 - Mostrar información del archivo")
    print("7 - Cambiar al directorio padre (..)")
    print("8 - Entrar en un directorio")
    print("9 - Renombrar archivo o carpeta")
    print("10 - Salir")

def listar_contenido():
    try:
        contenido = os.listdir()  # Lista con archivos y carpetas del directorio actual

        if len(contenido) == 0:
            print(Fore.YELLOW + "El directorio está vacío")
            return  # Salimos de la función si está vacío

        print(Fore.CYAN + "\n### CONTENIDO ###")
        print("-" * 40)

        for elemento in sorted(contenido):
            if os.path.isfile(elemento):
                print(Fore.WHITE + f"Archivo: {elemento}")
            elif os.path.isdir(elemento):
                print(Fore.BLUE + Style.BRIGHT + f"Carpeta: {elemento}")
        print("-" * 40)

    except PermissionError:
        print(Fore.RED + "Error: No tienes permisos para leer este directorio")
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}")


def crear_directorio(nombre):
        if not nombre:
            return Fore.RED + "Error: El nombre no puede estar vacío"

        if os.path.exists(nombre):
            return Fore.RED + f"Error: Ya existe un directorio llamado '{nombre}'"

        try:
            os.mkdir(nombre) #Creamos la carpeta
            return Fore.GREEN + f"Directorio '{nombre}' creado correctamente"
        except PermissionError:
            return Fore.RED + "Error: No tienes permisos para crear el directorio"
        except OSError as e:
            return Fore.RED + f"Error: Nombre inválido: {e}"


def crear_archivo(nombre, contenido):
    if not nombre:
        return Fore.RED + "Error: El nombre no puede estar vacío"

    if os.path.exists(nombre):
        return Fore.RED + f"Error: Ya existe un archivo llamado '{nombre}'"

    try:
        with open(nombre, 'w') as archivo: # Guarda el objeto file de open() en la variable archivo
            archivo.write(contenido)
        return Fore.GREEN + f"Archivo '{nombre}' creado correctamente"

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para crear archivos en este directorio"

    except OSError as e:
        return Fore.RED + f"Error: Nombre de archivo inválido: {e}"


def escribir_en_archivo(nombre, texto):
    if not nombre:
        return Fore.RED + "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return Fore.RED + f"Error: El archivo '{nombre}' no existe"

    if not os.path.isfile(nombre):
        return Fore.RED + f"Error: '{nombre}' no es un archivo"

    try:
        with open(nombre, 'a') as archivo: #Guardamos al final del archivo con 'a' el texto elegido
            archivo.write(texto + '\n')
        return Fore.GREEN + f"Texto añadido al archivo '{nombre}' correctamente"

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para escribir en este archivo"

    except OSError as e:
        return Fore.RED + f"Error: Nombre de archivo inválido: {e}"

def eliminar_elemento(nombre):
    if not nombre:
        return Fore.RED + "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return Fore.RED + f"Error: '{nombre}' no existe"

    try:
        if os.path.isfile(nombre):
            os.remove(nombre)
            return Fore.GREEN + f"Archivo '{nombre}' eliminado correctamente"
        elif os.path.isdir(nombre):
            os.rmdir(nombre)
            return Fore.GREEN + f"Carpeta '{nombre}' eliminada correctamente"

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para eliminar este elemento"

    except OSError as e:
        if os.path.isdir(nombre):
            return Fore.RED + "Error: La carpeta no está vacía. Elimina su contenido primero"
        else:
            return Fore.RED + f"Error del sistema: {e}"

def mostrar_informacion(nombre):
    if not nombre:
        return Fore.RED + "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return Fore.RED + f"Error: El archivo: '{nombre}' no existe"


    try:
        info = Fore.CYAN + f"\nInformación de '{nombre}': \n"
        info += ("-" * 40) + "\n"

        # Determinar tipo
        if os.path.isfile(nombre):
            info += Fore.WHITE  + "Tipo: Archivo\n"
            tamaño = os.path.getsize(nombre)
            info += f"Tamaño: {tamaño} bytes\n"
        elif os.path.isdir(nombre):
            info += Fore.BLUE + "Tipo: Carpeta\n"

        # Fecha
        timestamp = os.path.getmtime(nombre)
        fecha = time.ctime(timestamp)
        info += Fore.CYAN + f"Última modificación: {fecha}\n"
        info += ("-" * 40)

        return info

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para acceder a la información de este elemento"

    except OSError as e:
        return Fore.RED + f"Error del sistema: {e}"

def cambiar_directorio_padre():
    try:
        path_actual = os.getcwd()
        os.chdir("..")
        path_nuevo = os.getcwd()
        if path_actual == path_nuevo:
            return Fore.YELLOW + "Ya estás en el directorio raíz, no se puede ir más atrás."
        else:
            return Fore.GREEN + f"Has cambiado al directorio: {path_nuevo}"
    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para acceder al directorio padre."
    except Exception as e:
        return Fore.RED + f"Error inesperado: {e}"


def entrar_directorio(nombre):

    if not nombre:
        return Fore.RED + "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return Fore.RED + f"Error: La carpeta '{nombre}' no existe"

    if not os.path.isdir(nombre):
        return Fore.RED + f"Error: '{nombre}' no es una carpeta, es un archivo."

    try:
        os.chdir(nombre)
        path_nuevo = os.getcwd()
        return Fore.GREEN + f"Has entrado en: {path_nuevo}"

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para entrar en esta carpeta."
    except Exception as e:
        return Fore.RED + f"Error inesperado: {e}"


def renombrar_elemento(nombre_antiguo, nombre_nuevo):
    if not nombre_antiguo:
        return Fore.RED + "Error: El nombre actual no puede estar vacío"
    if not nombre_nuevo:
        return Fore.RED + "Error: El nombre nuevo no puede estar vacío"

    if not os.path.exists(nombre_antiguo):
        return Fore.RED + f"Error: El archivo o carpeta '{nombre_antiguo}' no existe"

    if os.path.exists(nombre_nuevo):
        return Fore.RED + f"Error: Ya existe un elemento llamado '{nombre_nuevo}'"

    try:
        os.rename(nombre_antiguo, nombre_nuevo)
        return Fore.GREEN + f"'{nombre_antiguo}' ha sido renombrado a '{nombre_nuevo}'"

    except PermissionError:
        return Fore.RED + "Error: No tienes permisos para renombrar este elemento."
    except OSError as e:
        return Fore.RED + f"Error del sistema: {e}"