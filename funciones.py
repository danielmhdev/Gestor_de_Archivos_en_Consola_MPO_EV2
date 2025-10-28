import time
import os

def mostrar_menu():
    print (f"Te encuentras en {os.getcwd()}")
    print("\n### MENÚ ###")
    print("1 - Listar contenido del directorio actual")
    print("2 - Crear un nuevo directorio")
    print("3 - Crear un archivo de texto")
    print("4 - Escribir texto en un archivo existente")
    print("5 - Eliminar un archivo o directorio")
    print("6 - Mostrar información del archivo")
    print("7 - Salir")

def listar_contenido():
    try:
        contenido = os.listdir()  # Lista con archivos y carpetas del directorio actual

        if len(contenido) == 0:
            print("El directorio está vacío")
            return  # Salimos de la función si está vacío

        print("\n### CONTENIDO ###")
        print("-" * 40)

        for elemento in sorted(contenido):
            if os.path.isfile(elemento):
                print(f"Archivo: {elemento}")
            elif os.path.isdir(elemento):
                print(f"Carpeta: {elemento}")
        print("-" * 40)

    except PermissionError:
        print("Error: No tienes permisos para leer este directorio")
    except Exception as e:
        print(f"Error inesperado: {e}")


def crear_directorio(nombre):
        if not nombre:
            return "Error: El nombre no puede estar vacío"

        if os.path.exists(nombre):
            return f"Error: Ya existe un directorio llamado '{nombre}'"

        try:
            os.mkdir(nombre) #Creamos la carpeta
            return f"Directorio '{nombre}' creada correctamente"
        except PermissionError:
            return "Error: No tienes permisos para crear el directorio"
        except OSError as e:
            return f"Error: Nombre inválido: {e}"


def crear_archivo(nombre, contenido):
    if not nombre:
        return "Error: El nombre no puede estar vacío"

    if os.path.exists(nombre):
        return f"Error: Ya existe un archivo llamado '{nombre}'"

    try:
        with open(nombre, 'w') as archivo: # Guarda el objeto file de open() en la variable archivo
            archivo.write(contenido)
        return f"Archivo '{nombre}' creado correctamente"

    except PermissionError:
        return "Error: No tienes permisos para crear archivos en este directorio"

    except OSError as e:
        return f"Error: Nombre de archivo inválido: {e}"


def escribir_en_archivo(nombre, texto):
    if not nombre:
        return "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return f"Error: El archivo '{nombre}' no existe"

    if not os.path.isfile(nombre):
        return f"Error: '{nombre}' no es un archivo"

    try:
        with open(nombre, 'a') as archivo: #Guardamos al final del archivo con 'a' el texto elegido
            archivo.write(texto + '\n')
        return f"Texto añadido al archivo '{nombre}' correctamente"

    except PermissionError:
        return "Error: No tienes permisos para escribir en este archivo"

    except OSError as e:
        return f"Error: Nombre de archivo inválido: {e}"

def eliminar_elemento(nombre):
    if not nombre:
        return "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return f"Error: '{nombre}' no existe"

    try:
        if os.path.isfile(nombre):
            os.remove(nombre)
            return f"Archivo '{nombre}' eliminado correctamente"
        elif os.path.isdir(nombre):
            os.rmdir(nombre)
            return f"Carpeta '{nombre}' eliminada correctamente"

    except PermissionError:
        return "Error: No tienes permisos para eliminar este elemento"

    except OSError as e:
        if os.path.isdir(nombre):
            return "Error: La carpeta no está vacía. Elimina su contenido primero"
        else:
            return f"Error del sistema: {e}"

def mostrar_informacion(nombre):
    if not nombre:
        return "Error: El nombre no puede estar vacío"

    if not os.path.exists(nombre):
        return f"Error: El archivo: '{nombre}' no existe"


    try:
        info = f"\nInformación de '{nombre}': \n"
        info += ("-" * 40) + "\n"

        # Determinar tipo
        if os.path.isfile(nombre):
            info += "Tipo: Archivo\n"
            tamaño = os.path.getsize(nombre)
            info += f"Tamaño: {tamaño} bytes\n"
        elif os.path.isdir(nombre):
            info += "Tipo: Carpeta\n"

        # Fecha
        timestamp = os.path.getmtime(nombre)
        fecha = time.ctime(timestamp)
        info += f"Última modificación: {fecha}\n"
        info += ("-" * 40)

        return info

    except PermissionError:
        return "Error: No tienes permisos para acceder a la información de este elemento"

    except OSError as e:
        return f"Error del sistema: {e}"

