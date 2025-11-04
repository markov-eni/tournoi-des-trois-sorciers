from typing import List
from equipements import Equipement
from jeu.personnage import Personnage
from jeu.lancer_sortilege import LancerSortilege

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