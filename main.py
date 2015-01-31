'''
Created on 31 ian. 2015

@author: Darius
'''
from repository.repo import FileRepo
from controller.ctr_tranducere import CtrTraducere
from UI.UI import UI
from domain.val_tr import ValTraducere
rep= FileRepo("Alandala.txt")
val = ValTraducere()
ctr= CtrTraducere(rep, val)
ui = UI(ctr)


ui.run()