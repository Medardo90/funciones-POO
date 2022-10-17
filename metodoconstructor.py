# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 02:37:14 2022

@author: Patricio Haro
"""

"""metodo constructor"""
class Persona:
    pass # siempre poner pass para que este vacio y no tener incoveniente
    def __init__(self,nombre, año):
        self.nombre= nombre
        self.año=año
        
    def descripcion (self):
        return "{} tiene: {} ".format(self.nombre,self.año)# con format se tiene un resultaso mas presentable
    
    def comentario (self, frase):
        return "{} dice: {}".format(self.nombre,frase)
    
doctor= Persona("jose","26")
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("hola que tal"))

"""modificar atributo"""

class Email:
    def __init__(self):
        self.enviado= False
    def enviar_correo(self):
        self.enviado=True

micorreo=Email()

print(micorreo.enviado)
micorreo.enviar_correo()
print(micorreo.enviado)














    
    