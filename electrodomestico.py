from abc import ABC, abstractmethod

class Electrodomestico(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass
    

class Lavadora(Electrodomestico):
    
    def encender(self):
        return "La lavadora se enciende"
    
    def apagar(self):
        return "La lavadora se apaga" 
    
class Refrigerador(Electrodomestico):    
    
    def encender(self):
        return "El refrigerador se enciende"
    
    def apagar(self):
        return "El refrigerador se apaga"