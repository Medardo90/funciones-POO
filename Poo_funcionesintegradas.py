# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:49:20 2022

@author: Patricio Haro
"""
"""FUNCIONES INTEGRADAS"""

class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
        
    def ingresardato(self):
        self.datos = [int(input("Ingrese dato "+ str(i+1) + " = " ))for i in range(self.n)]

class opbasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)#trabajar con constructor , que funcione con dos valores 
        
    def suma(self):#METODO, ACCION
        a,b,=self.datos #self.datos = a,b,# si da error se puede escribir al lado contrario 
        s= a+b
        print("El resultado es:",s)
    
    def resta(self):#METODO,ACCION
        a,b,=self.datos 
        r= a-b
        print("El resultado es:",r)
        
class raiz(Calculadora):
    def __init__(self):#METODO, ACCION
        Calculadora.__init__(self,1)
        
    def cuadrada(self):#METODO, ACCION
        import math
        a, = self.datos 
        print("El resultado es:",(math.sqrt(a)))
        
objeto=opbasicas()#llamar a la clase que se nesecita 

print(isinstance(objeto,opbasicas))# funcion integrad isinstance, verifica la herencia 
                                    #coma es para clases punto es para lo demas y metodo de constructor
print(isinstance(objeto,raiz))# deberia trabajr con la funcion raiz en creacion de objeto sera falso 


print(issubclass(raiz, Calculadora))#verifica las subclases si son verdareras o no 



