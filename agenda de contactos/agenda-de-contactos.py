def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir de la agenda")
    print("\n" )

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']} ")
        print(f"Email: {agenda[nombre]['email']} ")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def lista_de_contactos(agenda):
    if agenda:
        print("\nLista de contacto:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f": {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda aún está vacia")    

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción:")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            lista_de_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta pronto!")
            break

agenda_contactos()
