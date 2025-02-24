from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass

#Implementamos la clase Perro y Pajaro que heredan de la clase Animal
class Perro(Animal):
    
    def hacer_sonido(self):
        return "Guau"
    
    def moverse(self):
        return "El perro camina hacia su hogar"
    
class Pajaro(Animal):
    
    def hacer_sonido(self):
        return "Pío"
    
    def moverse(self):
        return "El pájaro vuela con los demas pájaros"