from typing import List
from domain.equipements import Equipement
from domain.personnages import Personnage
from domain.lancer_sort import LancerSortilege

class Sorcier(Personnage):

    equipements : List[Equipement]
    
    def __init__(self, 
        name :str , 
        maison : str, 
        lancer_sortilege  # le sorcier ne connait qu'unseul type de lancer de sortilege

    )->None:
        self.name = name
        self.maison = maison 
        self.lancer_sortilege = lancer_sortilege

    def attaquer(self)->str:
        return self.lancer_sortilege()