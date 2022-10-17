# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:24:24 2022

@author: Patricio Haro
"""
"""HERENCIA"""

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
        
    def ingresardato(self):
        self.datos = [int(input("Ingrese dato "+ str(i+1) + " = " ))for i in range(self.n)]

class opbasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)#trabajar con constructor , que funcione con dos valores 
        
    def suma(self):
        a,b,=self.datos #self.datos = a,b,# si da error se puede escribir al lado contrario 
        s= a+b
        print("El resultado es:",s)
    
    def resta(self):
        a,b,=self.datos 
        r= a-b
        print("El resultado es:",r)
        
class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
        
    def cuadrada(self):
        import math
        a, = self.datos 
        print("El resultado es:",(math.sqrt(a)))
        
ejemplo=raiz()#llamar a la clase que se nesecita 
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())
        