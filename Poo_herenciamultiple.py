# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 00:04:33 2022

@author: Patricio Haro
"""

"""HERENCIA MULTIPLE"""
"""se refiere a la posibildad de crear una clase de mutiples, enlasar clases superiores"""
"""ES TENER DIFERNETES CLASES Y SE COMBINA AL FINAL EN UNA CLASE ESPECIAL PARA"""
"""UINIR CADA UNA DE LAS CLASES QUE ES ESTAN es nesesario tener un metodo destructor del """

"""HERENCIA MULTINIVEL"""
"""Las caracteristicas de la clase base y la clase derivada """
"""se heredan en la nueva clase derivada, cada clase esta enlasada una tras otra"""

"""EJEMPLO HERENCIA MULTIPLE"""

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando.....")
    def ocupado(self):
        print("ocupado....")
    
class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("Tomando fotos...")
        
class Reproduccion:
    def __init__(self):
        pass
    def reproduccionmusica(self):
        print("Reproducuondo musica...")
    def reproduccionvideo(self):
        print("Reprducir video...")
        
class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self): # del se utiza para limpiar los recursos en este caso la clase smarphone
    #para ahorrar memoria
        print("Telefono apagado")
        
movil=Smartphone()
#print(dir(movil))#dir es como direccion
print(movil.fotografia())
print(movil.llamar())


