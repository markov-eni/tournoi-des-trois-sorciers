from typing import List
from domain.models.equipements import Equipement
from domain.models.personnages import Personnage
from domain.models.lancer_sort import LancerSortilege

class Sorcier(Personnage):

    equipements : List[Equipement]
    
    def __init__(self)->None:
        pass
    def attaquer(self)->str:
        return self.lancer_sortilege()