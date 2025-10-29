from funciones import(
mostrar_menu,
listar_contenido,
crear_directorio,
crear_archivo,
escribir_en_archivo,
eliminar_elemento,
mostrar_informacion,
cambiar_directorio_padre,
entrar_directorio,
renombrar_elemento
)

def main():
    print("Bienvenido al Gestor de Archivos")
    opcion = -1

    while opcion != 10:
        mostrar_menu()
        try:
            opcion = int(input("\nSelecciona una opción: "))
        except ValueError:
            print("Error: Introduce un número válido")
            continue

        match opcion:
            case 1:
                listar_contenido()
            case 2:
                nombre = input("Escribe el nombre de la carpeta que deseas crear: ").strip()
                mensaje = crear_directorio(nombre)
                print(mensaje)
            case 3:
                nombre = input("Escribe el nombre del archivo que deseas crear: ").strip()
                contenido = input("Escribe el contenido inicial del archivo: ")
                mensaje = crear_archivo(nombre, contenido)
                print(mensaje)
            case 4:
                nombre = input("¿En cuál archivo deseas escribir? ").strip()
                texto = input("Escribe el texto que deseas añadir: ")
                mensaje = escribir_en_archivo(nombre, texto)
                print(mensaje)
            case 5:
                nombre = input("¿Escribe el nombre de la carpeta u archivo que deseas eliminar?: ").strip()
                if not nombre:
                    print("Error: El nombre no puede estar vacío")
                    continue
                confirmar = input(f"¿Estas seguro de eliminar '{nombre}'? (s/n): ").lower()
                if confirmar == 's':
                    mensaje = eliminar_elemento(nombre)
                    print(mensaje)
                else:
                    print("Operación cancelada")
            case 6:
                nombre = input("¿De cuál archivo o carpeta deseas mostrar información?: ").strip()
                info = mostrar_informacion(nombre)
                print(info)
            case 7:
                mensaje = cambiar_directorio_padre()
                print(mensaje)
            case 8:
                nombre = input("¿A qué carpeta quieres entrar?: ").strip()
                mensaje = entrar_directorio(nombre)
                print(mensaje)
            case 9:
                nombre_antiguo = input("Nombre actual del archivo/carpeta: ").strip()
                nombre_nuevo = input("Nuevo nombre: ").strip()
                mensaje = renombrar_elemento(nombre_antiguo, nombre_nuevo)
                print(mensaje)
            case 10:
                print("\nSaliendo del gestor...")
            case _:
                print("Error: Introduce un número del 1 al 10")


if __name__ == "__main__":
    main()