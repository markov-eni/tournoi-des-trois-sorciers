from domain.objets import Objet
from domain.personnages import Personnage
from typing import List
from abc import ABC

class Epreuve():
    def __init__(self, nom :str , description ,objets: List[Objet]):
        self.nom = nom
        self.description = description
        self.objets = objets
        
    def tenter(self, personnage : Personnage)->bool:
        return True

    def reussir(self):
        return True