# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 01:45:06 2022

@author: Patricio Haro
"""
"""funciones para atributos  setattr"""

class Persona:
    edad= "27"
    nombre= "patricio"
    
doctor= Persona()
print("La edad del doctor es:", doctor.edad)
print("La edad del doctor es:", getattr(doctor,"edad"))


"""hasattr"""

class Persona:
    edad= "27"
    nombre= "patricio"
    
doctor= Persona()
print("El doctor tiene una edad? :", hasattr (doctor,"edad"))
print("El doctor tiene una edad? :", hasattr (doctor,"apellido"))


""" para hacer cambios con setattr"""

class Persona:
    edad= "27"
    nombre= "patricio"
    
doctor= Persona()
print("antes era:",doctor.nombre)
setattr(doctor,"nombre","medardo")
print("ahora se llama:",doctor.nombre)

"""delattr para eliminar"""

class Persona:
    edad= "27"
    nombre= "patricio"
    pais= "ecuador"
    
doctor=Persona()
delattr(Persona,"pais")#para eliminar un atributo dentro de una clase
#print(doctor.pais)#elimina pais
print(doctor.nombre)
print(doctor.edad)



















