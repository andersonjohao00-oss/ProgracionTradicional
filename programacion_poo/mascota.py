# Programación Orientada a Objetos - Clase Mascota

class Mascota:
    """Clase que representa una mascota"""
    
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    
    def presentarse(self):
        """Método que presenta la mascota"""
        return f"Soy {self.nombre}, soy un/a {self.tipo} de {self.edad} años"
    
    def hacer_sonido(self):
        """Método que simula el sonido de la mascota"""
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau!",
            "pajaro": "¡Pío pío!",
            "conejo": "¡Croc croc!"
        }
        return sonidos.get(self.tipo.lower(), "¡Sonido desconocido!")
    
    def cumplir_años(self):
        """Método que incrementa la edad de la mascota"""
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años"
