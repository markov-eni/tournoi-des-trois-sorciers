from typing import List
from equipements import Equipement
from jeu import Personnage


class Sorcier(Personnage):

    equipements : List[Equipement]
    
    def __init__(self, 
        name :str = "Drago Malefoy", 
        maison : str =" Serpentard", 

    )->None:
        self.name = name
        self.maison = maison 
