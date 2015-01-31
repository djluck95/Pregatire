'''
Created on 31 ian. 2015

@author: Darius
'''


class UI():
    def __init__(self, ctr):
        self.ctr = ctr
    
    def adaugare (self):
        c1 = input("da")
        l1 = input("da")
        c2 = input("da2")
        l2 = input("da2")
        try:
            self.ctr.adaugare(c1, l1, c2, l2)
        except ValueError as MSG:
            print (MSG)
            
    def cauta(self):
        lb = input ('Dati limba !')
        lista = self.ctr.cauta(lb)
        
        for el in lista:
            print (el.get_c_1(), el.get_l_1(), el.get_c_2(), el.get_l_2())
    
    
    def traducere(self):
        lb1 = input ('Dati limba 1!')
        lb2 = input ('Dati limba 2!')
        num1 = input('dati nume fisier sursa')
        num2 = input('dati nume fisier destinatie')
        self.ctr.trz( num1, lb1, num2, lb2)
        
    
    def run(self):
        while True:
            print ("meniu") 
            c = input("dai")
            if c =='1':
                self.adaugare()
            elif c== '2':
                self.cauta()
            elif c== '3':
                self.traducere()
            else:
                print ("Comanda invalida Boule")
        
        