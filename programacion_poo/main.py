# Programación Orientada a Objetos - Programa Principal

from mascota import Mascota

def main():
    """Función principal que demuestra el uso de clases"""
    
    # Crear instancias de Mascota
    mascota1 = Mascota("Rex", "perro", 3)
    mascota2 = Mascota("Whiskers", "gato", 2)
    mascota3 = Mascota("Tweety", "pajaro", 1)
    
    # Lista de mascotas
    mascotas = [mascota1, mascota2, mascota3]
    
    print("=== MIS MASCOTAS ===\n")
    
    # Iterar sobre las mascotas
    for mascota in mascotas:
        print(mascota.presentarse())
        print(f"Hace: {mascota.hacer_sonido()}")
        print()
    
    # Aumentar edad de la primera mascota
    print("=== CUMPLEAÑOS ===")
    print(mascota1.cumplir_años())

if __name__ == "__main__":
    main()
