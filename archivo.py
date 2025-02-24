from abc import ABC, abstractmethod

class Archivo(ABC):

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def cerrar(self):
        pass
    
class ArchivoTexto(Archivo):
    
    def abrir(self):
        return "El archivo de texto se abre"
    
    def cerrar(self):
        return "El archivo de texto se cierra"
    
class ArchivoImagen(Archivo):
    
    def abrir(self):
        return "El archivo de imagen se abre"
    
    def cerrar(self):
        return "El archivo de imagen se cierra"