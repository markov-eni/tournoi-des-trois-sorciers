from typing import List
from domain.equipements import Equipement
from domain.personnages import Personnage
from domain.lancer_sort import LancerSortilege

class Sorcier(Personnage):

    equipements : List[Equipement]
    
    def __init__(self)->None:
        pass
    def attaquer(self)->str:
        return self.lancer_sortilege()