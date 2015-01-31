'''
Created on 31 ian. 2015

@author: Darius
'''
from domain.traducere import Traducere
class CtrTraducere():
    def __init__(self, repo, val):
        self.repo = repo
        self.val = val
        
    def adaugare(self, c1, l1, c2, l2):
        tr = Traducere(c1, l1, c2, l2)
        self.val.validare(tr)
        self.repo.adaugare(tr)
        
    def cauta (self, lb):
        lista = self.repo.getAll()
        final=[]
#         print (lista)
        for x in lista:
            if x.get_l_1() == lb:
                final.append(x)
            if x.get_l_2() == lb:
                final.append(Traducere(x.get_c_2(),x.get_l_2(),x.get_c_1(),x.get_l_1()))
        final = sorted (final, key= lambda x:x.get_c_1(), reverse = False)
        return final
    
    
    def traducerecuv(self,cv, l1,l2):
        lista = self.repo.getAll()
        for e in lista:
            if e.get_l_1() == l1 and e.get_c_1() == cv and e.get_l_2() == l2:
                return e.get_c_2()
            if e.get_l_1() == l2 and e.get_c_2() == cv and e.get_l_2() == l1:
                return e.get_c_1() 
            
        return None
    
    def trz(self, num1, l1, num2, l2):
        f=open(num1, 'r')
        continut = f.read()
        f.close()
        cuv = continut.split(' ')
        g=open(num2, 'w')
        for c in cuv:
            x= self.traducerecuv(c, l1, l2)
            if x != None:
                g.write(x+' ')
                
            else:
                g.write('{'+c+'} ')
        g.close()
        
        
        
        
        