##Desempeño 1, realizado por Alexander Soto

########## listados
usuarios = []
prestamos = []


def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    numero_tarjeta = input("Ingrese el número de tarjeta: ")
    usuario = {"nombre": nombre, "numero_tarjeta": numero_tarjeta}
    usuarios.append(usuario)
    print(f"Usuario {nombre} registrado con éxito.")

def tomar_cicla():
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    usuario = buscar_usuario(numero_tarjeta)
    
    if usuario:
        origen = input("Ingrese la estación de origen: ")
        destino = input("Ingrese la estación de destino: ")
        prestamo = {"usuario": usuario["nombre"], "origen": origen, "destino": destino}
        prestamos.append(prestamo)
        print(f"{usuario['nombre']} ha tomado una bicicleta desde {origen} hacia {destino}.")
    else:
        print("Usuario no encontrado. Verifica el número de tarjeta.")

def listar_usuarios():
    print("Listado de usuarios:")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Número de Tarjeta: {usuario['numero_tarjeta']}")

def listar_prestamos():
    print("Listado de préstamos:")
    for prestamo in prestamos:
        print(f"Usuario: {prestamo['usuario']}, Origen: {prestamo['origen']}, Destino: {prestamo['destino']}")

def buscar_usuario(numero_tarjeta):
    for usuario in usuarios:
        if usuario["numero_tarjeta"] == numero_tarjeta:
            return usuario
    return None

while True:
    print("\nSistema integrado de ciclas :D  = ")
    print("1. Registrar Usuario")
    print("2. Tomar Bicicleta")
    print("3. Listar Usuarios")
    print("4. Listar Préstamos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        tomar_cicla()
    elif opcion == "3":
        listar_usuarios()
    elif opcion == "4":
        listar_prestamos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Seleccione una opción válida.")
