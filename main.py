from animal import Perro, Pajaro
from electrodomestico import Lavadora, Refrigerador
from archivo import ArchivoTexto, ArchivoImagen
from Retos.transporte import Autobus, Tren
from Retos.dispositivo import Telefono, Computadora
from Retos.evaluar import Examen, Proyecto
    
# # Creamos la lista de animales y llamamos a sus métodos
animales = [Perro(), Pajaro()]

for animal in animales:
    print(animal.hacer_sonido())
    print(animal.moverse())

# Creamos la lista de electrodomesticos y llamamos a sus métodos

electrodomesticos = [Lavadora(), Refrigerador()]

for electrodomestico in electrodomesticos:
    print(electrodomestico.encender())
    print(electrodomestico.apagar())

# Creamos la lista de archivos y llamamos a sus métodos 

archivos = [ArchivoTexto(), ArchivoImagen()]

for archivo in archivos:
    print(archivo.abrir())
    print(archivo.cerrar()) 

# Creamos la lista de transportes y llamamos a sus métodos

transportes = [Autobus(), Tren()]

for transporte in transportes:  
    print(transporte.arrancar())
    print(transporte.detener())

# Creamos la lista de dispositivos y llamamos a sus métodos

dispositivos = [Telefono(), Computadora()]

for dispositivo in dispositivos:
    print(dispositivo.encender())
    print(dispositivo.usar())

# Creamos la lista de evaluaciones y llamamos a sus métodos

evaluaciones = [Examen(), Proyecto()]

for evaluacion in evaluaciones:
    print(evaluacion.calificar())
    print(evaluacion.mostrar_resultados())