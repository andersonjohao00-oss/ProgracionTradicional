# programacion_tradicional/tradicional.py

def registrar_mascota():
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    edad = input("Edad de la mascota: ")
    return {"nombre": nombre, "especie": especie, "edad": edad}

def mostrar_mascota(mascota):
    print(f"\nMascota: {mascota['nombre']} | Especie: {mascota['especie']} | Edad: {mascota['edad']}")

# Flujo principal
datos = registrar_mascota()
mostrar_mascota(datos)
