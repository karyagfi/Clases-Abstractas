from abc import ABC, abstractmethod

class Transporte(ABC):
    
    @abstractmethod
    def arrancar(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass
    
class Autobus(Transporte):
    
    def arrancar(self):
        return "El autobus arranca"
    
    def detener(self):
        return "El autobus se detiene"
    
class Tren(Transporte):
    
    def arrancar(self):
        return "El tren arranca"
    
    def detener(self):
        return "El tren se detiene"