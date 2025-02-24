from abc import ABC, abstractmethod

class Evaluacion(ABC): 

    @abstractmethod
    def calificar(self):
        pass

    @abstractmethod
    def mostrar_resultados(self):
        pass
    
class Examen(Evaluacion):
    
    def calificar(self):
        return "El examen se califica"
    
    def mostrar_resultados(self):
        return "Se muestran los resultados del examen"
    
class Proyecto(Evaluacion):
    
    def calificar(self):
        return "El proyecto se califica"
    
    def mostrar_resultados(self):
        return "Se muestran los resultados del proyecto"