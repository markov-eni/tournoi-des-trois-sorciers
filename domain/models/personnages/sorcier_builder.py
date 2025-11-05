from domain.models.personnages.sorcier import Sorcier
from domain.models.lancer_sort import LancerSortilege

class SorcierBuilder:
    
    sorcier : Sorcier

    def __init__(self):
        pass

    def create(self):
        self.sorcier = Sorcier()
        return self 

    def nom(self,nom:str):
        self.sorcier.nom = nom
        return self 

    def maison(self, maison:str):
        self.sorcier.maison = maison
        return self 

    def lancer_sortilege(self,lancer_sortilege : LancerSortilege ):
        self.sorcier.lancer_sortilege = lancer_sortilege
        return self

    def build(self)->Sorcier:
        return self.sorcier