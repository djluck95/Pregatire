'''
Created on 31 ian. 2015

@author: Darius
'''
class Traducere():
    def __init__(self, c1, l1, c2, l2):
        self.__c1=c1
        self.__l1=l1
        self.__c2=c2
        self.__l2=l2

    def get_c_1(self):
        return self.__c1


    def get_l_1(self):
        return self.__l1


    def get_c_2(self):
        return self.__c2


    def get_l_2(self):
        return self.__l2


    def set_c_1(self, value):
        self.__c1 = value


    def set_l_1(self, value):
        self.__l1 = value


    def set_c_2(self, value):
        self.__c2 = value


    def set_l_2(self, value):
        self.__l2 = value

    def __eq__(self, ot):
        pass # fac eu !!!!
        
        
    