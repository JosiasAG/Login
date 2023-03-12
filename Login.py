import re

def validarNombre(nombre):
    while True:
        nombre = input("Introduce tu nombre: ")
        if len(nombre) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
            continue
        elif len(nombre) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
            continue
        elif not nombre.isalpha():
            print("El nombre de usuario puede contener solo letras y números")
            continue
        else:
            return nombre


def validarContrasena(contrasena):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    while True:
        contrasena = input("Ingresa tu contraseña: ")
        if len(contrasena) < 8:
            print("La contraseña debe contener al menos 8 caracteres")
            continue
        elif " " in contrasena:
            print("La contraseña no puede contener espacios en blanco")
            continue
        elif regex.search(contrasena) == None or contrasena.isupper() or contrasena.islower():
            print("La contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no "
                  "alfanumérico")
            continue
        else:
            return contrasena


nombre = ""
contrasena = ""
nombreReal = validarNombre(nombre)
contrasenaReal = validarContrasena(contrasena)

usuario = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")


while True:
    if usuario == nombreReal and password == contrasenaReal:
        print(f"Bienvenido {nombreReal}")
        break
    else:
        print("Usuario y/o contraseña incorrecta, inténtelo de nuevo")
        usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

