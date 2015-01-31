'''
Created on 31 ian. 2015

@author: Darius
'''
from domain.traducere import Traducere
class FileRepo():
    def __init__(self, fis):
        self.numefis=fis
        self.lista=[]
        self.citire()
        
    def adaugare(self, elem):
        self.lista.append(elem)
        self.salvare()
    
    def getAll(self):
        return self.lista
    
    
    def salvare(self):
        f=open(self.numefis,'w')
        
        for e in self.lista:
            f.write(e.get_c_1()+','+e.get_l_1()+','+e.get_c_2()+','+e.get_l_2()+'\n')
        
        f.close()
        
    def citire(self):
        try:
            f=open(self.numefis,'r')
            f.close()
        except FileNotFoundError:
            f=open(self.numefis,'w')
            f.close()
        f=open(self.numefis,'r')
        continut = f.read()
        f.close()
        linii =  continut.split('\n')
        self.lista = []
        for linie in linii:
            el = linie.split(',')
            if len (el) ==4:
                c = Traducere(el[0],el[1],el[2],el[3])
                self.lista.append(c)
        
        
        
        
        