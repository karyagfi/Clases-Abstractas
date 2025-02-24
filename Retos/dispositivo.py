from abc import ABC, abstractmethod

class Dispositivo(ABC): 

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def usar(self):
        pass
    
class Telefono(Dispositivo): 
    
    def encender(self):
        return "El telefono se enciende"
    
    def usar(self):
        return "El telefono se usa para llamar"
    
class Computadora(Dispositivo):
    
    def encender(self):
        return "La computadora se enciende"
    
    def usar(self):
        return "La computadora se usa para programar"