'''
Created on 31 ian. 2015

@author: Darius
'''
class ValTraducere():
    def validare(self, tr):
        erori = []
        if tr.get_c_1() == '':
            erori.append("Plm vida.. trist")
        if tr.get_c_2() == '':
            erori.append("Plm vida.. trist")
        if len(erori) > 0:
            raise ValueError(erori)